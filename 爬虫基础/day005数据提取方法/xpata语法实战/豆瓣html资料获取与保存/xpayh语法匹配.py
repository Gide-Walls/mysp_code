from lxml import etree
import json
import os
base_dir=r"爬虫基础\day005数据提取方法\xpata语法实战\豆瓣html资料获取与保存"
file_name="排行榜.html"
file_path=os.path.join(base_dir,file_name)
with open(file_path,"r",encoding="utf-8")as f:
    html_content=f.read()

tree=etree.HTML(html_content)
books=[]
book_name_list=tree.xpath('//li[contains(@class, "media") and contains(@class, "clearfix")]')
for idx,li in enumerate(book_name_list,1):
    #提取书名
    book_name_xpath=li.xpath('.//a[@class="fleft"]/text()')[0]
    #提取信息
    book_lnfo=' '.join(li.xpath('//p[@class="subject-abstract color-gray"]/text()')[0].split())
    comment_count=li.xpath('.//span[@class="fleft ml8 color-gray"]/text()')[0].strip('()').strip()
    
    
    book_list={
        "序号":f"{idx}",
        "书名":book_name_xpath,
        "信息":book_lnfo,
        "评价数量":comment_count
    }
    books.append(book_list)
print(books)
for i in books:
    print(i)


