import requests

def request_dir():
    url="https://www.xslca.cc/girl/674393.html"


    headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
            "referer":"https://cn.bing.com/"
        }
    #自动处理cookie
    session=requests.Session()

    response=session.get(url,headers=headers)
    return response.text



