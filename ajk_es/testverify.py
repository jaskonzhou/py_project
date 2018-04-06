
# -*- coding:utf8 -*-
from urllib import request
import urllib
import socket
socket.setdefaulttimeout(3)

inf = open("e:\ip.txt")    # 这里打开刚才存ip的文件
lines = inf.readlines()
proxys = []
for i in range(0,len(lines)):
    proxy_host = "http://" + lines[i]
    proxy_temp = {"https":proxy_host}
    proxys.append(proxy_temp)

# 用这个网页去验证，遇到不可用ip会抛异常
#url = "http://ip.chinaz.com/getip.aspx"
url = "https://foshan.anjuke.com/sale/p3/#filtersort"
# 将可用ip写入valid_ip.txt
ouf = open("e:\ipvalid_ip.txt", "w")

for proxy in proxys:
    try:

        proxy_support = urllib.request.ProxyHandler(proxy)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3047.4 Safari/537.36'
        opener = urllib.request.build_opener(proxy_support)
        headers = {'User-Agent': user_agent}
        urllib.request.install_opener(opener)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req).read().decode("utf8")
        #res = request.urlopen(url,proxies=proxy).read()
        print(str(response))
        valid_ip = proxy['http'][7:]
        print('valid_ip: ' + valid_ip)
        ouf.write(valid_ip)
    except Exception as e:
        print(proxy)
        print(e)
        continue