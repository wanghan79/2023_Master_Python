import random
import string
from pprint import pprint
class Factory:
    def create_data(self, **kwargs):
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
            # elif value['type'] == 'tuple':
            #     length = value['length']
            #     self.data[key] = tuple(random.choices(range(value['low'], value['high']+1), k=length))
        return self.data


class MLFactory:
    def __init__(self, methods):
        self.methods = methods

    def create_ml(self):
        return MLPackage(self.methods)


class MLPackage:
    def __init__(self, methods):
        self.methods = methods

    def execute(self, data):
        print("Executing machine learning methods:", self.methods)
        print("Data:", data)


class VerifyFactory:
    def __init__(self, indicators):
        self.indicators = indicators

    def create_verify(self):
        return VerifyPackage(self.indicators)


class VerifyPackage:
    def __init__(self, indicators):
        self.indicators = indicators

    def evaluate(self, data):
        print("Evaluating verification indicators:", self.indicators)
        print("Data:", data)


data_sampling_factory = Factory()
data_sampling = data_sampling_factory.create_data(
    int = {'type': 'int', 'low': 1, 'high': 100},
    float = {'type': 'float', 'low': 0.0, 'high': 1.0},
    str = {'type': 'str', 'length': 8}
    # tuple_data={'type': 'tuple', 'low': 1, 'high': 10, 'length': 5}
)

data = data_sampling.generate_data()

ml_factory = MLFactory(['SVM', 'RF', 'CNN', 'RNN'])
ml_package = ml_factory.create_ml()

verify_package_factory = VerifyFactory(['ACC', 'MCC', 'F1', 'RECALL'])
verify_package = verify_package_factory.create_verify()

if __name__ == '__main__':
    pprint(f"Generated Data:{data}")
    ml_package.execute(data)
    verify_package.evaluate(data)