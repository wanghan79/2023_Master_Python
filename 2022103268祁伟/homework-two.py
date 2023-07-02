import random
import string

def L_M(methods):
    def dec(func):
        def wrap(*args, **kwargs):
            print(f"Using the following learning methods: {methods}")
            return func(*args, **kwargs)
        return wrap
    return dec

def E_M(metrics):
    def dec(func):
        def wrap(*args, **kwargs):
            print(f"Using the following evaluation metrics: {metrics}")
            return func(*args, **kwargs)
        return wrap
    return dec

@L_M(["SVM", "RF", "CNN", "RNN"])
@E_M(["ACC", "MCC", "F1", "RECALL"])

def Sample2(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "int":
            result["int"] = [random.randint(value[0], value[1]) for _ in range(value[2])]
        elif key == "float":
            result["float"] = [random.uniform(value[0], value[1]) for _ in range(value[2])]
        elif key == "str":
            result["str"] = [''.join(random.choices(string.ascii_letters + string.digits, k=value[0])) for _ in range(value[1])]
    return result
instance = Sample2(int=(-2, 2, 1), float=(-3.0, 2.0, 4), str=(2, 3))
print(instance)