import random
import string


def dataSampling(*args, **kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            if 'range' in value:
                result.append(random.sample(range(value['range'][0], value['range'][1]), value['num']))
            else:
                result.append([random.randint(value['start'], value['end']) for _ in range(value['num'])])
        elif key == 'float':
            result.append([random.uniform(value['low'], value['high']) for _ in range(value['num'])])
        elif key == 'str':
            result.append([''.join(random.sample(string.ascii_letters + string.digits, value['length'])) for _ in
                           range(value['num'])])
    return result

result = dataSampling(int={'num': 5, 'start': 1, 'end': 10},float={'num': 5, 'low': 0.0, 'high': 1.0},str={'num': 5, 'length': 6})
print(result)