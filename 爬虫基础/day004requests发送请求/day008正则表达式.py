#正则表达式
import re
# result=re.match(正则表达式,要匹配的目标数据)
# result.group() 获取匹配到的结果

# result=re.match("tuling","tuling.cn")
# print(result.group())


#单个字符匹配
# result=re.match('.','kasfjdhksdhfksadhak')
# print(result.group())

result=re.match(r'\s','    ')
print("结果",result.group())




