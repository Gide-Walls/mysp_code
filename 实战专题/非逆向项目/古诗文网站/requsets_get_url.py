import requests


def requsets_get(url):
    # url=r"https://www.gushiwen.cn/mingjus/default.aspx?page=1&tstr=&astr=&cstr=&xstr="


    headers={
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

    response=requests.get(url=url,headers=headers)
    return response

    
    