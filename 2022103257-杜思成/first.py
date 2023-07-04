import random
import string


def dataSampling1(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "int":
            result["int"] = [random.randint(value[0], value[1]) for _ in range(value[2])]
        elif key == "float":
            result["float"] = [random.uniform(value[0], value[1]) for _ in range(value[2])]
        elif key == "str":
            result["str"] = [''.join(random.choices(string.ascii_letters + string.digits, k=value[0])) for _ in range(value[1])]
    return result


example = dataSampling1(int=(-10, 10, 5), float=(-5.0, 5.0, 7), str=(6, 4))
print(example)