import random
import string
 
# 机器学习方法西九十七
def machine_learning_methods(methods):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Executing machine learning methods...")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 验证指标操作方法修饰器
def evaluation_metrics(metrics):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Calculating evaluation metrics...")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@machine_learning_methods('SVM', 'RF', 'CNN', 'RNN')
@evaluation_metrics('ACC', 'MCC', 'F1', 'RECALL')
def dataSampling(**kwargs):
    result = []
    for dtype, num in kwargs.items():
        if dtype == 'int':
            data = [random.randint(0, 100) for _ in range(num)]
        elif dtype == 'float':
            data = [random.uniform(0, 100) for _ in range(num)]
        elif dtype == 'str':
            data = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(num)]
        else:
            print(f"Invalid data type: {dtype}")
            continue
        result.extend(data)
    return result


result = dataSampling(int=5, float=3, str=4)
print(result)
