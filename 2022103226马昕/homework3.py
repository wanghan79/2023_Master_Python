import random
import string
class DataSamplingDecoratorFactory:
    @staticmethod
    def create_decorator(*args, **kwargs):
        def decorator(func):
            def wrapper(*args, **kwargs):
                # 执行机器学习方法
                for method in args:
                    print(f"Applying {method} on data...")
                    # 执行机器学习操作

                # 执行精度指标操作
                for metric in kwargs:
                    print(f"Calculating {metric}...")
                    # 执行精度指标计算

                # 调用原始函数
                return func(*args, **kwargs)

            return wrapper

        return decorator


@DataSamplingDecoratorFactory.create_decorator("SVM", "RF", ACC=True, F1=True)
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == "int":
            result.extend(random.sample(range(value['start'], value['end'] + 1), value['num']))
        elif key == "float":
            result.extend([random.uniform(value['start'], value['end']) for _ in range(value['num'])])
        elif key == "str":
            result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=value['length'])) for _ in
                           range(value['num'])])
    return result


# 示例调用
dataSampling(int={'start': 1, 'end': 100, 'num': 10})
dataSampling(float={'start': 0, 'end': 1, 'num': 5})
dataSampling(str={'length': 5, 'num': 3})
