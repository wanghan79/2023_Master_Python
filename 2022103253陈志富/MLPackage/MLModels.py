import numpy as np

class MLModels:
    def __init__(self, *args):
        self._models = args

    def __call__(self, func):
        def wrapper(data,*args, **kwargs):
            results = list()
            for model in self._models:
                if model == "SVM":
                    result = self.SVM(data)
                elif model == "RF":
                    result = self.RF(data)
                elif model == "CNN":
                    result = self.CNN(data)
                elif model == "RNN":
                    result = self.RNN(data)
                else:
                    print("model error!")
                results.append(result)
            return results
        return wrapper

    def SVM(self, data):
        results = np.random.randint(size=len(data))
        return results

    def RF(self, data):
        results = np.random.randint(size=len(data))
        return results

    def CNN(self, data):
        results = np.random.randint(size=len(data))
        return results

    def RNN(self, data):
        results = np.random.randint(size=len(data))
        return results
