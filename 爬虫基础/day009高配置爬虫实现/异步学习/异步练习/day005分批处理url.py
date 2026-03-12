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
    
    # 创建信号量限制并发
    semaphore = asyncio.Semaphore(max_concurrent)
    
    # 带并发限制的爬取函数
    async def limited_crawl(url):
        async with semaphore:  # 这里控制并发！
            return await crawl(url)
    
    all_results = []
    
    print("开始分批处理...")
    print(f"总URL数: {len(urls)}")
    print(f"每批大小: {batch_size}")
    print(f"每批内最大并发: {max_concurrent}")
    print(f"需要批次: {(len(urls) + batch_size - 1) // batch_size}")
    print("=" * 50)
    
    # 核心：切片分批然后运行
    for i in range(0, len(urls), batch_size):
        # ========== 1. 切片分批 ==========
        batch = urls[i:i + batch_size]
        
        batch_num = i // batch_size + 1
        print(f"\n第{batch_num}批: 处理 {len(batch)} 个URL")
        print(f"  切片: urls[{i}:{i+batch_size}]")
        print(f"  实际URL: 第{i+1}到第{min(i+batch_size, len(urls))}个")
        
        # ========== 2. 运行这批（带并发控制） ==========
        # 为这批URL创建任务（使用limited_crawl）
        tasks = []
        for url in batch:
            task = asyncio.create_task(limited_crawl(url))  # 使用带限制的函数
            tasks.append(task)
        
        # 等待这批任务完成
        batch_results = await asyncio.gather(*tasks)
        print(batch_results)
        
        # 保存结果
        all_results.extend(batch_results)
        print(f"  本批完成，累计完成 {len(all_results)} 个")
    
    print(f"\n✅ 全部完成！共处理 {len(all_results)} 个URL")

asyncio.run(main())