import random
import string
from pprint import pprint
def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == 'int':
            result[key] = [random.randint(value['low'], value['high']) for _ in range(value['num'])]
        elif key == 'float':
            result[key] = [random.uniform(value['low'], value['high']) for _ in range(value['num'])]
        elif key == 'str':
            length = value['length']
            result[key] = [''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(value['num'])]
        # elif key == 'tuple':
        #     length = value['length']
        #     result[key] = [tuple(random.choices(range(value['low'], value['high']+1), k=length)) for _ in range(value['num'])]
    return result

result = dataSampling(int={'type': 'int', 'low': 1, 'high': 100, 'num': 5},
float={'type': 'float', 'low': 0.0, 'high': 1.0, 'num': 4},
str={'type': 'str', 'length': 8, 'num': 3})
#,tuple={'type': 'tuple', 'low': 1, 'high': 5, 'length': 3, 'num': 2})

if __name__ == '__main__':
    pprint(result)