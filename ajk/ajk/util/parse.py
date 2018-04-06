# code:utf8
from pyquery import PyQuery
import re
import hashlib



def urllastparse(response):
    jpy = PyQuery(response.text)
    title = jpy('#container > div.list-contents > div.list-results > div.key-list > div:nth-child(1) > div > a.lp-name > h3 > span').text()

    print("title:",title)
    ifgo = 'yes'
    print(str(len(title)))
    if len(title)<=0:
        ifgo='no'
        print('最后一页了')
    return ifgo

def urlhousparse(response):
    jpy = PyQuery(response.text)

    tr_list = jpy('#container > div.list-contents > div.list-results > div.key-list>div').items()

    result = set()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        flag_go = jpy('#container > div.list-contents > div.list-results > div.key-list > div:nth-child(1) > div > a.tags-wrap > div > i.status-icon.onsale').text()
        if (flag_go=='在售' or flag_go=='待售'):
            url = tr('  div > a.lp-name').attr('href')  # 爬取房间的url
            result.add(url)
            print("trueurl",url)
        else:
            url = tr('  div > a.lp-name').attr('href')  # 爬取房间的url
            print("非在售房源跳过",url)
    return result


'查询楼栋具体信息'
def housedetail(response):
        result = dict()
        jpy = PyQuery(response.text)
        result['url'] = response.url
        flag = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(1) > div.des > i').text()
        result['projname'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(1) > div.des > a').text()
        print(result['projname'])
        xzarea = jpy('#header > div.site-search.clearfix > div.crumb-item.fl > a:nth-child(1)').text()
        xzarea = xzarea.replace('安居客','区域')
        result['xzarea'] = xzarea
        if (flag == "待售" and xzarea=="中山区域"):
            result['price'] = 0
            print(result['price'])
            result['area'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(5) > div.des > a:nth-child(1)').text()
            print(result['area'])
            result['position'] = jpy( '#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(5) > div.des > a:nth-child(2)').text()
            print(result['position'])
            result['developer'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(4) > div.des > a').text()
            print(result['developer'])
        elif (flag == "在售" and xzarea=="中山区域"):
            strprice = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(3) > div.des').text()
            result['price'] = re.findall(r'\d+', strprice)[0]
            result['area'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(6) > div.des > a:nth-child(1)').text()
            result['position'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(6) > div.des > a:nth-child(2)').text()
            result['developer'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(5) > div.des > a').text()

        elif (flag == "待售" and xzarea!="中山区域"):
            result['price'] = 0
            print(result['price'])
            result['area'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(6) > div.des > a:nth-child(1)').text()
            print(result['area'])
            result['position'] = jpy( '#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(6) > div.des > a:nth-child(2)').text()
            print(result['position'])
            result['developer'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(5) > div.des > a').text()
            print(result['developer'])
        else:
            strprice = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(3) > div.des').text()
            result['price'] = re.findall(r'\d+', strprice)[0]
            print(result['price'])
            result['area'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(7) > div.des > a:nth-child(1)').text()
            print(result['area'])
            result['position'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(7) > div.des > a:nth-child(2)').text()
            print(result['position'])
            result['developer'] = jpy('#container > div.can-container.clearfix > div.can-left > div:nth-child(1) > div.can-border > ul > li:nth-child(6) > div.des > a').text()
            print(result['developer'])


        return result