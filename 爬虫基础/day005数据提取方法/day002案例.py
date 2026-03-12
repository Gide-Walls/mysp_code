import re
import requests
import os



# 第一步：读取 HTML 文件内容
file_path = "爬虫基础\day005数据提取方法\资料.html"  # 你的文件路径
try:
    with open(file_path, 'r', encoding="utf-8") as f:
        html_content = f.read()  # 把文件里的所有内容读成一个字符串
    
    # 第二步：写你的正则（就是我们刚才确认的那个）
    # 匹配 title 到 preview_url_o 的 mp3 链接
    pattern = r'title:"([^"]+)".*?preview_url_o:"([^"]+\.mp3)"'
    # 执行匹配（re.DOTALL 允许 .*? 匹配换行符）
    results = re.findall(pattern, html_content, re.DOTALL)
    
    # 第三步：输出结果（也可以保存到文件）
    if results:
        print(f"共匹配到 {len(results)} 条数据：")
        # 遍历结果，按序号输出
        for idx, (title, mp3_url) in enumerate(results, 1):
            mp3_url1=mp3_url.replace(r'\u002F','/')
            # response=requests.get(mp3_url1)
            # print(response.content)
            print(f"【{idx}】歌名：{title}")
            print(f"    链接：{mp3_url}")
            print("-" * 80)
            break
    else:
        print("没有匹配到任何数据，请检查正则或文件内容！")

except FileNotFoundError:
    print(f"错误：找不到文件 {file_path}，请检查文件路径是否正确！")
except Exception as e:
    print(f"程序出错：{e}")

