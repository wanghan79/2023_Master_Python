import random
import string

def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value['type'] == 'int':
            result[key] = random.randint(value['low'], value['high'])
        elif value['type'] == 'float':
            result[key] = random.uniform(value['low'], value['high'])
        elif value['type'] == 'str':
            length = value['length']
            result[key] = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        elif value['type'] == 'tuple':
            length = value['length']
            result[key] = tuple(random.choices(range(value['low'], value['high']+1), k=length))
    return result


result = dataSampling(
    int_data={'type': 'int', 'low': 1, 'high': 100},
    float_data={'type': 'float', 'low': 0.0, 'high': 1.0},
    str_data={'type': 'str', 'length': 10},
    tuple_data={'type': 'tuple', 'low': 1, 'high': 10, 'length': 5}
)

# print(result)
