import random
import string

class DataSamplingFactory:
    def create_data_sampling(self, **kwargs):
        return DataSampling(**kwargs)


class DataSampling:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.data = {}

    def generate_data(self):
        for key, value in self.kwargs.items():
            if value['type'] == 'int':
                self.data[key] = random.randint(value['low'], value['high'])
            elif value['type'] == 'float':
                self.data[key] = random.uniform(value['low'], value['high'])
            elif value['type'] == 'str':
                length = value['length']
                self.data[key] = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            elif value['type'] == 'tuple':
                length = value['length']
                self.data[key] = tuple(random.choices(range(value['low'], value['high']+1), k=length))
        return self.data


class MLPackageFactory:
    def __init__(self, methods):
        self.methods = methods

    def create_ml_package(self):
        return MLPackage(self.methods)


class MLPackage:
    def __init__(self, methods):
        self.methods = methods

    def execute(self, data):
        # Placeholder for executing machine learning methods
        print("Executing machine learning methods:", self.methods)
        print("Data:", data)


class VerifyPackageFactory:
    def __init__(self, indicators):
        self.indicators = indicators

    def create_verify_package(self):
        return VerifyPackage(self.indicators)


class VerifyPackage:
    def __init__(self, indicators):
        self.indicators = indicators

    def evaluate(self, data):
        # Placeholder for evaluating verification indicators
        print("Evaluating verification indicators:", self.indicators)
        print("Data:", data)


# 示例调用
data_sampling_factory = DataSamplingFactory()
data_sampling = data_sampling_factory.create_data_sampling(
    int_data={'type': 'int', 'low': 1, 'high': 100},
    float_data={'type': 'float', 'low': 0.0, 'high': 1.0},
    str_data={'type': 'str', 'length': 10},
    tuple_data={'type': 'tuple', 'low': 1, 'high': 10, 'length': 5}
)

data = data_sampling.generate_data()
# print("Generated Data:", data)

ml_package_factory = MLPackageFactory(['SVM', 'RF', 'CNN', 'RNN'])
ml_package = ml_package_factory.create_ml_package()
# ml_package.execute(data)

verify_package_factory = VerifyPackageFactory(['ACC', 'MCC', 'F1', 'RECALL'])
verify_package = verify_package_factory.create_verify_package()
# verify_package.evaluate(data)
