# -*- coding: utf-8 -*-

# Scrapy settings for ajk_es project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ajk_es'

SPIDER_MODULES = ['ajk_es.spiders']
NEWSPIDER_MODULE = 'ajk_es.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ajk_es (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 4.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'zh-CN,zh;q=0.9',

   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3047.4 Safari/537.36',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ajk_es.middlewares.AjkEsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    #'ajk_es.middlewares.MyCustomDownloaderMiddleware': 543,
#    # 'ajk_es.middlewares.UserAgentMiddleware': 543,
#    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 511,
# #   'ajk_es.middlewares.IPPOOLS': 540,
#
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ajk_es.pipelines.AjkEsPipeline': 300,
   'ajk_es.pipelines.AjkesPipelinejson': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#ip 池设置
#http://www.daxiangdaili.com/web?tid=556562604570496
IPPOOL=[
   {"ippaddr": "125.118.144.161:61234"},
   {"ippaddr": "118.254.153.3:3128"},
   {"ippaddr": "114.227.131.232:6666"},
   {"ippaddr": "125.109.195.80:31000"},
   {"ippaddr": "118.254.148.172:3128"},
   {"ippaddr": "115.213.224.28:44998"},
   {"ippaddr": "110.88.247.180:35545"},
   {"ippaddr": "101.201.209.207:7777"},
   {"ippaddr": "60.174.74.40:8118"},
   {"ippaddr": "59.58.222.204:25721"},
   {"ippaddr": "60.175.196.97:30272"},
   {"ippaddr": "1.192.230.7:45053"},
   {"ippaddr": "124.235.144.136:80"},
   {"ippaddr": "121.231.168.163:6666"},
   {"ippaddr": "123.180.69.246:8010"},
   {"ippaddr": "60.182.179.101:22019"},
   {"ippaddr": "14.112.76.126:61234"},
   {"ippaddr": "117.69.231.170:61234"},
   {"ippaddr": "110.73.6.189:8123"},
   {"ippaddr": "175.155.247.78:808"},
   {"ippaddr": "182.88.190.245:8123"},
   {"ippaddr": "59.51.123.108:3128"},
   {"ippaddr": "222.76.187.73:8118"},
   {"ippaddr": "123.53.132.243:37922"},
   {"ippaddr": "180.121.131.59:3128"},
   {"ippaddr": "120.37.165.173:48138"},
   {"ippaddr": "182.202.221.60:61234"},
   {"ippaddr": "119.190.34.70:80"},
   {"ippaddr": "211.159.219.158:80"},
   {"ippaddr": "180.121.131.233:808"},
   {"ippaddr": "163.177.151.23:80"},
   {"ippaddr": "14.215.177.73:80"},
   {"ippaddr": "14.215.177.58:80"},
   {"ippaddr": "125.121.133.50:808"},
   {"ippaddr": "180.149.131.67:80"},
   {"ippaddr": "121.8.98.197:80"},
   {"ippaddr": "180.97.104.14:80"},
   {"ippaddr": "218.59.139.238:80"},
   {"ippaddr": "120.199.64.163:8081"},
   {"ippaddr": "27.40.155.118:61234"},
   {"ippaddr": "114.112.104.223:80"},
   {"ippaddr": "112.80.255.32:80"},
   {"ippaddr": "180.116.204.110:6666"},
   {"ippaddr": "218.107.137.197:8080"},
   {"ippaddr": "171.80.88.4:1080"},
   {"ippaddr": "123.125.142.40:80"},
   {"ippaddr": "49.73.191.52:8118"},
   {"ippaddr": "27.217.107.25:8118"},
   {"ippaddr": "111.62.243.64:8080"},
   {"ippaddr": "115.239.210.42:80"},
   {"ippaddr": "112.80.255.21:80"},
   {"ippaddr": "163.177.151.162:80"},
   {"ippaddr": "121.8.98.198:80"},
   {"ippaddr": "222.76.187.147:8118"},
   {"ippaddr": "49.81.251.123:8118"},
   {"ippaddr": "123.125.115.86:80"},
   {"ippaddr": "222.85.5.50:61234"},
   {"ippaddr": "49.79.194.13:61234"},
   {"ippaddr": "180.212.140.84:8118"},
   {"ippaddr": "220.181.163.231:80"},
   {"ippaddr": "14.118.254.34:6666"},
   {"ippaddr": "218.26.227.108:80"}
]
