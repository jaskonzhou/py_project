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

    tr_list = jpy('#houselist-mod-new > li:nth-child(1) > div.house-details > ').items()

    result = set()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('  div.house-title > a').attr('href')  # 爬取房间的url
        result.add(url)
        print("trueurl",url)

    return result


'查询楼栋具体信息'
def housedetail(response):
        result = dict()
        jpy = PyQuery(response.text)
        result['url'] = response.url
        result['projname'] = jpy('#content > div.wrapper > div.wrapper-lf.clearfix > div.houseInfoBox > div > div.houseInfo-wrap > div > div.first-col.detail-col > dl:nth-child(1) > dd > a').text()
        print(result['projname'])
        strprice = jpy('#content > div.wrapper > div.wrapper-lf.clearfix > div.houseInfoBox > div > div.houseInfo-wrap > div > div.third-col.detail-col > dl:nth-child(2) > dd').text()
        print(result['strprice'])
        xzarea = jpy('#content > div.p_1180.p_crumbs > a:nth-child(1)').text()
        xzarea = xzarea.replace('房产网','区域')
        result['xzarea'] = xzarea
        result['area'] = jpy('#content > div.wrapper > div.wrapper-lf.clearfix > div.houseInfoBox > div > div.houseInfo-wrap > div > div.first-col.detail-col > dl:nth-child(2) > dd > p > a:nth-child(1)').text()
        print(result['area'])
        result['position'] = jpy('#content > div.wrapper > div.wrapper-lf.clearfix > div.houseInfoBox > div > div.houseInfo-wrap > div > div.first-col.detail-col > dl:nth-child(2) > dd > p > a:nth-child(2)').text()
        print(result['position'])



        return result