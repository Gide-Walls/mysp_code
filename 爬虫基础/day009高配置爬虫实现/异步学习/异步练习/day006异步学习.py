import asyncio

async def add(x,semaphore):
    async with semaphore:
        await asyncio.sleep(0.5)
        return x+x

async def main():
    semaphore=asyncio.Semaphore(3)
    
    urls=[f"url{i}"for i in range(1,96)]
    
    for idx in range(0,len(urls),10):
        url_ll=[]
        for i in urls[idx:idx+10]:
            y=asyncio.create_task(add(i,semaphore))
            url_ll.append(y)
        rea=await asyncio.gather(*url_ll)
        print(rea)
if __name__ == '__main__':
    asyncio.run(main())