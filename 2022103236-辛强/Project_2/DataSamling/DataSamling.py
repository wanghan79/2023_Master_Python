import random
import string


def dataSampling():
    """
    :return:
    """
    datatype = input("请输入您想随机生成的类型：")
    if datatype == "int" :
        s = int(input("您想生成几位随机整数："))
        random_int(s)
    elif datatype == "float":
        d = int(input("您想生成几位随机小数："))
        random_float(d)
    elif datatype == "str":
        v = int(input("您想生成几位随机小数："))
        random_str(v)
    elif datatype == "tuple":
        f = int(input("您想生成几位随机小数："))
        random_tup(f)
    else :
        print("输入类型错误！")
def random_int(num):
    numbers = []
    for i in range (num):
        numbers.append(random.randint(0,10))
    print(numbers)
def random_float(num):
    numbers = []
    for i in range (num):
        numbers.append(random.random(0,10))
    print(numbers)
def random_str(num):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=num))
    print(random_string)
def random_tup(num):
    random_tuple = tuple(random.randint(1, 10) for _ in range(num))
    print(random_tuple)


dataSampling()

