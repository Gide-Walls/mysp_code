import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
MONGO_URL="mongodb://localhost:27017"
DATABASE_NAME="mgtv_db"
COLLECTION_NAME = "video_data"
client:Optional[AsyncIOMotorClient]=None
db=None
collection = None
async def init_db():
    global client,db,collection
    client=AsyncIOMotorClient(
        MONGO_URL,
        maxPoolSize=10,
        minPoolsize=1,
        serverSelectionTimeoutMS=5000 
    )
    db=client[DATABASE_NAME]
    collection=db[COLLECTION_NAME]
async def close_db():
    global client
    if client:
        client.close()
        print("数据库已关闭")
async def print_all_data():
    cursor=collection.find({})
    
    semaphore=asyncio.Semaphore(3)
    while True:
        bacth=await cursor.to_list(length=100)
        
        if not bacth:
            print("数据读取完毕")
            break
        async def worker(doc):
            async with semaphore:
                print(f"{doc}")
        tasks=[]
        for document in bacth:
            task=asyncio.create_task(worker(document))
            tasks.append(task)
    
async def main():
    await init_db()
    await print_all_data()
    await close_db()
if __name__ == '__main__':
    asyncio.run(main())