import random


def datasampling(num=1, length=10, **kwargs):
    result = list()
    for i in range(num):
        if 'data_type' in kwargs:
            data_type = kwargs['data_type']
        else:
            data_type = random.choice([int, float, str, list, tuple, dict])
        if data_type == int:
            if 'range_start' in kwargs and 'range_end' in kwargs:
                result.append(random.randint(kwargs['range_start'], kwargs['range_end']))
            else:
                result.append(random.randint(-100, 100))
        elif data_type == float:
            if 'range_start' in kwargs and 'range_end' in kwargs:
                result.append(random.uniform(kwargs['range_start'], kwargs['range_end']))
            else:
                result.append(random.uniform(-100, 100))
        elif data_type == str:
            result.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length)))
        elif data_type == list:
            result.append([random.randint(kwargs.get('range_start', -100), kwargs.get('range_end', 100)) for i in range(length)])
        elif data_type == tuple:
            result.append(tuple(random.randint(kwargs.get('range_start', -100), kwargs.get('range_end', 100)) for i in range(length)))
        elif data_type == dict:
            result.append({i: random.randint(kwargs.get('range_start', -100), kwargs.get('range_end', 100)) for i in range(length)})
        else:
            raise ValueError('Unsupported data type')
    return result


print(datasampling(num=5, data_type=int, range_start=0, range_end=9))
# print(datasampling(num=3, data_type=str, length=5))
