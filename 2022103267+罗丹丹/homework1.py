# -*- coding: utf-8 -*-
from typing import List

import numpy
import numpy as np
import random
import string


#生成整数类型的随机数函数
def random_int(num, data_range):
    data_int = []
    min, max = data_range[0], data_range[1]
    for i in range(num):
        item = random.randint(min, max)
        data_int.append(item)
    return data_int

#生成浮点数类型的随机数
def random_float(num, data_range):
    data_float = []
    min, max = data_range[0], data_range[1]
    for i in range(num):
        item = random.uniform(min, max)
        data_float.append(item)
    return data_float

#生成任意长度的字符串随机数
def random_string(num, data_range, string_length):
    data_string = list()
    for i in range(num):
        random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(string_length))
        data_string.append(random_string)
    return data_string

def data_sampling(**kwargs):
    data_type = kwargs.get('data_type')
    num = kwargs.get('num')
    row = kwargs.get('row')
    column = kwargs.get('column')
    data_range = kwargs.get('data_range')
    if data_type == 'int':
        data_int = random_int(num, data_range)
        dataset = np.array(data_int).reshape(row, column)
        return dataset
    elif data_type == 'float':
        data_float = random_float(num, data_range)
        dataset = np.array(data_float).reshape(row, column)
        return dataset
    elif data_type == 'str':
        string_length = kwargs['string_length']
        data_string = random_string(num, data_range, string_length)
        dataset = np.array(data_string).reshape(row, column)
        return dataset


def test1():
    test = data_sampling(data_type='int', num=10000, row=1000, column=10, data_range=(0, 100))
    #test = data_sampling(data_type='float', num=10000, row=1000, column=10, data_range=(0, 100))
    #test = data_sampling(data_type='str', num=10000, row=1000, column=10, data_range=string.ascii_letters + string.digits,string_length=6)
    #print(test)
    return test
test1()


