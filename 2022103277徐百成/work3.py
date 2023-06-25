"""
平时作业3：
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架
"""
import random
import string


class DataStructureGenerator:
    def __init__(self, **kwargs):
        self.data_structure = []

        for key, value in kwargs.items():
            if key == 'int':
                self.data_structure.append(random.randint(0, value))
            elif key == 'float':
                self.data_structure.append(random.uniform(0, value))
            elif key == 'str':
                length = value
                self.data_structure.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))

    def get_data_structure(self):
        return self.data_structure

class SVMModel:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class RFModel:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class CNNModel:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class RNNModel:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class MLMethodFactory:
    def create_ml_method(self, model):
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
class ACCMetric:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)


class MCCMetric:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)

class F1Metric:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class RECALLMetric:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class EvaluationMetricFactory:
    def create_evaluation_metric(self, metric):
        if metric == 'ACC':
            return ACCMetric('ACC')
        elif metric == 'MCC':
            return MCCMetric('MCC')
        elif metric == 'F1':
            return F1Metric('F1')
        elif metric == 'RECALL':
            return RECALLMetric('RECALL')
        else:
            raise ValueError("Invalid metric name.")
