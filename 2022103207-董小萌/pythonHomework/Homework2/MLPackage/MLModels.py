import numpy as np
from functools import wraps
class MLModels:

    def __init__(self, MLM=None):
        self.MLM = MLM

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Model : {MLM} '.format(MLM=self.MLM))
            data, label = func(*args, **kwargs)
            results = None
            if self.MLM == "SVM":
                print('Modle is SVM')
                results = self.SVM(data, label)
            elif self.MLM == "RF":
                print('Modle is RF')
                results = self.RF(data, label)
            elif self.MLM == "CNN":
                print('Modle is CNN')
                results = self.CNN(data, label)
            elif self.MLM == "RNN":
                print('Modle is RNN')
                results = self.RNN(data, label)
            return data, label, results
        return wrapper

    def train(self, data):
        print('Training...')
        return np.random.random(size=len(data))

    def SVM(self, data, label):
        print('SVM running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result

    def RF(self, data, label):
        print('RF running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result

    def CNN(self, data, label):
        print('CNN running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result

    def RNN(self, data, label):
        print('RNN running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result