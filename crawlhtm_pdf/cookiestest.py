import requests
import re

def GetCookie():

    s=requests.session()

    loginUrl='http://10.1.9.159/reports/powerbi/%E6%9C%88%E5%BA%A6%E7%BB%8F%E8%90%A5%E4%BC%9A%E8%AE%AE/01%20%E7%BB%8F%E8%90%A5%E6%9C%88%E6%8A%A5'
    postData={'pname':'bhybidb1','password':'111111,a' }
    rs=s.post(loginUrl,postData)
    c=requests.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
    c.set('cookie-name','cookie-value')
    s.cookies.update(c)
    print(s.cookies.get_dict())

if __name__ == '__main__':
    GetCookie()