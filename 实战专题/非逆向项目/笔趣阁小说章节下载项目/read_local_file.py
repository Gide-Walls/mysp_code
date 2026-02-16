from lxml import html
import re


# with open(r"爬虫基础\day006数据提取方法\bs4学习\单页面测试代码\html单页面数据\道友你在和谁说话.html","r",encoding="utf-8")as f:
#     content=f.read()
def default(content):
    tree=html.fromstring(content)#tree是元素对象不能直接打印


    # 查看元素信息
    # html_string=html.tostring(tree,encoding='unicode',pretty_print=True)
    # print(html_string)
    print(tree)

    chapter=tree.xpath(r'//div[@id="list"]/dl/dd[position()>=10]/a/text()')
    chapter_content=tree.xpath(r'//div[@id="list"]/dl/dd[position()>=10]/a/@href')

    #定义存储的列表
    chapter_list=[]
    for chap,cont in zip(chapter,chapter_content):
        chapter_list.append({
            "章节":chap,
            "链接":cont
        })
    print(chapter_list)

    day_link=[]
    for i in chapter_list:
        cont=f"https://www.xslca.cc{i["链接"]}"
        result=re.search(r'第(\d+).\s*(.*)',i["章节"])
        chapyer_num=result.group(1)
        charpter_name=result.group(2)
        all_name=f"day_{chapyer_num:0>5s}"
        day_link.append((all_name,cont,charpter_name))
    return day_link