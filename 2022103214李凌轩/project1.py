import random
import string

def dataSampling(**kwargs):
    result = []
    for key,value in kwargs.items():
        if key == 'int':
            for i in range(value):
                result.append(random.randint(0,100))
        elif key == 'float':
            for i in range(value):
                result.append(random.uniform(0,1))
        elif key == 'str':
            for i in range(value):
                result.append(''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,10))))
    return result

# # 测试示例
# print(dataSampling(int=3))
# print(dataSampling(float=3))
# print(dataSampling(str=3))
# print(dataSampling(int=2, float=4, str=1))