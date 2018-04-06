# -*- coding: utf-8 -*-
import scrapy
import pymysql
import pyquery
from housegz.items import HousegzItem
from lxml import etree
import re
import datetime


# 图片转换数字
def jpg_to_number(jpg):
    switcher = {
        "b24e802f1a.gif": "0",
        "039fbdc9ac.gif": "1",
        "3c4838d8df.gif": "2",
        "2c1083d291.gif": "3",
        "848977f965.gif": "4",
        "66e0539ab9.gif": "5",
        "231c818b33.gif": "6",
        "e5579ef2de.gif": "7",
        "449c4759fc.gif": "8",
        "cef652e275.gif": "9",

    }
    return switcher.get(jpg, "nothing")

#根据html返回具体数字
def reconjpg_str(jpgpath):
    res_key = r'images/(.*?)" width'
    t_str = re.findall(res_key, jpgpath, re.S | re.M)
    str_rtn_num = ""
    for strn in t_str:
        str_rtn_num = str_rtn_num + jpg_to_number(strn)
   # rtn_num=int(str_rtn_num)
    return str_rtn_num

# 小数网页内容处理
def floathtml(htmltext):
        floatnum =""
        if htmltext.find(">.<") != -1:
            num_int = str(htmltext).split(">.<", 1)[0]
            ys1 = reconjpg_str(num_int)
        #    print("ys1:", ys1)
            num_ws = str(htmltext).split(">.<", 1)[1]
            ys2 = reconjpg_str(num_ws)
        #   print("ys2", ys2)
            floatnum = float(ys1 + "." + ys2)
        else:
            floatnum = float(Inthtml(htmltext))
        #print(str(floatnum))
        return  floatnum

# 整数网页内容处理
def Inthtml(htmltext):
    str_num=""
    strnum =reconjpg_str(htmltext)
    intnum=int(strnum)
    return  intnum

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['gzcc.gov.cn']
#       start_urls = ['http://housing.gzcc.gov.cn/fyxx/ysz/index_1.shtml']
    start_urls = ['http://www.gzcc.gov.cn/housing/fyxx/fdcxmxx/index_1.shtml']

#start_urls = ['http://www.gzcc.gov.cn/housing/search/project/p++roject_detail.jsp?changeproInfoTag=1&changeSellFormtag=1&pjID=100000019095&name=fdcxmxx']

    def parse_strurl(self, response):
        print("搜索页面地址", str(response.url))
        urli = 0
        for strlink in response.xpath('//tr/td/a/@href').extract():
            if strlink.find("pjID=") != -1:
                res_key = r'pjID=(.*?)&name'
                proj = re.findall(res_key, strlink, re.S | re.M)[0]
                link = "http://www.gzcc.gov.cn/housing/search/project/project.jsp?pjID=" + str(proj)
                yield scrapy.Request(link, callback=self.parse_dir_contents)
                urli = urli + 1

    #    print("总共爬取Url:", str(urli),"============")


    def parse(self, response):
        strpagepath = response.xpath('//table[5]/tr[1]/td[1]').extract()

        pagei =  re.findall(r'\d+', str(strpagepath))
        pageinum=int(pagei[0])
        print("pagei",pagei[0])

        #   for i in range(1, 2):
        for i in range(1, pageinum):
        #    strurl = "http://www.gzcc.gov.cn/housing/ysz/fdcxmxx/index_" + str(i) + ".shtml"
            strurl = "http://www.gzcc.gov.cn/housing/fyxx/fdcxmxx/index_" + str(i) + ".shtml"
            print(strurl)
            yield scrapy.Request(strurl, callback=self.parse_strurl)

        pass



    def filter1(html):
        """过滤网页源码中的特殊符号和sup标签"""
        return remove_tags(html, which_ones=('sup',)).replace('\n', '') \
            .replace('\r', '').replace('\t', '').replace('\xa0','')

    def clean(s):
        """去除字符串两边的空格"""
        return s.strip() if s else ''

    def parse_dir_contents(self,response):
        print("strpj",str(response.url) )
        strpj = re.findall(r'\d+', str(response.url))
        item = HousegzItem()

        print("projid", str(strpj[0]))
        ysnum = ""          #预售证套数
        rgnum =""           #认购套数

        # 获取批准预售证套数
        for ysnums in  response.xpath('//div[@class="content"]/table[1]/tr[6]/td[2]/img/@src').extract():
            temp = ysnums[-14:]
            print(temp)
            ysnum=ysnum+jpg_to_number(temp)

        int_ysnum = int(ysnum)
    #    print("批准预售证套数",str(int_ysnum))

        # 获取批准预售证面积·
        ys_areas = response.xpath('//div[@class="content"]/table[1]/tr[6]/td[4]').extract()
        ysarea = floathtml(str(ys_areas))
    #    print("批准预售证面积",str(ysarea))

        strprojname = response.xpath('//div[@class="content"]/table[1]/tr[1]/td[2]/text()').extract()
        strcompany = response.xpath('//div[@class="content"]/table[1]/tr[3]/td[2]/text()').extract()

        # 已售总套数
        rgpath = response.xpath('//div[@class="content"]/table[1]/tr[7]/td[2]').extract()
        rgnum=Inthtml(str(rgpath))
     #   print("已售总套数", str(rgnum))

        # 未售总套数
        wspath = response.xpath('//div[@class="content"]/table[1]/tr[7]/td[4]').extract()
        wsnum = Inthtml(str(wspath))
    #    print("未售总套数", str(wsnum))

        # 已售总面积
        rgareapath = response.xpath('//div[@class="content"]/table[1]/tr[8]/td[2]').extract()
        rgarea = floathtml(str(rgareapath))
    #    print("已售总面积", str(rgarea))

        # 未售总面积
        wsareapath = response.xpath('//div[@class="content"]/table[1]/tr[8]/td[4]').extract()
        wsarea= floathtml(str(wsareapath))
    #    print("未售总面积", str(wsarea))


        # 住宅当天已售套数
        today_rgpath = response.xpath('//div[@class="content"]/table[2]/tr[3]/td[2]').extract()
        today_rgnum = Inthtml(str(today_rgpath))
    #    print("住宅已售套数", str(today_rgnum))

        # 住宅当天认购面积
        today_rgarpath = response.xpath('//div[@class="content"]/table[2]/tr[3]/td[3]').extract()
        today_rgarea = floathtml(str(today_rgarpath))
    #    print("住宅已售面积", str(today_rgarea))

        # 住宅当天退房套数
        today_tfpath = response.xpath('//div[@class="content"]/table[2]/tr[3]/td[4]').extract()
        today_tf = Inthtml(str(today_tfpath))
    #    print("住宅当天退房", str(today_tf))


        # 采集日期
        putdatepath = response.xpath('//*[@id ="currentDate"]/text()')[0].extract()
        putdate=putdatepath
    #    print ("putdate",putdate)

        # 商铺当天已售套数
        today_rgpath = response.xpath('//div[@class="content"]/table[2]/tr[4]/td[2]').extract()
        today_shrgnum = Inthtml(str(today_rgpath))
    #    print("商铺已售套数", str(today_shrgnum))


        # 商铺当天认购面积
        today_rgarpath = response.xpath('//div[@class="content"]/table[2]/tr[4]/td[3]').extract()
        today_shrgarea = floathtml(str(today_rgarpath))
    #    print("商铺已售面积", str(today_shrgarea))


        # 商铺当天退房套数
        today_tfpath = response.xpath('//div[@class="content"]/table[2]/tr[4]/td[4]').extract()
        today_shtf = Inthtml(str(today_tfpath))
    #    print("商铺退房套数", str(today_shtf))
        # 住宅累计均价
        hsprice_path = response.xpath('//div[@class="content"]/table[2]/tr[3]/td[7]').extract()

        houseprice=Inthtml(str(hsprice_path))

        shprice_path = response.xpath('//div[@class="content"]/table[2]/tr[4] / td[7]').extract()

        shprice = Inthtml(str(shprice_path))

        strpresaleno = response.xpath('//div[@class="content"]/table[1]/tr[1]/td[4]/text()').extract()
        stradminarea = response.xpath('//div[@class="content"]/table[1]/tr[3]/td[4]/text()').extract()

        if len(strpresaleno) == 0:
            strpresaleno = ""

        presaleno = strpresaleno
        print("presaleno",str(presaleno))

        print("stradminarea", str(stradminarea))
        print("========================")
        item["projid"] = str(strpj[0])  #项目ID
        item["sysnum"] = int(int_ysnum)  #批准预售证套数
        item["sysarea"] = float(ysarea)  #批准预售面积
        item["srgnum"] = int(rgnum)      #已售总套数
        item["swsarea"] = float(wsarea)  #未售总面积
        item["srgarea"] = float(rgarea)  #已售总面积
        item["swsnum"] = int(wsnum)      #未售总套数
        item["stoday_zrgnum"] = int(today_rgnum)       #住宅已售套数
        item["stoday_zrgarea"] = float(today_rgarea)    #住宅已售面积
        item["stoday_tfz"] = float(today_tf)            #住宅当天退房
        item["rgdate"] = putdate                         #采集日期
        item["stoday_shoprgnum"] = today_shrgnum       # 当天商铺认购套数
        item["stoday_sharea"] = today_shrgarea          # 当天商铺认购面积
        item["stoday_shtfsh"] = today_shtf              # 当天商铺退房套数
        item["projname"] = strprojname              # 项目名称
        item["company"] = strcompany                # 公司名
        item["houseprice"] = houseprice             # 住宅均价
        item["shprice"] = shprice                   # 商铺均价
        item["adminarea"] = stradminarea               #行政区域
        item["presaleno"] = presaleno             # 预售证

        yield item