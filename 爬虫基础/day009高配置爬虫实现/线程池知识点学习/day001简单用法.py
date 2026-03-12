
from concurrent.futures import ThreadPoolExecutor
import time
def task(name):
    print(f"{name}开始")
    time.sleep(1)
    return f"{name}完成"

with ThreadPoolExecutor(max_workers=3)as executor:
    funtures=[executor.submit(task,f"{i}")for i in range(5)]
    for future in funtures:
        print(future.result())