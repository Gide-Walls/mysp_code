import requests
import json
#第一种携带cookie的方法 
url="https://www.cninfo.com.cn/new/disclosure"
#不是所有的都要带cookie
haerdes={
    "cookie":"JSESSIONID=0A215BD094CB843CC5CF35A8350B67A3; cninfo_user_browse=000002,gssz0000002,%E4%B8%87%20%20%E7%A7%91%EF%BC%A1; routeId=.uc1; _sp_ses.2141=*; _sp_id.2141=913acec7-446b-4018-bb86-2f236c58a134.1770283899.2.1770340508.1770284092.1b3daad9-7fc9-492c-85f1-a07c04e7f401",
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

data = {
    'column': 'szse_main_latest',
    'pageNum': '1',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}
respones=requests.post(url,data=data,headers=haerdes)
print(respones.json())