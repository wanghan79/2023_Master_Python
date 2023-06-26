import random


def machineLearningDecorator(*args):
    def decorator(func):
        def wrapper(**kwargs):
            result = func(**kwargs)

            for method in args:
                print(f"Applying {method} machine learning method...")

            for metric in ['ACC', 'MCC', 'F1', 'RECALL']:
                if metric in args:
                    print(f"Calculating {metric} accuracy...")

            return result

        return wrapper

    return decorator


@machineLearningDecorator('SVM', 'RF', 'ACC', 'F1')
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
