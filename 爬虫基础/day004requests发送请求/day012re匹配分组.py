import re



#   | 或

result=re.match('163|qq|126','qq')
print(result)



#  ()进行分组

result=re.match('[1-9]{5,12}@(163|qq|126)\.com','213213121@qq.com')
print(result)


#  \num 引入分组

result=re.match(r'<[a-zA-Z1-6]+>(.*)</[a-zA-Z1-6]+>','<span>aa</span>')
print(result.group(1))#写1是匹配第一个分组


import re

# result = re.match(r'<([a-zA-Z1-6]+)>.*/\1>', '<span>aa</span>')#  \1>是引用第一个分组的内容
# if result:
#     print("匹配成功")
#     print("捕获的标签名:", result.group(1))
# else:
#     print("匹配失败")

#(?P)  给分组起名
result = re.match('<(?P<baichuan1>[a-zA-Z1-6]+)>.*</\\1>', '<span>aa</span>')
print(result.group(0))#里面的0代表完整的匹配
print(result.group(1))


#(?P)给分组起别名
result = re.match(r'<(?P<baichuan1>[a-zA-Z1-6]+)>.*/(?P=baichuan1)>', '<span>aa</span>')
print(result.group(0))