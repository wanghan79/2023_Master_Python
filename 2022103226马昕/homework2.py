import random
import string
from homework1 import dataSampling


def ml_operation(*args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            for operation in args:
                if operation == 'SVM':
                    # 执行SVM操作
                    print("Performing SVM operation on data:", data)
                elif operation == 'RF':
                    # 执行RF操作
                    print("Performing RF operation on data:", data)
                elif operation == 'CNN':
                    # 执行CNN操作
                    print("Performing CNN operation on data:", data)
                elif operation == 'RNN':
                    # 执行RNN操作
                    print("Performing RNN operation on data:", data)
        return wrapper
    return decorator


def accuracy_metrics(*args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            for metric in args:
                if metric == 'ACC':
                    # 计算准确率
                    print("Calculating accuracy (ACC) on data:", data)
                elif metric == 'MCC':
                    # 计算马修斯相关系数
                    print("Calculating Matthews correlation coefficient (MCC) on data:", data)
                elif metric == 'F1':
                    # 计算F1值
                    print("Calculating F1 score on data:", data)
                elif metric == 'RECALL':
                    # 计算召回率
                    print("Calculating recall on data:", data)
        return wrapper
    return decorator


@ml_operation('SVM', 'RF')
@accuracy_metrics('ACC', 'F1')
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == "int":
            result.extend(random.sample(range(value['start'], value['end'] + 1), value['num']))
        elif key == "float":
            result.extend([random.uniform(value['start'], value['end']) for _ in range(value['num'])])
        elif key == "str":
            result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=value['length'])) for _ in range(value['num'])])
    return result
# 生成10个范围在1到100之间的整数，并进行SVM和RF操作以及ACC和F1的指标计算


dataSampling(int={'start': 1, 'end': 100, 'num': 10})

# 生成5个范围在0到1之间的浮点数，并进行SVM和RF操作以及ACC和F1的指标计算
dataSampling(float={'start': 0, 'end': 1, 'num': 5})

# 生成3个长度为5的随机字符串，并进行SVM和RF操作以及ACC和F1的指标计算
dataSampling(str={'length': 5, 'num': 3})
