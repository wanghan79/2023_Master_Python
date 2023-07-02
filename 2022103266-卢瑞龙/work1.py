import random

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
