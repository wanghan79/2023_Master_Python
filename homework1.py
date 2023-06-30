import random
import string

def dataSampling(**kwargs):
    """
    生成随机数据结构
    :param kwargs: 关键字参数，包含数据结构类型和数量
    :return: 返回生成的数据结构
    """
    result = {}
    for key, value in kwargs.items():
        if key == 'int':
            result[key] = [random.randint(0, 100) for _ in range(value)]
        elif key == 'float':
            result[key] = [random.uniform(0, 100) for _ in range(value)]
        elif key == 'str':
            result[key] = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(value)]
    return result
# 生成10个int类型、5个float类型、3个str类型的数据结构
result = dataSampling(int=10, float=5, str=3)

# 输出结果
print(result)