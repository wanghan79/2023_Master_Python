from functools import wraps
import numpy as np


class ML:
    def __init__(self, *args):
        self.models = args

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            data, label = func(*args, **kwargs)

            predict = []
            for model in self.models:
                if model == "SVM":
                    predict.append(list(self.SVM(data)))

                elif model == "RF":
                    predict.append(list(self.RF(data)))

                elif model == "CNN":
                    predict.append(list(self.CNN(data)))

                elif model == "RNN":
                    predict.append(list(self.RNN(data)))
            predict = np.array(predict)
            return data, label, predict

        return wrapped_function

    def SVM(self, data):

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
