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


svm = SVM()
svm.accuracy('data')

rf = RF()
rf.mcc('data')

cnn = CNN()
cnn.f1('data')

rnn = RNN()
rnn.recall('data')