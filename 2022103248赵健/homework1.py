import random

def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.randint(0, value))
        elif key == 'float':
            result.append(random.uniform(0, value))
        elif key == 'str':
            result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=value)))
    return result
