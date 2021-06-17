
import mysql.connector as mysql
from data.DBConnector import connDefault
from data.DBConnector import SQLexecutor
@connDefault
def getDataFromDataBase(mydb:mysql.MySQLConnection,stockid):

    if stockid[2] != '.':
        stockid = stockid[0:2] + '.' + stockid[2:]
    sql="select s_show from %s where s_code='%s'"%('stock_data',stockid)

    mycur=mydb.cursor()
    mycur.execute(sql)
    result=[]

    for i in mycur:
        result.append(int(i[0]))
    return result
@connDefault
def fetchStockList(mydb:mysql.MySQLConnection):
    pass
if __name__ == '__main__':
    data=getDataFromDataBase('sz.002273')
