import random


def dataSampling(numbers=0, floats=0, strings=0):
    result = {
        'numbers': [],
        'floats': [],
        'strings': []
    }

    for _ in range(numbers):
        result['numbers'].append(random.randint(1, 100))

    for _ in range(floats):
        result['floats'].append(round(random.uniform(1, 100), 2))

    for _ in range(strings):
        result['strings'].append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)))

    return result


def dataSamplingDecorator(func):
    def wrapper(*args, **kwargs):
        print("=== Random Data Sampling ===")
        result = func(*args, **kwargs)
        print("Generated Data:", result)
        print("===========================")
        return result

    return wrapper
