def showResult(func):
    def f(*args):
        result=func(*args)
        print('-----------------以下为测试输出------------------')
        print("函数名   "+func.__name__+'()')
        print('结果输出:')
        print(result)
        print("结果类型:"+str(type(result)))
        print('-----------------------------------------------')
        return result
    return f