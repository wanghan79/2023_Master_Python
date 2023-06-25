import random
import string

# 随机数据结构生成函数
def generate_random(data_type, num=1, **kwargs):
    """
    生成随机数据的函数

    Parameters:
        data_type: str，要生成的数据类型，包括'int', 'float', 'str'。
        num: int，要生成的数据个数，默认为1。
        kwargs: dict，根据不同数据类型，可接受不同的参数，包括'int'类型的'start'和'end'，
                'float'类型的'start'和'end'，'str'类型的'length'。

    Returns:
        生成的随机数据，根据不同的数据类型返回不同类型的数据。
    """
    try:
        if data_type == 'int':
            start = kwargs.get('start', 0)
            end = kwargs.get('end', 100)
            return random.randint(start, end)
        elif data_type == 'float':
            start = kwargs.get('start', 0.0)
            end = kwargs.get('end', 1.0)
            return random.uniform(start, end)
        elif data_type == 'str':
            length = kwargs.get('length', 5)
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        else:
            raise ValueError("Invalid data type: {}".format(data_type))
    except Exception as e:
        print("Error: {}".format(e))


# 类工厂 - 机器学习方法修饰器
class MachineLearningMethodsFactory:
    def __init__(self, *methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("Applying machine learning methods: {}".format(self.methods))
            return result
        return wrapper


# 类工厂 - 验证指标操作修饰器
class ValidationMetricsFactory:
    def __init__(self, *metrics):
        self.metrics = metrics

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("Applying validation metrics: {}".format(self.metrics))
            return result
        return wrapper


# 使用类工厂创建修饰器实例
machine_learning_methods = MachineLearningMethodsFactory('SVM', 'RF', 'CNN', 'RNN')
validation_metrics = ValidationMetricsFactory('ACC', 'MCC', 'F1', 'RECALL')


# 使用修饰器修饰生成随机数据结构函数
@machine_learning_methods
@validation_metrics
def generate_random_data_structure(data_type, num=1, **kwargs):
    return generate_random(data_type, num, **kwargs)


# 调用示例
random_int = generate_random_data_structure('int')
print(random_int)

random_float_list = generate_random_data_structure('float', num=10)
print(random_float_list)

random_string = generate_random_data_structure('str', length=10)
print(random_string)
