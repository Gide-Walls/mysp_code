import re

#匹配多个字符

#匹配多个字符
result=re.match('1*','111111111654646461111111111111111111111111111111111')
print(result.group())

#*匹配0个或多个
result = re.match('1*', '1111111111111111111111111111111111111')
print(result.group())


#匹配一个或者多个
result = re.match('1+', '1111111111111111111111111111111111111')
print(result.group())



# 注释修正：? 表示匹配前一个字符0次或1次，但re.match()从开头匹配时，
# 若开头有该字符，则优先匹配1次（而非0次），因此结果为'1'。
result = re.match('1?', '1111111111111111111111111111111111111')
print(result.group())

#正则有贪婪或者非贪婪 加个问号就是非贪婪
result=re.match('1*?','111111111654646461111111111111111111111111111111111')
print(result.group())


#匹配指定个数的字符
result=re.match('4{4}','4444444444444444444444444')
print(result.group())

result=re.match('[0-9]{9}','4444444444444444444444444')
print(result.group())


#{m,n}匹配m到n个数字

result=re.match(r'[1-9]\d{6,12}@qq\.com',"123456789@qq.com")
print(result)
