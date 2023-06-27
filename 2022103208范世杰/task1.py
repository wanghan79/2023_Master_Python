import random
import string
def dataSampling(**kwargs):    #传入参数名称=数值的形式后在函数内部接收为一个字典
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, tuple) and len(value) == 2:
            data_type = value[0]
            data_range = value[1]
            if data_type == int:
                result[key] = random.randint(*data_range)
            elif data_type == float:
                result[key] = random.uniform(*data_range)
            elif data_type == str:
                length = random.randint(*data_range)
                result[key] = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            else:
                print(f"Unsupported data type: {data_type}")
        else:
            print(f"Invalid input for {key}")

    return result
result = dataSampling(
    int_data=(int, (1, 100)),
    float_data=(float, (0.0, 1.0)),
    str_data=(str, (5, 10))
)
print(result)
