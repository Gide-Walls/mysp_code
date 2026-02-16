import os
def seve_content(filename,content):
    
    SAVE_DID=r"爬虫基础\day006数据提取方法\bs4学习\单页面测试代码\保存小说"
    os.makedirs(SAVE_DID,exist_ok=True)
    full_path=os.path.join(SAVE_DID,filename)
    
    with open(full_path,"w",encoding="utf-8")as f:
        f.write(content)
