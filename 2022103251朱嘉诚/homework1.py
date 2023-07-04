import random
import string

def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, tuple) and len(value) == 2:
            dataType = value[0]
            dataNumber = value[1]
            if dataType == int:
                result[key] = random.sample(range(1, 101), dataNumber)
            elif dataType == float:
                result[key] = [round(random.uniform(1.0, 100.0), 2) for i in range(dataNumber)]
            elif dataType == str:
                result[key] = [''.join(random.sample(string.ascii_letters + string.digits, 8)) for i in
                               range(dataNumber)]
    return result


result = dataSampling(intdata=(int, 5), floatdata=(float, 8), strdata=(str, 4))
for key in result:
    print(key, ":", result[key])
#print(result)
