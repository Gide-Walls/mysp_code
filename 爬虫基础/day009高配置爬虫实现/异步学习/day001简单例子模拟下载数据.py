import asyncio

semaphore=asyncio.Semaphore(3)
async def fetch_data(name,delay=1):
    async with semaphore:
        print(f"开始获取{name}")
        
        await asyncio.sleep(delay)
        print(f"数据{name}获取完成")
        
        return f"数据的结果{name}"

async def main():
    print("程序开始")
    data=[f"数据{i}"for i in range(100)]
    
    result=await asyncio.gather(*(fetch_data(x)for x in data))
    print("数据获取完毕",result)
    print("程序结束")
if __name__ == '__main__':
    asyncio.run(main())