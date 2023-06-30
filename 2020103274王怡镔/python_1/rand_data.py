import random
import string


def rand_integer(num, data_range):
    """
    生成由任意个数的整型随机数构成的数据集
    :param num: 整型随机数个数
    :param data_range: 元素范围
    """
    result_int = list()
    for i in range(num):
        it = iter(data_range)
        item = random.randint(next(it), next(it))
        result_int.append(item)
    return result_int


def rand_float(num, data_range):
    """
    生成由任意个数的浮点型随机数构成的数据集
   :param num: 浮点数随机数个数
    :param data_range: 元素范围
    """
    result_flt = list()
    for i in range(num):
        it = iter(data_range)
        item = random.uniform(next(it), next(it))
        result_flt.append(item)
    return result_flt


def rand_string(num, data_range, str_length):
    """
    随机生成字符串
    :param num:
    :param data_range:
    :param str_length:
    :return:
    """
    result_str = list()
    for i in range(num):
        random_str = ''.join(random.SystemRandom().choice(data_range) for _ in range(str_length))
        result_str.append(random_str)
    return result_str


# print(rand_integer(10, (2, 200)))
