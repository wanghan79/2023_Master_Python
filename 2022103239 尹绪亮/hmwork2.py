import random
import string

# 随机数据生成函数，与原作业1中的函数相同
def dataSampling(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if value["type"] == "int":
            result[key] = [random.randint(value["start"], value["end"]) for _ in range(value["num"])]
        elif value["type"] == "float":
            result[key] = [random.uniform(value["start"], value["end"]) for _ in range(value["num"])]
        elif value["type"] == "str":
            result[key] = ["".join(random.choices(value["candidate"], k=value["length"])) for _ in range(value["num"])]
        else:
            result[key] = []

    return result


# 函数修饰器，添加机器学习方法和验证指标操作
def decorate_dataSampling_func(*args):
    def decorator(func):
        def wrapper(**kwargs):
            # 调用原函数生成随机数据
            data = func(**kwargs)

            # 对每个参数名进行操作
            for key in kwargs.keys():
                # 对每个机器学习方法进行操作
                for method in args:
                    print("Method: ", method)

                # 对每个验证指标进行操作
                for metric in args:
                    print("Metric: ", metric)

            return data

        return wrapper
    return decorator


# 类修饰器，将原函数变为类方法并添加机器学习方法和验证指标操作
class decorate_dataSampling_class:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 调用原函数生成随机数据
            data = func(*args, **kwargs)

            # 对每个参数名进行操作
            for key in kwargs.keys():
                # 对每个机器学习方法进行操作
                for method in self.args:
                    print("Method: ", method)

                # 对每个验证指标进行操作
                for metric in self.args:
                    print("Metric: ", metric)

            return data

        return wrapper

# 装饰函数dataSampling，使用函数修饰器
@decorate_dataSampling_func("SVM", "RF", "CNN", "RNN", "ACC", "MCC", "F1", "RECALL")
def dataSampling1(**kwargs):
    return dataSampling(**kwargs)

# 通过配置参数来初始化类装饰器
decorate = decorate_dataSampling_class("SVM", "RF", "CNN", "RNN", "ACC", "MCC", "F1", "RECALL")

# 装饰函数dataSampling，使用类修饰器
@decorate
def dataSampling2(**kwargs):
    return dataSampling(**kwargs)
if __name__ == '__main__':

    # 调用函数进行测试
    # print(dataSampling1(numbers={"type": "int", "start": 1, "end": 100, "num": 10}, percentages={"type": "float", "start": 1, "end": 10, "num": 5}, names={"type": "str", "candidate": "abcdefghijklmnopqrstuvwxyz", "length": 5, "num": 3}))

    # 调用类方法进行测试
    ds = dataSampling2()
    print(ds({"numbers": {"type": "int", "start": 1, "end": 100, "num": 10}, "percentages": {"type": "float", "start": 1, "end": 10, "num": 5}, "names": {"type": "str", "candidate": "abcdefghijklmnopqrstuvwxyz", "length": 5, "num": 3}}))