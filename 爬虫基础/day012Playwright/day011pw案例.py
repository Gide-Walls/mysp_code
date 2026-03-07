import sys
import os
import ssl
import urllib.request
import sqlite3
import venv

print(f"Python 版本: {sys.version}")
print(f"Python 可执行文件路径: {sys.executable}")
print(f"SSL 模块信息: {ssl.OPENSSL_VERSION}")
print("\n正在测试核心库导入...")
try:
    # 测试网络相关库（与下载包相关）
    response = urllib.request.urlopen('https://www.baidu.com', timeout=5)
    print("✓ urllib.request 模块正常，网络连接测试通过。")
except Exception as e:
    print(f"✗ 网络连接测试异常: {e}")

try:
    # 测试数据库库（许多工具依赖）
    conn = sqlite3.connect(':memory:')
    conn.close()
    print("✓ sqlite3 模块正常。")
except Exception as e:
    print(f"✗ sqlite3 模块异常: {e}")

print("核心库检查完成。")