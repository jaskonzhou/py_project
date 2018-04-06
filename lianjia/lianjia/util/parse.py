# code:utf8
from pyquery import PyQuery
import re
import hashlib

page_verif_list={}

def urllastparse(response):
    jpy = PyQuery(response.text)
    lastpage1title = jpy('body > div.content > div.leftContent > ul > li:nth-child(1) > div.info.clear > div.title > a').text()
    lastpage2title = jpy('body > div.content > div.leftContent > ul > li:nth-child(2) > div.info.clear > div.title > a').text()
    lastpage1price = jpy('body > div.content > div.leftContent > ul > li:nth-child(1) > div.info.clear > div.priceInfo > div.totalPrice > span').text()
    lastpage2price = jpy('body > div.content > div.leftContent > ul > li:nth-child(2) > div.info.clear > div.priceInfo > div.totalPrice > span').text()
    page_tag=lastpage1title+lastpage1price+lastpage2title+lastpage2price
    page_verif = hashlib.md5(page_tag.encode('utf-8')).hexdigest()
    print("page_verif:",page_verif)
    ifgo = 'yes'
    for list1 in page_verif_list:
        print("list1",list1)
        print("page_verif:", page_verif)
        if list1 == page_verif:
            print("==============当前页面重复了==============")
            ifgo = 'no'
            return ifgo
        page_verif_list.add(page_verif)
    return ifgo

def urlhousparse(response):
    jpy = PyQuery(response.text)

    tr_list = jpy('body > div.content > div.leftContent > ul > li').items()

    result = set()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('div.info.clear > div.title >  a').attr('href')  # 爬取房间的url
        result.add(url)
        print("url",url)
    return result

def housedetail(response):
    result = dict()
    jpy = PyQuery(response.text)
    result['housename'] = jpy('body > div.overview > div.content > div.aroundInfo > div.communityName > a.info').text()
    result['xqarea'] = jpy('body > div.overview > div.content > div.aroundInfo > div.areaName > span.info > a:nth-child(1)').text()
    result['xzarea'] = jpy('body > div.overview > div.content > div.aroundInfo > div.areaName > span.info >a:nth-child(2)').text()
    result['total'] = jpy('body > div.overview > div.content > div.price > span.total').text()
    result['price'] = jpy('body > div.overview > div.content > div.price > div.text > div.unitPrice > span').text()
    result['bldarea'] = jpy('body > div.overview > div.content > div.houseInfo > div.area > div.mainInfo').text()
    strbyear = jpy('body > div.overview > div.content > div.houseInfo > div.area > div.subInfo').text()
    t=re.findall(r'\d+', strbyear)
    if t:
        result['buildyear'] = str(t[0])
    else:
        result['buildyear'] =""
    return result

if __name__ == '__main__':
    import requests
    r = requests.get('https://gz.lianjia.com/ershoufang/tianhe/')
    housedetail(r)