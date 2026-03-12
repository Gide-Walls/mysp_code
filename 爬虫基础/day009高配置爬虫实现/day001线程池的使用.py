from concurrent.futures import ThreadPoolExecutor

def crawl(url):
    print(url)
    
if __name__ == '__main__':
    base_url="http{}"
    with ThreadPoolExecutor(10)as f:
        for i in range(1,15):
            f.submit(crawl,url=base_url.format(i))