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

class SVM:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class RF:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class CNN:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class RNN:
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
class ACC:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)


class MCC:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)

class F1:
    def __init__(self, name):
        self.name = name
        print("Creating machine learning method:", name)
class RECALL:
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
            raise ValueError("Invalid metric name!!!")