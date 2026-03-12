# test_pymysql.py
print("=== 使用pymysql测试MySQL连接 ===")

try:
    import pymysql
    
    print("尝试连接...")
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="test_db"  # 可选
    )
    
    print("✅ pymysql连接成功！")
    
    # 测试查询
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()[0]
    print(f"MySQL版本: {version}")
    
    cursor.close()
    conn.close()
    
except ImportError:
    print("❌ 未安装pymysql，请运行: pip install pymysql")
    print("或者运行: pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple")
    
except Exception as e:
    print(f"❌ 连接失败: {e}")