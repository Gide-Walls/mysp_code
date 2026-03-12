
def url_headers_data(i):
    """需要传入i也就是分页"""
    url=r"http://www.ccgp-hunan.gov.cn/mvc/getContentList.do"

    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

    data = {
        'column_code': '2',
        'title': '',
        'pub_time1': '',
        'pub_time2': '',
        'own_org': '1',
        'page': f'{i}',
        'pageSize': '18',
    }
    return[r"http://www.ccgp-hunan.gov.cn/mvc/getContentList.do",headers,data]