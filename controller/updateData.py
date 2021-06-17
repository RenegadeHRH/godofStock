from object.RealTimeData import RealTimeData
from controller import getRealTimeData as grt
from data.dumpToDailyData import dumpToDatabase

def update(stockList):
    stockObjList=[]
    for i in range(len(stockList)):
        stockObjList.append(RealTimeData(data=grt.parse(grt.get_real_time_data(stockList))[i]))
    dumpToDatabase(stockObjList)
