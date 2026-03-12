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
        
        # 创建下载目录
        download_dir = "音乐下载"
        os.makedirs(download_dir, exist_ok=True)
        print(f"✅ 下载目录已创建: {os.path.abspath(download_dir)}")
        
        # 遍历结果，按序号输出并下载
        for idx, (title, mp3_url) in enumerate(results, 1):
            print(f"\n{'='*60}")
            print(f"正在处理第 {idx} 个音频:")
            print(f"【{idx}】歌名：{title}")
            print(f"    原始链接：{mp3_url}")
            
            # ✅ 修复1：完整的 URL 解码（处理大小写）
            mp3_url1 = mp3_url.replace('\\u002f', '/').replace('\\u002F', '/')
            print(f"    修复后链接：{mp3_url1}")
            
            # ✅ 修复2：清理文件名（移除非法字符）
            clean_title = re.sub(r'[\\/*?:"<>|]', '_', title)  # 移除 Windows 非法字符
            clean_title = re.sub(r'\s+', ' ', clean_title).strip()  # 清理多余空格
            if len(clean_title) > 50:
                clean_title = clean_title[:50]  # 限制文件名长度
            
            filename = f"{clean_title}.mp3"
            file_path_save = os.path.join(download_dir, filename)  # ✅ 修复3：正确拼接路径
            
            print(f"    保存文件名：{filename}")
            print(f"    保存路径：{file_path_save}")
            
            try:
                # 设置请求头（有些服务器需要）
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                    'Referer': 'https://houzi8.com/',
                }
                
                print("    🔄 开始下载音频...")
                response = requests.get(mp3_url1, headers=headers, timeout=30)
                
                if response.status_code == 200:
                    # ✅ 写入文件
                    with open(file_path_save, "wb") as music_file:
                        music_file.write(response.content)
                    
                    # 验证文件是否写入成功
                    if os.path.exists(file_path_save):
                        file_size = os.path.getsize(file_path_save)
                        print(f"    ✅ 下载并写入成功！")
                        print(f"    📊 文件大小: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
                        
                        if file_size == 0:
                            print(f"    ⚠️  警告：文件大小为0，可能下载失败")
                            os.remove(file_path_save)  # 删除空文件
                        elif file_size < 10000:  # 小于10KB可能是错误页面
                            print(f"    ⚠️  警告：文件过小，可能不是有效音频")
                    else:
                        print(f"    ❌ 文件写入失败：文件未创建")
                        
                else:
                    print(f"    ❌ 下载失败：HTTP {response.status_code}")
                    print(f"    📄 响应内容预览：{response.text[:200]}...")  # 显示前200字符
                    
            except requests.exceptions.RequestException as e:
                print(f"    ❌ 网络请求异常：{e}")
            except IOError as e:
                print(f"    ❌ 文件写入异常：{e}")
            except Exception as e:
                print(f"    ❌ 其他异常：{type(e).__name__}: {e}")
            
            print("-" * 60)
            
            # 可选：只下载第一个文件进行测试（去掉 break 可以下载所有）
            # break  # 如果想要下载所有文件，注释掉这行
            
    else:
        print("没有匹配到任何数据，请检查正则或文件内容！")
        print("💡 建议：检查一下 HTML 文件中是否真的包含 'title:' 和 'preview_url_o:' 这样的字段")

except FileNotFoundError:
    print(f"错误：找不到文件 {file_path}，请检查文件路径是否正确！")
    print("💡 当前工作目录：", os.getcwd())
except UnicodeDecodeError:
    print(f"错误：文件编码问题，尝试使用其他编码方式读取")
    # 可以尝试其他编码
    try:
        with open(file_path, 'r', encoding="gbk") as f:
            html_content = f.read()
        print("✅ 使用 GBK 编码成功读取文件")
    except:
        print("❌ 无法读取文件，请检查文件编码")
except Exception as e:
    print(f"程序出错：{type(e).__name__}: {e}")

print(f"\n🎯 程序执行完毕！")
print(f"📁 请检查 '{download_dir}' 文件夹查看下载的音频文件")