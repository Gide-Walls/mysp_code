import asyncio

# 模拟爬取函数
async def crawl(url):
    await asyncio.sleep(0.1)  # 模拟网络请求
    return f"结果: {url}"

async def main():
    # 1000个URL
    urls = [f"https://example.com/page{i}" for i in range(1, 1001)]
    
    # 每批处理100个，但每批内限制并发为20个
    batch_size = 100
    max_concurrent = 20  # 新增：每批内最大并发数
    semaphore = asyncio.Semaphore(max_concurrent)
    async def limited_crawl(url):
        async with semaphore:  # 这里控制并发！
            return await crawl(url)
    
    all_results = []
    for i in range(0, len(urls), batch_size):
        # ========== 1. 切片分批 ==========
        batch = urls[i:i + batch_size]

        tasks = []
        for url in batch:
            task = asyncio.create_task(limited_crawl(url))  # 使用带限制的函数
            tasks.append(task)
        
        # 等待这批任务完成
        batch_results = await asyncio.gather(*tasks)
        
        # 保存结果
        all_results.extend(batch_results)
        print(f"  本批完成，累计完成 {len(all_results)} 个")
    
    print(f"\n✅ 全部完成！共处理 {len(all_results)} 个URL")

asyncio.run(main())