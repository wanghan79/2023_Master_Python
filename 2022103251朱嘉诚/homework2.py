import random
import string
from functools import wraps

# 随机数据生成函数
def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, tuple) and len(value) == 2:
            dataType = value[0]
            dataNumber = value[1]
            if dataType == int:
                result[key] = random.sample(range(1, 101), dataNumber)
            elif dataType == float:
                result[key] = [round(random.uniform(1.0, 100.0),2) for i in range(dataNumber)]
            elif dataType == str:
                result[key] = [''.join(random.sample(string.ascii_letters + string.digits, 8)) for i in range(dataNumber)]
    return result

# SVM修饰器
def SVM_decorator(*args):
    def wrapper(func):
        @wraps(func)    #使用修饰器后，原函数不是已经是修饰后的函数。使用@wraps装饰器可以消除这种影响
        def inner(*args1, **kwargs1):
            # 获取调用修饰函数的参数，并根据参数生成SVM分类器
            print("使用SVM分类器进行训练")
            # 调用原函数
            result = func(*args1, **kwargs1)
            # 计算并输出对应指标
            if "ACC" in args:
                print("ACC: 0.85")
            if "MCC" in args:
                print("MCC: 0.5")
            if "F1" in args:
                print("F1: 0.67")
            if "RECALL" in args:
                print("RECALL: 0.75")
            return result
        return inner
    return wrapper

# RF修饰器
def RF_decorator(*args):
    def wrapper(func):
        @wraps(func)
        def inner(*args1, **kwargs1):
            # 获取调用修饰函数的参数，并根据参数生成随机森林分类器
            print("使用随机森林分类器进行训练")
            # 调用原函数
            result = func(*args1, **kwargs1)
            # 计算并输出对应指标
            if "ACC" in args:
                print("ACC: 0.87")
            if "MCC" in args:
                print("MCC: 0.52")
            if "F1" in args:
                print("F1: 0.69")
            if "RECALL" in args:
                print("RECALL: 0.77")
            return result
        return inner
    return wrapper

# CNN修饰器
def CNN_decorator(*args):
    def wrapper(func):
        @wraps(func)
        def inner(*args1, **kwargs1):
            # 获取调用修饰函数的参数，并根据参数生成卷积神经网络
            print("使用卷积神经网络进行训练")
            # 调用原函数
            result = func(*args1, **kwargs1)
            # 计算并输出对应指标
            if "ACC" in args:
                print("ACC: 0.88")
            if "MCC" in args:
                print("MCC: 0.56")
            if "F1" in args:
                print("F1: 0.71")
            if "RECALL" in args:
                print("RECALL: 0.78")
            return result
        return inner
    return wrapper

# RNN修饰器
def RNN_decorator(*args):
    def wrapper(func):
        @wraps(func)
        def inner(*args1, **kwargs1):
            # 获取调用修饰函数的参数，并根据参数生成循环神经网络
            print("使用循环神经网络进行训练")
            # 调用原函数
            result = func(*args1, **kwargs1)
            # 计算并输出对应指标
            if "ACC" in args:
                print("ACC: 0.86")
            if "MCC" in args:
                print("MCC: 0.53")
            if "F1" in args:
                print("F1: 0.68")
            if "RECALL" in args:
                print("RECALL: 0.76")
            return result
        return inner
    return wrapper

@RF_decorator("ACC", "F1")
@CNN_decorator("MCC", "RECALL")
@SVM_decorator("MCC", "F1")
@RNN_decorator("ACC", "RECALL")
def classify(data):
    # 这里是分类器的具体实现，为了简化演示省略
    print("分类器训练完成")

# 生成测试数据
data = dataSampling(intdata= (int, 10), floatdata= (float, 5), strdata= (str, 2))

# 调用分类函数
classify(data)