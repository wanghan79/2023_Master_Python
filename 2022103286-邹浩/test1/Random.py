import random
import numpy as np
import string

def dataSampling(**kwargs):
    len = kwargs['len']
    shape = kwargs['shape']
    desire_type = kwargs['desire_type']
    str_length = kwargs['str_length']

    result = []
    for datatype in desire_type:
        for _ in range(0, len):
            if datatype == 'float':
                result.append(np.random.uniform(0, 10, shape))
            elif datatype == 'int':
                result.append(np.random.randint(0, 10, shape))
            elif datatype == 'str':
                item = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_length))
                result.append(item)
    return result

result = dataSampling(len=2, shape=(2, 3, 5), desire_type=['int', 'str'], str_length=26)
print(result)