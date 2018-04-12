#coding=utf-8
from __future__ import unicode_literals
import os,sys,re,time
import requests,codecs
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pdfkit
import platform
requests.packages.urllib3.disable_warnings()

system=platform.system()
print(sys.getdefaultencoding())

str_encode='gbk' if system is 'Windows' else 'utf-8'
print(str_encode)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""

if not os.path.exists(os.path.join(os.path.dirname(__file__),'html')):
    os.mkdir(os.path.join(os.path.dirname(__file__),'html'))


url_list=[]
start_url='http://www.ziqiangxuetang.com/django/django-tutorial.html'

# s=requests.session()
# html_doc=s.get('{}'.format(start_url),verify=False).content

# soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())

def get_url_list(url):
    """
    获取所有URL目录列表
    :return:
    """
    last_position = find_last(url, "/") + 1
    tutorial_url_head = url[0:last_position]
    domain = get_domain(url) + "/"
    print(domain)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    urls = []
    for a in soup.find_all("a"):
        href = str(a.get('href'))
        result = href.find('/')
        if result == -1:
            url = tutorial_url_head + href
        else:
            url = domain + href
        if 'django' in url:
            urls.append(url)
    return urls


def find_last(string, char):
    last_position = -1
    while True:
        position = string.find(char, last_position + 1)
        if position == -1:
            return last_position
        last_position = position


def get_domain(url):
    r = urlparse(url)
    return r.scheme + "://" + r.netloc


def parse_url_to_html(url,name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 正文
        body = soup.find_all(class_="w-col l10 m12")
        h = str(body)
        html = h[1:-1]
        html = html_template.format(content=html)
        html = html.encode("utf-8")
        title=soup.title.get_text()
        print(url)
        with open('{}/{}'.format(os.path.join(os.path.dirname(__file__),'html'),name), 'wb') as f:
            f.write(html)
        return '{}/{}'.format(os.path.join(os.path.dirname(__file__),'html'),name)
    except Exception as e:
        print(e)


def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 安装位置
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)

def main():
    start = time.time()
    urls = get_url_list(start_url)
    htmls = [parse_url_to_html(url, str(index) + ".html") for index, url in enumerate(urls)]
    print(htmls)
    try:
        save_pdf(htmls, 'cralwer_{}.pdf'.format(time.strftime('%Y_%m_%d_%H_%M_%S')))
    except Exception as e:
        print(e)
    for html in htmls:
            os.remove(html)
    total_time = time.time() - start
    print(u"总共耗时：{0:.2f}秒".format(total_time))



if __name__ == '__main__':
    main()