import random
"""
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架。
"""


class DataSampler:
    def __init__(self):
        pass

    def reshape(self, res, new_shape):
        new_len = len(res)

        # 每次拿最后n个元素组成一个列表
        for n in new_shape[::-1]:
            # print("----------")
            lst = []
            for _ in range(new_len // n):  # 拿几次
                tmp = res[-n:]  # 切片，取最后n个元素
                # print("tmp:", tmp)
                lst.insert(0, tmp)  # 头插
                res = res[:-n]  # 剩下的切片重新赋值

            # print("lst:", lst)
            res = lst
            new_len //= n

        return res

    def dataSampling(self, **kwargs):
        new_shape, type1 = kwargs.get('shape'), kwargs.get('type')
        print('我想要一个{}维度的随机数据，其中每个元素的类型是{}'.format(new_shape, type1))

        # 计算列表长度，即new_shape的每一个元素乘起来
        data_len = 1
        for _ in new_shape:
            data_len *= _

        # 根据type生成数据
        res = []
        for _ in range(data_len):
            tmp = []
            for data_type in type1:
                if data_type == int:
                    tmp.append(random.randint(1, 100))
                elif data_type == float:
                    tmp.append(round(random.uniform(0, 100), 3))
                elif data_type == str:
                    tmp.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10))))
                else:
                    print(f'unsupported data type: {data_type}')
            res.append(tmp)

        # print('当前获取的随机列表为{}, 我想要的维度是{}.'.format(res, new_shape))
        return self.reshape(res, new_shape)


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
    results = data_sampler.dataSampling(shape=(3, 2, 2), type=(int, str, float, int))
    print(f'result={results}')


if __name__ == '__main__':
    main()

