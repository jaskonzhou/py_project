import sys
import importlib
importlib.reload(sys)
import re
import csv
import tabula
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

'''
 解析pdf 文本，保存到txt文件中
'''

path = r'E:\scrapy\json\180304.pdf'
#path = r'../../data/pdf/阿里巴巴Java开发规范手册.pdf'
def parse():
    fp = open(path, 'rb') # 以二进制读模式打开
    #用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pdftext=''
        # 循环遍历列表，每次处理一个page的内容
        pagei=1
        x1 = 1
        for page in doc.get_pages(): # doc.get_pages() 获取page列表
            print(x1)
            x1=x1 +1
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    #with open(r'E:\scrapy\json\1.txt', 'a') as f:
                        str = x.get_text()
                        results=str
                        #results = str.replace('\n', ',')
                        #print(results)
                     #   f.write(results + '\n')
                        if (str.find('601668')>0):
                            print(str)

                            break
                        #pdftext=pdftext+results
            pdftext = pdftext+'\n'
        pagei = pagei+1
    print(pagei)
    start_keyword='重仓线'
    end_keyword='1，建仓线是指值得买入的价位，这个价位是相对低位，不存在追高风险。'
#    pdftext = pdftext.replace('\n', '')
    pat = re.compile(start_keyword + '(.*?)' + end_keyword, re.S)
    result = pat.findall(pdftext)

    print('result',result)
    filename=r'E:\scrapy\json\tushare.csv'
    convert2csv(result,filename)

def convert2csv(str1,filename):
    data = str1
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\n')
        for line in data:
            writer.writerow(line)



if __name__ == '__main__':
    parse()