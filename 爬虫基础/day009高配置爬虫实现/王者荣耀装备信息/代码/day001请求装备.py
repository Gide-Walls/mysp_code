import requests
import re
import json
url=r"https://pvp.qq.com/web201605/js/item.json"


headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://pvp.qq.com/web201605/item.shtml',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'RK=TQzaC14V2w; ptcz=5b7bdfed2613a038d5de2a03d1fa93fe7b5966f1af7376c0941128709b1bde3c; qq_domain_video_guid_verify=fe31d00c4c1581b9; _qimei_uuid42=1a213171b1010023b828d2308ea837b52adcb566da; _qimei_q36=; pgv_pvid=1768698540; _qimei_i_3=64d26a8a915f028ec594ab31098727b3f6ecf5f0405a0b86bcdb7b5f2fc1716a37353e943989e283b6ae; _qimei_q32=; _qimei_h38=bb615081b828d2308ea837b50200000961a213; _qimei_fingerprint=45f69c3cc34c8ef92d0f7f071941aec2; _qimei_i_2=64e846c6c801; _qimei_i_1=53bc6fd0c75c51dec19fff6253867bb4f5eda4f9470a0b81b3dd2d582493206c61633e9339d8e0ddd582c1c2; isHostDate=20504; PTTuserFirstTime=1771545600000; isOsSysDate=20504; PTTosSysFirstTime=1771545600000; isOsDate=20504; PTTosFirstTime=1771545600000; pgv_info=ssid=s5461997717; ts_refer=cn.bing.com/; ts_uid=1294877171; weekloop=0-0-0-8; eas_sid=v1F7Z7f19598J6h9r3X6I6y9C1; eas_entry=https%3A%2F%2Fcn.bing.com%2F; lcad_o_minduid=YmX-KbYASCMZdUrc8NypOmYrH0cbF1Mx; lcad_appuser=6DFF0368B82C5BE0; lcad_LDERturn=177; pvpqqcomrouteLine=index_index_herolist_item_item_item_item; ts_last=pvp.qq.com/web201605/item.shtml; PTTDate=1771588089386',
}

response=requests.get(url,headers=headers)
data=response.json()
print(data)
list_data=[]
for i in data:
    
    name=i["item_name"]
    price=i["price"]
    total=i["total_price"]
    des1=i["des1"]
    des2=i.get("des2","")
    
    
    des1=des1.replace('<br>','\n')
    des2=des2.replace('<br>','\n')
    des1 = re.sub(r"<[^>]+>", "", des1).strip()
    des2 = re.sub(r"<[^>]+>", "", des2).strip()
    # if des2==des1:
    #     list_data.append({"name":name,"price":price,"total":total,"des1":des1})    
    # else :
    list_data.append({"name":name,"price":price,"total":total,"des1":des1,"des2":des2})
        
    
with open(r"爬虫基础\day009高配置爬虫实现\王者荣耀装备信息\代码\保存信息\装备信息.json","w",encoding="utf-8")as f:
    json.dump(list_data,f,ensure_ascii=False,indent=4,separators=(",",":"))
    