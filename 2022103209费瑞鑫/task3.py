"""
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架。
"""
import random


class MLFactory:
    def __init__(self, method):
        self.method = method

    def __call__(self, cls):
        setattr(cls, 'mlMethod', self.mlMethod)
        setattr(cls, 'accuracyMetric', self.accuracyMetric)
        return cls

    @staticmethod
    def mlMethod(func):
        def wrapper(self, *args):
            result = func(self, *args)
            print(f"{type(self).__name__}.{func.__name__} - {result}")

        return wrapper

    @staticmethod
    def accuracyMetric(func):
        def wrapper(self, *args):
            result = func(self, *args)
            print(f"ACC - {result}")

        return wrapper


@MLFactory('SVM')
class SVM:
    @MLFactory.mlMethod
    def accuracy(self, data):
        return random.random()


@MLFactory('RF')
class RF:
    @MLFactory.mlMethod
    def mcc(self, data):
        return random.random()


@MLFactory('CNN')
class CNN:
    @MLFactory.mlMethod
    def f1(self, data):
        return random.random()


@MLFactory('RNN')
class RNN:
    @MLFactory.mlMethod
    def recall(self, data):
        return random.random()


