import random
import string

def dataSampling(**kwargs):
    data = []
    for key, value in kwargs.items():
        if key == 'int':
            for i in range(value):
                data.append(random.randint(0, 100))
        elif key == 'float':
            for i in range(value):
                data.append(random.uniform(0, 1))
        elif key == 'str':
            for i in range(value):
                data.append(''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,10))))
    return data

# # 测试示例
# print(dataSampling(int=5))
# print(dataSampling(float=2))
# print(dataSampling(str=4))
# print(dataSampling(int=3, float=4, str=5))