import random

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
data = dataSampling(int=5, float=3, str=4)
print(data)