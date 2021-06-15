import random
import requests
import fake_useragent
from decorators.test.testing import showResult


@showResult
def get_real_time_data(data: list):
    """

    从新浪财经请求当日当前时刻股票的实时信息
    :param data: 请求的股票代码
    :return:
    """

    headers = {

        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        # "User-Agent": random.choice(fake_useragent.UserAgent().data['browsers']['chrome']),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",

    }

    # respond=requests.get(url='http://hq.sinajs.cn/',data=data,headers=headers)
    respond = requests.get(url='http://hq.sinajs.cn/list=' + data.__str__()[1:-1].replace('\'', '').replace(' ', ''),
                           headers=headers)

    return respond.text

@showResult
def parse(rawData: str):
    """
    解析请求到的实时数据
    :param rawData: 请求到的数据(string)
    :return: dict
    """
    result=[]
    for line in rawData.splitlines():
        item = {'id': line[11:19], 'data': line[21:-3].split(',')}
        result.append(item)


    return result



