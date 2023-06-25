import random

def randomMetric(metric):
    def decorator(func):
        def wrapper(*args):
            print("Calculating", metric, "metric...")
            return func(*args)
        return wrapper
    return decorator

def randomMethod(method):
    def decorator(func):
        def wrapper(*args):
            print("Running", method, "method...")
            return func(*args)
        return wrapper
    return decorator

@randomMethod("PF")
@randomMetric("ACC")
def dataSampling(**kwargs):
    result = []
    for data_type, data_num in kwargs.items():
        if data_type == "int":
            result.extend(random.sample(range(1, 100), data_num))
        elif data_type == "float":
            result.extend([random.uniform(0, 1) for _ in range(data_num)])
        elif data_type == "str":
            result.extend([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(data_num)])
    return result

# 调用示例
def task2_run():
    data = dataSampling()
    print(data)