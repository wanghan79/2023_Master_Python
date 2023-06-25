import random

class RandomDataGenerator:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def generate_data(self):
        result = []

        for data_type, data_range in self.kwargs.items():
            if isinstance(data_range, int):
                result.append(random.randint(0, data_range))
            elif isinstance(data_range, float):
                result.append(random.uniform(0, data_range))
            elif isinstance(data_range, str):
                length = len(data_range)
                result.append(''.join(random.choices(data_range, k=length)))

        return result


class MLMethodFactory:
    def __init__(self):
        self.ml_methods = []

    def add_method(self, ml_method):
        self.ml_methods.append(ml_method)

    def apply_methods(self, data):
        for ml_method in self.ml_methods:
            print(f"Applying {ml_method} on random data...")
            # 在这里执行相应的机器学习方法


class MetricFactory:
    def __init__(self):
        self.metrics = []

    def add_metric(self, metric):
        self.metrics.append(metric)

    def calculate_metrics(self, data):
        for metric in self.metrics:
            print(f"Calculating {metric} on random data...")
            # 在这里执行相应的验证指标操作


# 调用示例
data_generator = RandomDataGenerator(int=100, float=10.0, str='abc')

ml_factory = MLMethodFactory()
ml_factory.add_method('SVM')
ml_factory.add_method('RF')
ml_factory.add_method('CNN')
ml_factory.add_method('RNN')

metric_factory = MetricFactory()
metric_factory.add_metric('ACC')
metric_factory.add_metric('MCC')
metric_factory.add_metric('F1')
metric_factory.add_metric('RECALL')

random_data = data_generator.generate_data()

ml_factory.apply_methods(random_data)

metric_factory.calculate_metrics(random_data)
