import os
import sys
from reportlab.lib.pagesizes import A4, landscape

from reportlab.pdfgen import canvas

def convert2pdf():
    # 获取横向A4大小
    (w, h) = landscape(A4)
    # 遍历当前目录
    for root, dirs, files in os.walk(os.getcwd()+"\png"):
        # 根据根目录名创建一个pdf
    #    c = canvas.Canvas(os.path.basename(root) + ".pdf", pagesize=landscape(A4))
        c = canvas.Canvas(os.path.basename(root) + ".pdf", pagesize=(1280, 640))
        # print(os.path.basename(root)+".pdf")
        # 用于存放jpg文件
        jpg_list = []
        # 从文件列表中取出jpg文件放入到list中
        for p in files:
            # 将jpg文件名存入列表
            if p[-4:] == '.png':
                # jpg_list.append(root + "\\" +p)
                jpg_list.append(p)
        # 对文件名称排序
#        jpg_list.sort(key=lambda x: int(x[:-4]))
        for f in jpg_list:
            # 按顺序把图片画到画布上
            c.drawImage(root + "\\" + f, 0, 0, 1280, 640)
            # 结束当前页并新建页
            c.showPage()
        c.save()
    print("ok.")


convert2pdf()