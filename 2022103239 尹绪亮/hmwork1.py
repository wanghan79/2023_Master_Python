import random

def dataSampling(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if value["type"] == "int":
            result[key] = [random.randint(value["start"], value["end"]) for _ in range(value["num"])]
        elif value["type"] == "float":
            result[key] = [random.uniform(value["start"], value["end"]) for _ in range(value["num"])]
        elif value["type"] == "str":
            result[key] = ["".join(random.choices(value["candidate"], k=value["length"])) for _ in range(value["num"])]
        else:
            result[key] = []

    return result
if __name__ == '__main__':

 result1 = dataSampling(numbers={"type": "int", "start": 1, "end": 100, "num": 10})
 result2=dataSampling( percentages={"type": "float", "start": 1, "end": 10, "num": 5})
 result3=dataSampling(names={"type": "str", "candidate": "abcdefghijklmnopqrstuvwxyz", "length": 5, "num": 3})

print(result1)
print(result2)
print(result3)