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


class MLMethodFactory:
    def create_ml_method(self, method_name):
        print("Creating machine learning method:", method_name)
        # 在这里根据method_name创建对应的机器学习方法实例并返回
        pass


class EvaluationMetricFactory:
    def create_evaluation_metric(self, metric_name):
        print("Creating evaluation metric:", metric_name)
        # 在这里根据metric_name创建对应的精度指标实例并返回
        pass
