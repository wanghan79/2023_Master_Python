"""
平时作业3：
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架
"""

class SVMModel:
    def __init__(self, name):
        self.name = name

    def apply(self):
        print(f"Applying {self.name}...")


class RFModel:
    def __init__(self, name):
        self.name = name

    def apply(self):
        print(f"Applying {self.name}...")


class CNNModel:
    def __init__(self, name):
        self.name = name

    def apply(self):
        print(f"Applying {self.name}...")


class RNNModel:
    def __init__(self, name):
        self.name = name

    def apply(self):
        print(f"Applying {self.name}...")


class MLFactory:
    def create_ml_model(self, model):
        if model == 'SVM':
            return SVMModel('SVM')
        elif model == 'RF':
            return RFModel('RF')
        elif model == 'CNN':
            return CNNModel('CNN')
        elif model == 'RNN':
            return RNNModel('RNN')
        else:
            raise ValueError("Invalid model name.")