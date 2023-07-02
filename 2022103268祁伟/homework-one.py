import random
import string

def Sample1(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "int":
            result["int"] = [random.randint(value[0], value[1]) for _ in range(value[2])]
        elif key == "float":
            result["float"] = [random.uniform(value[0], value[1]) for _ in range(value[2])]
        elif key == "str":
            result["str"] = [''.join(random.choices(string.ascii_letters + string.digits, k=value[0])) for _ in range(value[1])]
    return result
instance = Sample1(int=(-1, 2, -3), float=(-2.0, 4.0, 5), str=(3, 2))
print(instance)