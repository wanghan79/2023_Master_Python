import random
import string
from pprint import pprint
class MLPackage:
    def __init__(self, *args):
        self.methods = args

    def __call__(self, func):
        def wrapper(**kwargs):
            result = func(**kwargs)
            result['package'] = 'MLPackage'
            result['methods'] = self.methods
            return result
        return wrapper


class VerifyPackage:
    def __init__(self, *args):
        self.indicators = args

    def __call__(self, func):
        def wrapper(**kwargs):
            result = func(**kwargs)
            result['package'] = 'VerifyPackage'
            result['indicators'] = self.indicators
            return result
        return wrapper


@MLPackage('SVM', 'RF', 'CNN', 'RNN')
@VerifyPackage('ACC', 'MCC', 'F1', 'RECALL')
def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == 'int':
            result[key] = [random.randint(value['low'], value['high'])]
        elif key == 'float':
            result[key] = [random.uniform(value['low'], value['high'])]
        elif key == 'str':
            length = value['length']
            result[key] = [''.join(random.choices(string.ascii_letters + string.digits, k=length))]
        # elif key == 'tuple':
        #     length = value['length']
        #     result[key] = [tuple(random.choices(range(value['low'], value['high']+1), k=length))]
    return result

result = dataSampling(
int={'type': 'int', 'low': 1, 'high': 100},
float={'type': 'float', 'low': 0.0, 'high': 1.0},
str={'type': 'str', 'length': 10})
# tuple={'type': 'tuple', 'low': 1, 'high': 10, 'length': 5})

if __name__ == '__main__':
    pprint(result)