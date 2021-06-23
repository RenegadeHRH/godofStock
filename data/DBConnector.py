import json
import sys

import mysql.connector as mysql


def returnDBconnInfo():
    with open(sys.path[1].replace('\\', '/') + '/data/mysql.json', 'r') as f:
        data = json.load(f)
        host = data["host"]
        user = data["user"]
        passwd = data["password"]
        database = data["database"]
    return data


def connector():
    loginfo = returnDBconnInfo()

    mydb = mysql.connect(
        host=loginfo["host"],  # 数据库主机地址
        user=loginfo["user"],  # 数据库用户名
        passwd=loginfo["password"],  # 数据库密码
        database=loginfo["database"]
    )

    return mydb


def SQLexecutor(sql: str):
    mydb = connector()
    mycur = mydb.cursor()
    mycur.execute(sql)
    mycur.close()
    mydb.close()


def connDefault(func, *args,**kwargs):
    """
    作为装饰器使用,让函数自动连接,加了这个装饰器后,函数形参要有mysql.connect()返回的对象(mydb)
    :param func: 需要连接数据库的函数,处理好数据之后返回,func传入的第一个数据必须是mysql.connect()返回的对象
    :param args: 传入func的参数,其实就是一个list
    :return: 由func决定
    """


    def wrapper(*args,**kwargs):
        mydatabase = connector()
        # print('数据库连接')
        #
        # print('数据库连接状态:%s'%str(mydatabase.is_connected()))
        result=func(mydatabase,*args,**kwargs)
        try:
            mydatabase.close()
            # print('数据库连接关闭')
        except Exception as e :
            print(mydatabase.connect())
            print('数据库关闭失败')
        return result
    #哪怕把代码写在这里,它也是比wrapper先执行

    return wrapper
