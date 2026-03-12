import asyncio
import time
import random


class Spider:
    def __init__(self):
        # 模拟URL
        self.url = '模拟主页'
        self.semaphore = asyncio.Semaphore(2)  # 信号量，控制并发数为2
        self.q = asyncio.Queue()

    async def init_session(self):
        """初始化会话（模拟）"""
        print(f"[{time.time():.2f}] 初始化会话完成")
        return

    # 主页请求
    async def requests_get(self):
        """模拟发送主页请求"""
        print(f"[{time.time():.2f}] 请求主页: {self.url}")
        # await asyncio.sleep(1)  # 模拟网络延迟
        return "模拟主页HTML内容"

    # 第二层 链接发送请求
    async def requests_province(self, url):
        """模拟省份页面请求"""
        print(f"[{time.time():.2f}] 请求省份: {url}")
        # await asyncio.sleep(0.5)  # 模拟网络延迟
        return f"模拟省份{url}的HTML内容"

    # 第三次请求 结果并筛选打印
    async def train(self, url):
        """模拟列车数据处理，改为加法计算"""
        async with self.semaphore:  # 信号量控制并发
            for i in range(3):  # 重试3次
                try:
                    # 模拟网络请求
                    await asyncio.sleep(0.2)  # 模拟网络延迟

                    # 改为加法计算：从URL中提取数字进行计算
                    # 例如：url是"车站_5"，则提取5进行计算
                    if '_' in url:
                        num = int(url.split('_')[1])
                    else:
                        num = random.randint(1, 10)

                    # 进行加法计算
                    result = 0
                    for j in range(num * 1000):  # 模拟一些计算量
                        result += j
                        if j % 2 == 0:
                            result -= j // 2

                    car_data = {
                        "原始URL": url,
                        "提取的数字": num,
                        "计算结果": result,
                        "计算时间": time.time()
                    }

                    print(f"[{time.time():.2f}] 立即打印计算结果: {car_data}")

                except Exception as e:
                    print(f"[{time.time():.2f}] 出现异常正在重试: {e}")

                # await asyncio.sleep(0.5)  # 重试间隔
            return None

    # 第二层各个火车站解析出url 进行请求(用train)并打印出来
    async def tow_analysis(self, data):
        """模拟解析省份页面，改为生成数字"""
        print(f"\n{'=' * 60}")
        print(f"[{time.time():.2f}] 开始解析省份数据")
        print(f"{'=' * 60}")

        # 模拟解析出多个"车站"，用数字表示
        # 假设每个字母分类有不同数量的车站
        station_list = []

        # 模拟3个字母分类，每个有不同数量的"车站"
        for letter in ['A', 'B', 'C']:
            # 每个字母有随机数量的车站
            station_count = random.randint(3, 6)
            station_dict_list = []

            for j in range(station_count):
                # 生成模拟URL，如"车站_A_1", "车站_A_2"
                href_data = f"车站_{letter}_{j + 1}"
                station_dict_list.append({
                    'href': href_data,
                })

            station_list.append({letter: station_dict_list})
            stations = station_dict_list
            batch_size = 2

            print(f"\n[处理字母 {letter}] 有 {len(stations)} 个计算任务")

            # async with self.semaphore:
            for i in range(0, len(stations), batch_size):
                # async with self.semaphore:
                batch_stations = stations[i:i + batch_size]
                tasks = []

                print(f"\n[字母{letter}批次{i // batch_size + 1}] 等待10秒...")
                await asyncio.sleep(1)  # 批次前等待10秒
                print(f"[{time.time():.2f}] 等待结束，开始当前批次计算")

                for station in batch_stations:
                    task = asyncio.create_task(self.train(station['href']))
                    tasks.append(task)

                results = await asyncio.gather(*tasks)
                print(f"[{time.time():.2f}] 当前批次计算完成")

    async def analysis(self, res):
        """模拟解析主页，改为生成省份"""
        print(f"\n{'=' * 60}")
        print(f"[{time.time():.2f}] 开始解析主页数据")
        print(f"{'=' * 60}")

        # 模拟解析出多个省份
        dict_data = []

        # 模拟3个地区，每个地区有2个省份
        for region_idx in range(1, 4):
            region_name = f"地区{region_idx}"
            dict_pro = []

            for province_idx in range(1, 3):
                province_name = f"省份{region_idx}_{province_idx}"
                link_url = f"省份链接_{province_name}"
                dict_pro.append({'省份': province_name, '链接': link_url})

                print(f"\n处理省份: {province_name}")
                res_province = await self.requests_province(link_url)

                if res_province:
                    await self.tow_analysis(res_province)  # 解析各个省份
                else:
                    print("省份数据处理失败")

            dict_data.append({region_name: dict_pro})

        return dict_data

    async def main(self):
        """主函数"""
        print("=" * 60)
        print("开始异步加法计算演示")
        print(f"[{time.time():.2f}] 程序开始")
        print("=" * 60)

        await self.init_session()
        res = await self.requests_get()  # 获取主页数据

        if res is not None:
            result = await self.analysis(res)
            print(f"\n[最终结果数据结构]: {result}")
        else:
            print("主页数据获取失败")

        print(f"\n[{time.time():.2f}] 程序结束")


if __name__ == "__main__":
    print("注意：每个批次前会等待10秒，信号量控制最多2个计算同时进行")
    print("您将看到明显的批次间隔和并发控制效果")
    print("-" * 60)

    spider = Spider()
    asyncio.run(spider.main())