import re
#match 从头开始匹配
# result=re.match(r'\d\d\d','1214uausdyFGD')
# print(result.group())

#search 找一个
# result=re.search(r'\d','uausd1yFGD')
# print(result.group())

#找所有返回列表
result=re.findall(r'\d','uausd1654yFGD')
print(result)

#sub替换数据
result=re.sub(r'\d','___','uausd1654yFGD')
print(result)

#re的修饰符
import re

text = "Hello WORLD hello world"

# 不使用修饰符 - 只匹配小写 hello
result1 = re.findall(r'hello', text)
print(result1)  # ['hello', 'hello']

# 使用 IGNORECASE - 匹配所有大小写组合
result2 = re.findall(r'hello', text, re.IGNORECASE)
print(result2)  # ['Hello', 'WORLD', 'hello', 'world']