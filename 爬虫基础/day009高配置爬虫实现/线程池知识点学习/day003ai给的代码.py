from concurrent.futures import ThreadPoolExecutor
# 从文件读取
with open("urls.txt") as f, \
     ThreadPoolExecutor(max_workers=5) as executor:
    
    for result in executor.map(download, f):  # 文件对象直接当迭代器用
        print(result)

# 从数据库读取（分批）
cursor.execute("SELECT url FROM table")
while True:
    batch = cursor.fetchmany(1000)  # 一批1000条
    if not batch:
        break
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(process, batch))
        save(results)