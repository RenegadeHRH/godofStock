class RealTimeData:
    """
    单个股票得实时数据
    包含以下字段:
    stockID:股票ID
    stockName:股票名称
    SPIEMT(Stock prices in early morning trading):股票开盘价格
    SCP(stock closing price):股票收盘价格
    CP(Current Prince):股票当前价格
    HP(Highest Price):最高价格
    LP(Lowest Price):最低价格
    BP(bid price):竞买价格(和买1报价一致)
    SPC(The selling price competition):竞卖价格(和卖1一致)
    DealNum:成交股票数(单位:股)
    DealVal:成交金额(单位:元)
    BidInCount1~6:买1~6申请数量
    BP1~6:买1~6报价
    SaleCount1~4:卖1~6申请数量
    SP1~4:卖1~4报价
    Date:获取日期
    Time:获取时间
    """

    def __init__(self):

        self.stockID = ''
        self.stockName = ''
        self.SPIEMT = ''
        self.SCP = ''
        self.CP = ''
        self.HP = ''
        self.LP = ''
        self.BP = ''
        self.SPC = ''
        self.DealNum = ''
        self.DealVal = ''
        self.BidInCount = []
        self.BP = []
        self.SaleCount = []
        self.SP = []
        self.Date = ''
        self.Time = ''
        self.ini = 0

    def __int__(self, data: dict):
        """
        初始化
        :param data: getRealTimeData获取到数据后经过parse在传入
        :return: self
        """
        self.ini = 1
        self.stockID = data['id']
        self.stockName, self.SPIEMT, self.SCP, self.CP, self.HP, self.LP, self.BP, self.SPC, self.DealNum, self.DealVal = \
            data['data'][0:10]
        # 前半部分数据
        j = 0
        # 买1~买6的数据
        for i in range(6):
            self.BidInCount[j] = data['data'][10 + i + j * 2 + 1]  # 前半部分数据10,'买'有6对数据,former是买入数量,after是买入价格
            self.BP[j] = data['data'][10 + i + j * 2 + 2]  # after,offset+1
            j += 1
        j = 0
        for i in range(4):
            self.SaleCount[j] = data[10 + 12 + i + j * 2+1]
            self.SP[j]=data[10+12+i+j*2+2]
            j += 1
        self.Date,self.Time=data['data'][10+12+8+1:]
        return self
    def showTitle(self):
        print("%-8s %-20s %-12s %-12s %-8s %-8s %-8s %-8s %-8s %-8s %-16s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s"%
              ('股票ID','股票名称','股票开盘价格','股票收盘价格','股票当前价格','最高价格','最低价格','最高竞买价格','最低竞卖价格','成交股票数(单位:股)','成交金额(单位:元)',
              '买1数量','买1报价','买2数量','买2报价','买3数量','买3报价','买4数量','买4报价','买5数量','买5报价','买6数量','买6报价',
              '卖1数量','卖1报价','卖2数量','卖2报价','卖3数量','卖3报价','卖4数量','卖4报价',
              '获取日期','获取时间'))
