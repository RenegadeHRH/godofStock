import json
import sys
from datetime import datetime

import mysql.connector as mysql

from object.baoStockdailyData import baoStockDailyData


def getStockList():
    stockList = []
    with open(sys.path[1].replace('\\', '/') + '/data/mysql.json', 'r') as f:
        data = json.load(f)
        host = data["host"]
        user = data["user"]
        passwd = data["password"]
        database = data["database"]
    mydb = mysql.connect(
        host=host,  # 数据库主机地址
        user=user,  # 数据库用户名
        passwd=passwd,  # 数据库密码
        database=database
    )
    mycur = mydb.cursor()
    sql = "select stock_id from stock"
    mycur.execute(sql)
    for i in mycur:
        stockList.append(str(i).replace("'", '').replace(",", '').replace('(', '').replace(')', ''))
    mycur.close()
    mydb.close()
    return stockList


def getObjList():
    stockList = getStockList()

    objList = []
    for i in stockList:
        objList.append(baoStockDailyData(i))

    return objList


def dumpToDataBase():
    with open(sys.path[1].replace('\\', '/') + '/data/mysql.json', 'r') as f:
        data = json.load(f)
        host = data["host"]
        user = data["user"]
        passwd = data["password"]
        database = data["database"]
    mydb = mysql.connect(
        host=host,  # 数据库主机地址
        user=user,  # 数据库用户名
        passwd=passwd,  # 数据库密码
        database=database
    )
    mycur = mydb.cursor()
    # conn = create_engine('mysql+pymysql://'+user+':'+passwd+'@'+host+'/'+database, encoding='utf8')
    objList = getObjList()

    for i in objList:
        s_open = i.data[0][3]
        for d in i.data:
            d[1] = datetime.strptime(d[1], "%Y%m%d%H%M%S000")
            d[1] = d[1].strftime('%Y-%m-%d-%H:%M:%S')

            # sql = 'insert into stock_data values (' + 'null,' + "'" + str(d[0]) + "','" + str(d[1])+"','"+str(d[2])+ "'," + str(d[3]).replace("'", '') + ',' + str(d[4]).replace("'", '') + ',' + str(d[5]).replace(
            #     "'", '') + ',' + str(d[6]).replace("'", '') + ',' + str(d[7]).replace("'", '') + ',' + str(
            #     d[8]).replace("'", '') + ',' + str(d[9]).replace("'", '') + ')'
            sql = "insert into stock_data values (null,'%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f)" % (
            str(d[0]), str(d[1]), str(d[2]), float(d[3]), float(d[4]), float(d[5]), float(d[6]), float(d[7]), float(d[8]),
            float(d[3]), float((float(d[4]) + float(d[5])) /2/float(s_open)))
            # print(sql)
            mycur.execute(sql)
    mydb.commit()
    mycur.close()
    mydb.close()

    # pd.io.sql.to_sql(i.data, "stock_data", conn, if_exists='replace')
