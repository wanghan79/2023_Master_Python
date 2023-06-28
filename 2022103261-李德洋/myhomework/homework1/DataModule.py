import random
import string

def dataSampling(data_type, length, **kwargs):
    result = []
    # length = int(length)
    # for data_type, length in kwargs.items():
    length = int(length)
    if data_type == 'int':
        result.extend(random.sample(range(0, 10 * length), length))
    elif data_type == 'float':
        result.extend([random.uniform(0, 1) for _ in range(length)])
    elif data_type == 'str':
        result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(length)])
    print(result)
    return result

# 调用
# result = dataSampling(data_type = 'str', length = 10)
# print(result)



