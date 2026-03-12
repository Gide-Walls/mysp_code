import asyncio
import random

# 创建一个异步队列
queue = asyncio.Queue()

async def producer(producer_id):
    # 限制每个生产者只生产 5 个数据，防止无限生产
    for _ in range(5):
        await asyncio.sleep(random.uniform(0.1, 0.5)) 
        item = f"产品-{producer_id}-{_}"
        await queue.put(item)
        print(f"[生产者{producer_id}] 生产了: {item}")
    print(f"[生产者{producer_id}] 完成工作，退出")

async def consumer():
    while True:
        item = await queue.get()
        await asyncio.sleep(random.uniform(0.2, 0.6)) # 模拟处理耗时
        print(f"          [消费者] 消费了: {item}")
        queue.task_done() # 标记任务完成（这一步很重要，否则 join() 永远不会结束）

async def main():
    tasks = []
    # 启动 3 个生产者
    for i in range(3):
        task = asyncio.create_task(producer(i))
        tasks.append(task)
    
    # 启动 1 个消费者
    consumer_task = asyncio.create_task(consumer())
    
    # 等待所有生产者结束
    await asyncio.gather(*tasks)
    
    # 生产者结束了，现在等待队列里的剩余数据被消费完
    await queue.join() 
    
    # 取消消费者任务（因为消费者是死循环，必须手动取消）
    consumer_task.cancel()
    print("所有任务完成，程序结束")

if __name__ == "__main__":
    asyncio.run(main())