from pymongo import MongoClient
import pymysql
class select(object):
    '''类'''
    def __init__(self):
        #连接mongodb
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db=self.client["mgtv_db"]["video_data"]
        #连接mysql
        self.conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="test_db"  # 可选
    )
        #创建游标
        self.cursor = self.conn.cursor()
        #语句
        self.sql="INSERT INTO data_info(电影,演员,年份,简介,类型)VALUES(%s,%s,%s,%s,%s)"     
    def read(self):
        '''读取'''
        mongodb_data=self.db.find()
        list_data=[]
        for i in mongodb_data:
            
            list_data.append((i["title"],i["subtitle"],int(i["year"]),i["story"],i["kind"]))
        print(list_data)
        self.cursor.executemany(self.sql,list_data)
        self.conn.commit()
    def colse(self):
        '''关闭数据库'''
        self.client.close()
        self.conn.close()
        self.cursor.close()    
if __name__ == '__main__':
    aaa=select()
    aaa.read()
    aaa.colse() 