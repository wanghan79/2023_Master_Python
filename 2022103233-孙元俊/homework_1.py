import random
import string


def dataSampling(**kwargs):
    result = []
    for data_type, data_num in kwargs.items():
        if data_type == 'int':
            result.extend(random.sample(range(0, 100), data_num))
        elif data_type == 'float':
            result.extend([random.uniform(0, 100) for _ in range(data_num)])
        elif data_type == 'str':
            result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 50))) for _ in range(data_num)])
    return result


# 调用示例
a, b, c = map(int, input("请分别输入需要产生int, float, str的个数：").split())
random_data = dataSampling(int=a, float=b, str=c)
print(random_data)
