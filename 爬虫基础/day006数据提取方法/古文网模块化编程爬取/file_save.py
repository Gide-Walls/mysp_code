import os
import re
import time

def w_html(url,response):
    path_1=r"爬虫基础\day006数据提取方法\数据"
    #判断文件是否创建
    if not os.path.exists(path_1):
        os.makedirs(path_1)
        print(f"已创建{path_1}")
    page_match=re.search(r"page=(\d+)",url)
    if page_match:
        page_num=page_match.group(1)
    else:
        page_num=f"未知页码_{int(time.time()*1000)}"
    file_name=f"古诗文{page_num}.html"
    file_path=os.path.join(path_1,file_name)
    if  os.path.exists(file_path):
        print(f"文件{file_path}已存在")
        return
        
    with open(file_path,"w",encoding="utf-8")as f:
        f.write(response.text)
    print(f"文件{file_path}写入成功")
        
