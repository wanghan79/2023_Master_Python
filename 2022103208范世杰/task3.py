import random
import string


class DataSampling:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
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

        return self.func(result)


class MachineLearningMethods:
    def __init__(self, *ml_methods):
        self.ml_methods = ml_methods

    def __call__(self, func):
        def wrapper(data):
            print("Machine learning methods used:")
            for ml_method in self.ml_methods:
                print(ml_method)

            return func(data)

        return wrapper


class EvaluationMetrics:
    def __init__(self, *metrics):
        self.metrics = metrics

    def __call__(self, func):
        def wrapper(data):
            result = func(data)
            print("Evaluation metrics used:")
            for metric in self.metrics:
                print(metric)

            return result

        return wrapper
@DataSampling
@MachineLearningMethods("SVM", "RF")
@EvaluationMetrics("ACC", "MCC")
def processRandomML(data):
    print("Processing random data...")
    print(f"Data: {data}")

processRandomML(
    (int, (1, 100)),
    (float, (0.0, 1.0)),
    (str, (5, 10))
)
