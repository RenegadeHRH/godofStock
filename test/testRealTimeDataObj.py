import object.RealTimeData as RTDobj
from controller import getRealTimeData as GRT

if __name__ == '__main__':
    print(len(GRT.parse(GRT.get_real_time_data(['sz002307']))[0]['data']))
    print(GRT.parse(GRT.get_real_time_data(['sz002307']))[0]['data'][26])
    rtd=RTDobj.RealTimeData(data=GRT.parse(GRT.get_real_time_data(['sz002307']))[0])
    print(rtd.Data())

    rtd.parseForDataBase()