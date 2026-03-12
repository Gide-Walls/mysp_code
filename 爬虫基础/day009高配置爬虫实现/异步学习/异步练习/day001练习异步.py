import asyncio
from datetime import datetime 
import time
async def add(x):
    print(x)
    await asyncio.sleep(1)
    return x*x


async def main():
    t1=datetime.now()
    task=[]
    
    for i in range(1,10):
        tasks=asyncio.create_task(add(i))
        task.append(tasks)
    await asyncio.gather(*task)
    print(t1)
    print(datetime.now())
    
if __name__ == '__main__':
    asyncio.run(main())