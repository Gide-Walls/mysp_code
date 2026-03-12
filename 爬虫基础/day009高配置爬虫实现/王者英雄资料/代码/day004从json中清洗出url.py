import json

with open(r"爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄.json","r",encoding='utf-8')as f:
    data=json.load(f)

result=[]

for i in data['yxlb20_2489']:
    print(i)
    if 'fllb_2105' in i and 'yxpymc_4614'in i:
        url=f"https://pvp.qq.com/web201605/herodetail/{i['yxpymc_4614']}.shtml"
        result.append({
            '英雄名称':i["yxmclb_9965"],
            '英雄拼音':i["yxpymc_4614"],
            'url':url
        })
with open(r'爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄名称url.json','w',encoding='utf-8')as f:
    json.dump(result,f,ensure_ascii=False,indent=4,separators=(',',':'))
print('文件写入完成')