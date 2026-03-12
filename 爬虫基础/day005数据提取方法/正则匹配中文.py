import re



text="你好 我是大白sdafds"

#[]意思是 取一个范围
ree=re.findall('[\u4e00-\u9fa5]+',text)
print(ree)




