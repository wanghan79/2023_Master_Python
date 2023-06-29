import random
import numpy as np
import string

def dataSampling(**kwargs):
    len = kwargs['len']
    shape = kwargs['shape']
    desire_type = kwargs['desire_type']
    str_length = kwargs['str_length']

    float_data = []
    int_data = []
    string_data = []
    for datatype in desire_type:
        for _ in range(0, len):
            if datatype == 'float':
                float_data.append(np.random.uniform(0, 10, shape))
            elif datatype == 'int':
                int_data.append(np.random.randint(0, 10, shape))
            elif datatype == 'str':
                item = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_length))
                string_data.append(item)
    return float_data ,int_data, string_data


'''生成2组随机整数和2组字符串，随机整数形状为(2,2,5)，字符串长度为26'''
result = dataSampling(len=2, shape=(2, 2, 5), desire_type=['int', 'str'], str_length=26)
print(result)