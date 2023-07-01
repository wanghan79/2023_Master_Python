# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/12
@Auth    : song
@File    : task_data_sampling.py
@IDE     : PyCharm
@Edition : 001
@Describe: 复制自python_homework_0.full_code.py
"""
import numpy
import random
import string
import numpy as np


# conf = {'num': 6000, 'row': 1000, 'column': 6}  # 配置文件示例
def data_sampling(**kwargs) -> numpy.ndarray or str:
    # 控制台输入练习
    # last_name = input('请输入姓氏：')
    # first_name = input('请输入名字：')
    # print('名字：', last_name + first_name)

    # 读取参数
    data_type = kwargs['data_type']
    # 生成row*column维的数据集
    num = kwargs['num']  # num = row * column
    row = kwargs['row']
    column = kwargs['column']
    data_range = kwargs['data_range']
    # 所要生成数据的类型清单
    if data_type == 'int':
        result_int = rand_integer(num, data_range)
        avail_dataset = np.array(result_int).reshape(row, column)
        return avail_dataset
    elif data_type == 'float':
        result_flt = rand_float(num, data_range)
        avail_dataset = np.array(result_flt).reshape(row, column)
        return avail_dataset
    elif data_type == 'str':
        str_length = kwargs['str_length']
        result_str = rand_string(num, data_range, str_length)
        avail_dataset = np.array(result_str).reshape(row, column)
        return avail_dataset
    # elif data_type not in ['int', 'float', 'str']: 下面一行的写法更简洁
    else:
        return 'Sorry, we are unable to generate this type of data at the moment. Please stay tuned for future updates.'


def rand_integer(num, data_range) -> list:
    """
    生成由任意个数的整型随机数构成的数据集
    :param num: 整型随机数个数
    :param row: 数据集元素个数
    :param column: 元素维度
    :param data_range: 元素范围
    :return: 可用数据集
    """
    result_int = list()
    for i in range(num):
        it = iter(data_range)
        item = random.randint(next(it), next(it))
        result_int.append(item)
    # avail_dataset = np.array(result_int).reshape(row, column)
    return result_int


def rand_float(num, data_range) -> list:
    """
    生成由任意个数的浮点型随机数构成的数据集，参数及返回值含义同上
    :param num:
    :param row:
    :param column:
    :param data_range:
    :return:
    """
    result_flt = list()
    for i in range(num):
        it = iter(data_range)
        item = random.uniform(next(it), next(it))
        result_flt.append(item)
    # avail_dataset = np.array(result_flt).reshape(row, column)
    return result_flt


def rand_string(num, data_range, str_length) -> list:
    """
    生成字符串，具体内容同上
    :param num:
    :param row:
    :param column:
    :param data_range:
    :param str_length:
    :return:
    """
    result_str = list()
    for i in range(num):
        random_str = ''.join(random.SystemRandom().choice(data_range) for _ in range(str_length))
        # 从'a'-'z', 'A'-'Z', '0'-'9'中选取元素随机生成指定长度字符串，两种写法
        # random_str =
        # ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(strlen))
        # ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()') for _ in range(strlen))
        result_str.append(random_str)
    # avail_dataset = np.array(result_str).reshape(row, column)
    return result_str

# data_sampling(**conf)  # 配置文件读取参数

# 测试
# 生成由范围在[0,100]的6000个整型、浮点型和字符串类型的数据构成的1000*6*1维数据集
# print(data_sampling(data_type='int', num=6000, row=1000, column=6, data_range=(0, 100)))
# print(data_sampling(data_type='float', num=6000, row=1000, column=6, data_range=(0, 100)))
# print(data_sampling(data_type='str', num=6000, row=1000, column=6, data_range=string.ascii_letters + string.digits,
#                     str_length=4))
#
# print(data_sampling(data_type='bool', num=6000, row=1000, column=6, data_range=(0, 100)))
