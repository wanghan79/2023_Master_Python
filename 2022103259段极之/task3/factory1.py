from pprint import pprint
# from task1 import datasampling
from task2 import decorator
class DataGeneratorFactory:
    def __init__(self, method, metric):
        self.method = method
        self.metric = metric

    def generate_data(self, **kwargs):
        print(f"Using {self.method} method.")
        print(f"Calculating {self.metric}.")
        return decorator.dataSampling(**kwargs)

factory_svm_acc = DataGeneratorFactory("SVM", "ACC")
sample_data3 = factory_svm_acc.generate_data(
    int={'type': 'int', 'low': 1, 'high': 100},
    float={'type': 'float', 'low': 0, 'high': 1},
    str={'type': 'str', 'length': 8}
)
pprint(sample_data3)