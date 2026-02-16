from lxml import html
import requests

def requests_get_2(url_2):
    
    
    headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
            "referer":"https://cn.bing.com/"
        }
    response=requests.get(url_2,headers)
    
    tree=html.fromstring(response.text)
    result=tree.xpath(r'//div[@id="content"]/text()')
    full_text=''.join(result)
    return full_text
    
    
    
    
    


