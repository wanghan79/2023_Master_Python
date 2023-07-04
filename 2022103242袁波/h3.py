import random
import string
"""
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架。
"""


def _generate_data(shape, data_type):
    if len(shape) == 0:
        if len(data_type) == 1:
            if data_type[0] == "int":
                return (random.randint(-100, 100))
            elif data_type[0] == "float":
                return (round(random.uniform(-100.0, 100.0), 2))
            elif data_type[0] == "str":
                return (''.join(random.choices(string.ascii_letters, k=8)))
            else:
                raise ValueError("data_type参数类型应该是整形，浮点型，字符型")
        else:
            res = []
            for i in range(len(data_type)):
                if data_type[i] == "int":
                    res.append(random.randint(-100, 100))
                elif data_type[i] == "float":
                    res.append(round(random.uniform(-100.0, 100.0), 2))
                elif data_type[i] == "str":
                    res.append(''.join(random.choices(string.ascii_letters, k=8)))
                else:
                    raise ValueError("data_type参数类型应该是整形，浮点型，字符型")
            return res
    else:
        return [_generate_data(shape=shape[1:], data_type=data_type) for _ in range(shape[0])]
class DataSampler:
    def __init__(self):
        pass

    def dataSampling(self,**kwargs):
        shape = kwargs.get("shape", [1, ])
        data_type = kwargs.get("data_type", ["int"])
        for i in shape:
            if i < 0:
                raise ValueError("shape参数不能为负数")
            elif i == 0:
                raise ValueError("shape参数不能为0")
        return _generate_data(shape, data_type)




class Factory:
    def __init__(self, models=None, metrics=None):
        self.models = models or []
        self.metrics = metrics or []

    def create_data_sampler(self):
        print("机器学习方法模型:")
        for model in self.models:
            if model == 'SVM':
                print('执行了SVM操作...')
            elif model == 'RF':
                print('执行了RF操作...')
            elif model == 'CNN':
                print('执行了CNN操作...')
            elif model == 'RNN':
                print('执行了RNN操作...')

        print("\n精度指标操作:")
        for metric in self.metrics:
            if metric == 'ACC':
                print('执行了ACC操作...')
            elif metric == 'MCC':
                print('执行了MCC操作...')
            elif metric == 'F1':
                print('执行了F1操作...')
            elif metric == 'RECALL':
                print('执行了RECALL操作...')

        return DataSampler()


# 调用示例
def main():
    models = ["SVM", "RF", "CNN", "RNN"]
    metrics = ["ACC", "MCC", "F1", "RECALL"]
    factory = Factory(models=models, metrics=metrics)
    data_sampler = factory.create_data_sampler()
    results = data_sampler.dataSampling(shape=[10,5], data_type=['int','float','str'])
    print(f'result={results}')


if __name__ == '__main__':
    main()
