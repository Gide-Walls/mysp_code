from lxml import html
def lxml_get_xpaths(response):
    #元素对象
    data_hyml=html.fromstring(response.text)
    #获取的数据是列表
    result=data_hyml.xpath(r'//a[@style="float: left;font-size:18px;"]/text()')
    print(result)
    
    