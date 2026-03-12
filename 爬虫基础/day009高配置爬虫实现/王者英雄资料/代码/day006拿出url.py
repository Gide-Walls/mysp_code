import json
def url_list_data():
    with open(r'爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄名称url.json',"r",encoding='utf-8')as f:
        url=json.load(f)
    data_list=[]
    for itme in url:
        name=itme["英雄名称"]
        url=itme["url"]
        data_list.append(url)
    return data_list

    
    