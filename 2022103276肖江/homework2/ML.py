from functools import wraps
import numpy as np

# 第一层修饰器，对dataSampling函数进行修饰


class ML:
    def __init__(self, *args):
        self.models = args

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data, label = func(*args, **kwargs)

            predict = []
            for model in self.models:
                if model == "SVM":
                    predict.append(list(self.SVMPredict(data)))

                elif model == "RF":
                    predict.append(list(self.RFPredict(data)))

                elif model == "CNN":
                    predict.append(list(self.CNNPredict(data)))

                elif model == "RNN":
                    predict.append(list(self.RNNPredict(data)))
            predict = np.array(predict)
            return data, label, predict  # 返回值，在这里返回真实label和每个模型预测label，传入下一层评价指标

        return wrapper

    # 随机生成相应模型的预测结果
    def SVMPredict(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def RFPredict(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def CNNPredict(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def RNNPredict(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result
