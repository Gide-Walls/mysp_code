from pymongo import MongoClient
import datetime

# 1. 连接到 MongoDB
def connect_mongodb():
    """
    连接到 MongoDB 数据库
    """
    try:
        # 方式1：连接到本地默认端口
        client = MongoClient('mongodb://localhost:27017/')
        # 或 MongoClient('localhost', 27017)
        
        # 方式2：带认证的连接
        # client = MongoClient('mongodb://用户名:密码@localhost:27017/数据库名')
        
        # 方式3：连接远程 MongoDB
        # client = MongoClient('mongodb://服务器IP:27017/')
        
        print("✅ MongoDB 连接成功!")
        return client
        
    except Exception as e:
        print(f"❌ 连接失败: {e}")
        return None

# 2. 测试连接
if __name__ == "__main__":
    client = connect_mongodb()
    if client:
        # 查看所有数据库
        print("数据库列表:", client.list_database_names())
        client.close()