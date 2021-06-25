import matplotlib.pyplot as plt
import mysql.connector as mysql
from data.DBConnector import connDefault
from data.DBConnector import SQLexecutor
import datetime


def legitimateId(stockid: str):

    if stockid[2] != '.':
        stockid = stockid[0:2] + '.' + stockid[2:]

    return stockid


@connDefault
def getDataFromDataBase(mydb: mysql.MySQLConnection, stockid, date=datetime.date.today()):
    """

    :param mydb:
    :param stockid:
    :param date: 格式:yy-mm-dd
    :return:
    """
    stockid = legitimateId(stockid)
    if date == datetime.date.today():
        date -= datetime.timedelta(days=1)

    sql = "select s_time,s_show from %s where s_code='%s' and s_date='%s'" % ('stock_data', stockid, str(date))
    mycur = mydb.cursor()
    mycur.execute(sql)
    result = dict()

    for i in mycur:
        result[str(i[0])] = float(i[1])
    return result


@connDefault
def fetchStockList(mydb: mysql.MySQLConnection):
    mycur = mydb.cursor()
    sql = "select stock_id,stock_name from stock"
    mycur.execute(sql)
    result = dict()
    for i in mycur:
        id = legitimateId(str(i[0]))
        result[id] = i[1]

    return result


def seperateTime(dt: str):
    dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    dt = dt.strftime('%H:%M:%S')
    return dt


def drawOne(data: dict, stockName: str):
    plt.rcParams["font.family"] = "SimHei"
    plt.figure(figsize=(15, 15))
    plt.title(stockName + '日数据')
    plt.xlabel("Time")
    plt.ylabel("今日净值变化")

    time = []
    val = []
    for k, v in data.items():
        time.append(seperateTime(k))
        val.append(float(v))
    plt.xticks(range(0, 48), time, rotation=90)
    plt.plot(time, val)
    plt.savefig("anl.png")
    plt.show()


def drawMulti(stockDict: dict,choice=[],date=datetime.date.today()):
    """
    画出给定日期的多只股票的折现图
    :param stockDict: {'name':'stockID',}
    :return:
    """
    stockIDs = []
    stockNames = []
    plt.rcParams["font.family"] = "SimHei"
    plt.figure(figsize=(15, 15))
    plt.title('%s当日数据对比'%str(date))
    plt.xlabel("Time")
    plt.ylabel("今日净值变化")

    for k, v in stockDict.items():
        stockIDs.append(k)
        stockNames.append(v)
    if len(choice) !=0:
        chosenIDs=[]
        chosenNames=[]
        for i in choice:
            chosenIDs.append(stockIDs[i])
            chosenNames.append(stockNames[i])
        stockIDs=chosenIDs
        stockNames=chosenNames
    drawx=0
    i=0
    for s in stockIDs:
        time=[]
        val=[]
        result = getDataFromDataBase(s, date=date)

        for k,v in result.items():
            time.append(seperateTime(k))
            val.append(float(v))

        if drawx==0:
            plt.xticks(range(0, 48), time, rotation=90)
        plt.plot(time, val,label=stockNames[i])
        i+=1
    plt.legend()
    plt.show()




if __name__ == '__main__':
    # data=getDataFromDataBase('sz.002273')

    # drawOne(getDataFromDataBase('sz.002273',date=datetime.date.today()- datetime.timedelta(days=1)), '水晶光电')
    drawMulti(fetchStockList(),date=datetime.date.today()- datetime.timedelta(days=2),choice=[3,2,5])
