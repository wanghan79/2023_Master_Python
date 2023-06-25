import random
import string


def dataSampling():
    def decorator(func):
        def wrapper(*args):
            result = []
            for data_type, data_num in args:
                if data_type == 'int':
                    result.extend(random.sample(range(1, 100), data_num))
                elif data_type == 'float':
                    result.extend([random.uniform(1, 100) for _ in range(data_num)])
                elif data_type == 'str':
                    result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 50))) for _ in range(data_num)])
            return func(result)
        return wrapper
    return decorator


# 第一个修饰器，用于选择机器学习方法
def ml_method(*args):
    mt = args[0].upper()

    def decorator(func):
        def wrapper(data):
            if mt == 'SVM':
                print("使用SVM支持向量机!")
            elif mt == 'RF':
                print("使用RF随机森林!")
            elif mt == 'CNN':
                print("使用CNN!")
            elif mt == 'RNN':
                print("使用RNN!")
            return func(data)
        return wrapper

    return decorator


# 第二个修饰器，用于选择精度指标
def accuracy_metric(*args):
    am = args[0].upper()

    def decorator(func):
        def wrapper(data):
            if am == 'ACC':
                print("使用ACC精度验证!")
            elif am == 'MCC':
                print("使用MCC精度验证!")
            elif am == 'F1':
                print("使用F1精度验证!")
            elif am == 'RECALL':
                print("使用RECALL精度验证!")
            return func(data)
        return wrapper
    return decorator


a, b, c = map(int, input("请分别输入需要产生int, float, str的个数：").split())
method, acc = input("请输入深度学习方法（SVM, RF, CNN, RNN）和精度验证(ACC, MCC, F1, RECALL):").split()


# 调用示例
@dataSampling()
@ml_method(method)
@accuracy_metric(acc)
def processRandomData(data):
    print("随机数据结构:", data)


processRandomData(('int', a), ('float', b), ('str', c))
