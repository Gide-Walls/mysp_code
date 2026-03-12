from bs4 import BeautifulSoup
import re



with open(r"爬虫基础\day006数据提取方法\bs4学习\单页面测试代码\html单页面数据\道友你在和谁说话.html","r",encoding="utf-8")as f:
    read_html=f.read()
    
soup=BeautifulSoup(read_html,"lxml")
#prettifu()美化打印和源代码一样
#find_all 

# suop.find_all("a")

#获取所有当前a标签 #获取的是列表
# print(suop.find_all('div'))

#直接传正则表达式

# i_list=soup.find_all(re.compile('^i'))
# li=soup.find_all(["div","a"])#传列表
# div=soup.find_all("div",attrs={"id":"list"})#根据属性去获取

# divv=soup.find("div")#获取1个
# print(divv)


#css选择器
#定位和 find_all一样的
# div=soup.select('div')#标签选择器

# print(div)
# class_data=soup.select(".box_con")#类选择器
# print(class_data)

#id选择器
# id_data=soup.select("#sidebar")#id是#写

# print(id_data)


#层级选择器

# a=soup.select("div span")
# print(a)

#属性选择器 
# 

# texts=soup.select("dd a")
# print(texts[9].get('href'))