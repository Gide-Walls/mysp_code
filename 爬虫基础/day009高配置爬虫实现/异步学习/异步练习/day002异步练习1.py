import asyncio

semaphore = asyncio.Semaphore(100) 
async def add(x):
    async with semaphore:
        # await asyncio.sleep(1)
        print(x)
        return x+x

async def main():
    tasks=[]
    
    for i in range(1,1000):
        task=asyncio.create_task(add(i))
        tasks.append(task)
    result=await asyncio.gather(*tasks)
    print(result)
    
if __name__ == '__main__':
    asyncio.run(main())