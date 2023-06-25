"""
平时作业2：
采用修饰器技术对作业1随机数据结构生成函数进行修饰，
实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，
四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。
主要考察点是带参数修饰器的使用，
具体要求如下：
1. 修饰器类型不限，可以是函数修饰器或类修饰器；
2. 实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""
import random
import string


# 类修饰器
class MLMethod:
    def __init__(self, method_name):
        self.method_name = method_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 执行机器学习方法
            print("Running machine learning method:", self.method_name)
            result = func(*args, **kwargs)
            return result

        return wrapper


#
class EvaluationMetric:
    def __init__(self, metric_name):
        self.metric_name = metric_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 执行精度指标操作
            print("Running evaluation metric:", self.metric_name)
            result = func(*args, **kwargs)
            return result

        return wrapper


@MLMethod("CNN")
@EvaluationMetric("RECALL")
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.randint(0, value))
        elif key == 'float':
            result.append(random.uniform(0, value))
        elif key == 'str':
            length = value
            result.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    return result
