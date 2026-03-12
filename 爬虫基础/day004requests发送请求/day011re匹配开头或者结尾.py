import re

#以某某开头
ree=re.match('^[A-Z]\d{8,12}','A5465465464')
print(ree)
#以某某结尾
ree=re.match('^[A-Z]\d{8,12}\W','A5465465464/')
print(ree)