from pandas import DataFrame
import baostock as bs
import datetime
class baoStockDailyData:
    def __init__(self,code:str):
        if code[2] != '.':
            code = code[0:2] + '.' + code[2:]
        self.code=code
        self.fetchData()

    def fetchData(self,delta=1):

        bs.login()

        rs = bs.query_history_k_data_plus(self.code,
                                          "date,time,code,open,high,low,close,volume,amount,adjustflag",
                                          start_date=str(datetime.date.today() - datetime.timedelta(days=delta)),
                                          frequency="5", adjustflag="3")

        data_list=[]

        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())

        self.data=data_list
        # self.data=DataFrame(data_list, columns=rs.fields,index=['']*len(data_list))


        bs.logout()
