import re

# 文本所在TXT文件
file = '123.txt'

# 关键字1,2(修改引号间的内容)
w1 = '股票池'
w2 = '到此为止'

f = open(file, 'r',encoding='utf-8')
buff = f.read()
# 清除换行符,请取消下一行注释
buff = buff.replace('\n','')
pat = re.compile(w1 + '(.*?)' + w2, re.S)
result = pat.findall(buff)
print(result)


str1='abc'
str2='4322'
result1=str1+str2
print(result1)