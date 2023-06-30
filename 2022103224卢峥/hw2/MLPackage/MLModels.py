# from sklearn.svm import svc
from random import random


class MLModels(object):

    def __init__(self, *args):
        self._model = args

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            results = list()
            # 2. call model: according to the parameters
            for model in self._model:
                if model == "SVM":
                    results = self.SVM(data)
                elif model == "RF":
                    results = self.RF(data)
                elif model == "CNN":
                    results = self.CNN(data)
                else:
                    results = self.RNN(data)
            return results
        return wrapper

    def SVM(self, data):
        results = list()
        for i in range(5):
            result = random(0, 1)
            results.append(result)

        return results

    def RF(self, data):
        results = list()

        return results

    def CNN(self, data):
        results = list()
        for i in range(len(data[0])):
            col_data = [row[i] for row in data]
            num_non_missing = sum(1 for val in col_data if val is not None)
            if num_non_missing < 2:
                results.append(None)
            else:
                sorted_vals = sorted(col_data)
                min_diff = float('inf')
                for j in range(1, len(sorted_vals)):
                    diff = sorted_vals[j] - sorted_vals[j - 1]
                    if diff < min_diff:
                        min_diff = diff
                cnn = min_diff / (max(col_data) - min(col_data))
                results.append(cnn)
        return results

    def RNN(self, data):
        results = list()
        for i in range(len(data[0])):
            col_data = [row[i] for row in data]
            num_non_missing = sum(1 for val in col_data if val is not None)
            if num_non_missing < 2:
                results.append(None)
            else:
                sorted_vals = sorted(col_data)
                max_diff = -float('inf')
                for j in range(1, len(sorted_vals)):
                    diff = sorted_vals[j] - sorted_vals[j - 1]
                    if diff > max_diff:
                        max_diff = diff
                rnn = max_diff / (max(col_data) - min(col_data))
                results.append(rnn)
        return results
