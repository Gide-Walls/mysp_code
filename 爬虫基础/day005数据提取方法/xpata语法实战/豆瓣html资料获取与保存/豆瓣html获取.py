import requests

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
        }
rsponse=requests.get("https://book.douban.com/chart?subcat=all&p=1&updated_at=2026-02-02",headers=headers)
with open(r"爬虫基础\day005数据提取方法\xpata语法实战\豆瓣html资料获取与保存\排行榜.html","w",encoding="utf-8")as f:
    f.write(rsponse.text)