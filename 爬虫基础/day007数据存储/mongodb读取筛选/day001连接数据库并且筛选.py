from pymongo import MongoClient

# with 语句会自动管理连接，代码结束后自动关闭
with MongoClient("mongodb://localhost:27017/") as client:
    db = client["my_database"]
    collection = db["my_collection"]
    write_col = db["new_collection"]
    
    # 打印所有数据
    for item in collection.find():
        a=item["content"]["datas"]
         
        for items in a:
            data_dict={}
            data_dict["name"] = ','.join(items["name"]) if isinstance(items["name"], list) else items["name"]
            data_dict["categories"] = ','.join(items["categories"]) if isinstance(items["categories"], list) else items["categories"]
            data_dict["workLocations"] = ','.join(items["workLocations"]) if isinstance(items["workLocations"], list) else items["workLocations"]
            data_dict["requirement"]=items["requirement"]
            data_dict["description"]=items["description"]
            write_col.insert_one(data_dict)
        

            
            
            
            
            

# 出了 with 块，连接已经自动关闭，不用额外操作
print("数据库连接已自动关闭")