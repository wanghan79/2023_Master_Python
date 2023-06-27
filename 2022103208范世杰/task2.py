import random
import string

def dataSampling(func):
    def wrapper(*args):
        result = {}
        for arg in args:
            if isinstance(arg, tuple) and len(arg) == 2:
                data_type = arg[0]
                data_range = arg[1]
                if data_type == int:
                    result[arg] = random.randint(*data_range)
                elif data_type == float:
                    result[arg] = random.uniform(*data_range)
                elif data_type == str:
                    length = random.randint(*data_range)
                    result[arg] = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                else:
                    print(f"Unsupported data type: {data_type}")
            else:
                print(f"Invalid input: {arg}")

        return func(result)

    return wrapper


def machineLearningMethods(*ml_methods):
    def decorator(func):
        def wrapper(data):
            print("Machine learning methods used:")
            for ml_method in ml_methods:
                print(ml_method)
            return func(data)
        return wrapper
    return decorator


def evaluationMetrics(*metrics):
    def decorator(func):
        def wrapper(data):
            result = func(data)
            print("Evaluation metrics used:")
            for metric in metrics:
                print(metric)
            return result
        return wrapper

    return decorator
@dataSampling
@machineLearningMethods("SVM", "RF")
@evaluationMetrics("ACC", "MCC")
def processRandomData(data):
    print("Processing random data...")
    print(f"Data: {data}")

processRandomData(
    (int, (1, 100)),
    (float, (0.0, 1.0)),
    (str, (5, 10))
)
