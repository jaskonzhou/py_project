#-*- coding: UTF-8 -*-
import requests
import re

def get_cookie():
#    with open('zhihu_cookie','r') as f:
     with open('oa.txt','r') as f:
        cookies={}
        for line in f.read().split(';'):
            name,value=line.strip().split('=',1)  #1代表只分割一次
            cookies[name]=value
        return cookies


s = requests.Session()
#url = 'http://10.1.9.159/reports/powerbi/%E6%9C%88%E5%BA%A6%E7%BB%8F%E8%90%A5%E4%BC%9A%E8%AE%AE/01%20%E7%BB%8F%E8%90%A5%E6%9C%88%E6%8A%A5'
#url = 'http://portal.timesgroup.cn/PIndex.aspx'
url = 'http://hcm.timesgroup.cn/hr/home'



headers = {
    'Host':'hcm.timesgroup.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    #'reffer':'http://10.1.9.159/powerbi/?id=2d343a90-562c-467c-b8ca-d36b2cc01127&hostdata=%7B%22Build%22:%2215.0.2.389%22,%22ExternalUser%22:%22True%22,%22IsPublicBuild%22:true,%22Host%22:%22Microsoft.ReportingServices.Portal.Services%22,%22HashedUserId%22:%22087CC85343BECC6AD0EA5E96F5D957E53E4912AD589D005E2EAE962887E45BEF%22,%22InstallationId%22:%228fc4650c-8115-403c-8d7a-2faca8b453c7%22,%22IsEnabled%22:true,%22Edition%22:%22PBIRS%20Developer%22,%22AuthenticationTypes%22:%22RSWindowsNTLM%22,%22NumberOfProcessors%22:4,%22NumberOfCores%22:32,%22IsVirtualMachine%22:true,%22MachineId%22:%228A633067A7E551765A2E9D37A37CCCF1%22,%22CountInstances%22:2,%22Count14xInstances%22:0,%22Count13xInstances%22:1,%22Count12xInstances%22:0,%22Count11xInstances%22:0,%22ProductSku%22:%22SSRSPBI%22%7',
    }
#print(get_cookie())
#requests.utils.add_dict_to_cookiejar(s.cookies,get_cookie())
#oacookies={ 'ASP.NET_SessionId':'u5zuhneubajr1gkenuz32rf4'}
cookies={'JSESSIONID':'51140392BB370A920E137384961ACC72'}
#oacookies={ "ASP.NET_SessionId=u5zuhneubajr1gkenuz32rf4":"path=":"HttpOnly" }
req2 = s.get(url, headers = headers, cookies =cookies,  verify=False)
#req2 = s.get(url, headers = headers, cookies =get_cookie(),  verify=False)
html = req2.content
response = requests.get(url)
#print(html)
#print(response)
#soup = BeautifulSoup(response.content, 'html.parser')


#将获取到的页面源码写入zhihu.html文件中
with open('zhihu.html','w') as fl:
      fl.write(str(html))
