import data.dumpToDailyData as dmp
import object.RealTimeData as RTDobj
from controller import getRealTimeData as GRT
if __name__ == '__main__':
    # rtd = RTDobj.RealTimeData(data=GRT.parse(GRT.get_real_time_data(['sz002307']))[0])
    # print(type(rtd))
    # dmp.dumpToDatabase([rtd])
    print(dmp.getStockList())