# import random
#
#
# def randomInt(datarange, num):
#     result = set()
#     for index in range(0, num):
#         it = iter(datarange)
#         item = random.randint(next(it), next(it))
#         result.add(item)
#     return result
#
#
# def randomFloat(datarange, num):
#     result = set()
#     for index in range(0, num):
#         it = iter(datarange)
#         item = random.uniform(next(it), next(it))
#         result.add(item)
#     return result
#
#
# def randomStr(datarange, strlength):
#     result = set()
#     item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlength))
#     result.add(item)
#     return result
#
#
# def dataSampling(**kwargs):
#     result_1 = randomInt([2, 100], 10)
#     result_2 = randomFloat([11.2, 15.6], 10)
#     result_3 = randomStr(['a', 'z'], 10)
#     print("随机整形：")
#     print(result_1)
#     print("随机字符型：")
#     print(result_2)
#     print("随机字符型：")
#     print(result_3)
import random
import string


def dataSampling(**kwargs):  # 传入参数名称=数值的形式后在函数内部接收为一个字典
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


def run_work1():
    result = dataSampling(
        int_data=(int, (1, 100)),
        float_data=(float, (0.0, 1.0)),
        str_data=(str, (5, 10))
    )
    print(result)
