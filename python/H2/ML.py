from functools import wraps
import numpy as np

'''
作为第一层修饰器，对dataSampling函数进行修饰
'''


class ML:
    def __init__(self, *args):
        self.models = args

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            # 1.接受数据data.shape(nums, features), label.shape(nums)都是0和1
            data, label = func(*args, **kwargs)

            predict = []
            for model in self.models:
                # 2.记录各个模型结果
                if model == "SVM":
                    predict.append(list(self.SVM(data)))

                elif model == "RF":
                    predict.append(list(self.RF(data)))

                elif model == "CNN":
                    predict.append(list(self.CNN(data)))

                elif model == "RNN":
                    predict.append(list(self.RNN(data)))
            predict = np.array(predict)
            return data, label, predict  # 返回值，在这里返回真实label和每个模型预测label，传入下一层评价指标

        return wrapped_function

    def SVM(self, data):
        '''
        随机产生对应长度的标签，其他model也是如此
        '''
        result = np.random.randint(2, size=(len(data)))
        return result

    def RF(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def CNN(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def RNN(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result
