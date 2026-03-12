import requests





def request_posts(url,headers,data):
    """请求"""
    response=requests.post(url,headers=headers,data=data)
    json_data = response.json()
    return json_data

