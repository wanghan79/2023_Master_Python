"""
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，
四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。
主要考察点是带参数修饰器的使用，具体要求如下：
1. 修饰器类型不限，可以是函数修饰器或类修饰器；
2. 实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""

import random

def mlMethod(method):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"{method} - {result}")
        return wrapper
    return decorator

def accuracyMetric(metric):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"{metric} - {result}")
        return wrapper
    return decorator

@mlMethod('SVM')
@accuracyMetric('ACC')
def svm_accuracy(data):
    return random.random()

@mlMethod('RF')
@accuracyMetric('MCC')
def rf_mcc(data):
    return random.random()

@mlMethod('CNN')
@accuracyMetric('F1')
def cnn_f1(data):
    return random.random()

@mlMethod('RNN')
@accuracyMetric('RECALL')
def rnn_recall(data):
    return random.random()


