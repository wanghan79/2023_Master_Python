import random


def dataSampling(**kwargs):
    result = []

    for data_type, data_range in kwargs.items():
        if data_type == 'int':
            result.append(random.randint(*data_range))
        elif data_type == 'float':
            result.append(random.uniform(*data_range))
        elif data_type == 'str':
            result.append(''.join(random.choices(data_range, k=random.randint(1, 10))))

    return result


data = dataSampling(int=(1, 100), float=(0.0, 1.0), str='mingtian')
print(data)
