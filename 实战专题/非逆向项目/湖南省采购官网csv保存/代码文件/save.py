import csv

#保存数据
def write_csv_header():
    '''单独写表头'''
    with open(r'爬虫基础\day007数据存储\湖南省采购官网csv保存\数据保存\数据.csv',"w",newline="",encoding='utf-8')as f:
        writer=csv.writer(f)
        writer.writerow(["RN","AREA_NAME","TITLE","STAFF_DATE"])

def write_csv_data(row_data):
    with open(r'爬虫基础\day007数据存储\湖南省采购官网csv保存\数据保存\数据.csv',"a",newline='',encoding='utf-8-sig')as f:
        writer=csv.writer(f)
        writer.writerow(row_data)