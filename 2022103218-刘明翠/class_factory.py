import random


class DataSamplingFactory:
    def __init__(self, *args):
        self.methods = args

    def create_data_sampling(self):
        def dataSampling(**kwargs):
            result = []

            for data_type, data_range in kwargs.items():
                if data_type == 'int':
                    result.append(random.randint(*data_range))
                elif data_type == 'float':
                    result.append(random.uniform(*data_range))
                elif data_type == 'str':
                    result.append(''.join(random.choices(data_range, k=random.randint(1, 10))))

            return result

        for method in self.methods:
            print(f"Applying {method} machine learning method...")

        for metric in ['ACC', 'MCC', 'F1', 'RECALL']:
            if metric in self.methods:
                print(f"Calculating {metric} accuracy...")

        return dataSampling


# 创建类工厂实例
factory = DataSamplingFactory('SVM', 'RF', 'ACC', 'F1')

# 创建数据生成函数
dataSampling = factory.create_data_sampling()

data = dataSampling(int=(1, 100), float=(0.0, 1.0), str='mingtian')
print(data)
