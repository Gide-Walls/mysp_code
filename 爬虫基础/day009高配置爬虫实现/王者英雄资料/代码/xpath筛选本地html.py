from lxml import etree

with open(r'爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄主页.html','r',encoding='gbk')as f:
    html=f.read()
tree=etree.HTML(html)
list_data=tree.xpath('//ul[@class="herolist clearfix"]/li')
li_list=[]
for li in list_data:
    a_text = li.xpath('./a/text()')
    li_list.append(a_text)
    print(a_text)
print(len(li_list))