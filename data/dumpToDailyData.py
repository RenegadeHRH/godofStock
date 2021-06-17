import sys

from object.RealTimeData import RealTimeData
from controller.getRealTimeData import *
import mysql.connector as mysql
import json


def getStockList():
    stockList = []
    with open(sys.path[1].replace('\\','/')+'/data/mysql.json','r') as f:
        data=json.load(f)
        host=data["host"]
        user=data["user"]
        passwd=data["password"]
        database=data["database"]
    mydb = mysql.connect(
        host=host,  # 数据库主机地址
        user=user,  # 数据库用户名
        passwd=passwd,  # 数据库密码
        database=database
    )
    mycur = mydb.cursor()
    sql="select stock_id from stock"
    mycur.execute(sql)
    for i in mycur:
        stockList.append(str(i).replace("'",'').replace(",",'').replace('(','').replace(')',''))
    mycur.close()
    return stockList
def dumpToDatabase(RealTimeDataList:list):

    with open(sys.path[1].replace('\\','/')+'/data/mysql.json','r') as f:
        data=json.load(f)
        host=data["host"]
        user=data["user"]
        passwd=data["password"]
        database=data["database"]
    mydb = mysql.connect(
        host=host,  # 数据库主机地址
        user=user,  # 数据库用户名
        passwd=passwd,  # 数据库密码
        database=database
    )
    mycur=mydb.cursor()

    for i in RealTimeDataList:
        sql = "insert into stock_details values "+"(null,"+str(tuple(i.parseForDataBase()))[1:]
        print(sql)
        mycur.execute(sql)
        mydb.commit()
    mydb.disconnect()