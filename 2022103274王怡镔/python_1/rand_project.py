# -*- coding: utf-8 -*-

import numpy
import string
import numpy as np
from python_1.rand_data import rand_integer
from python_1.rand_data import rand_string
from python_1.rand_data import rand_float


def data_sampling(**kwargs):
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


def test():
    return data_sampling(data_type='int', num=6000, row=1000, column=6, data_range=(0, 100))
    # print(data_sampling(data_type='float', num=6000, row=1000, column=6, data_range=(0, 100)))
    # print(data_sampling(data_type='str', num=6000, row=1000, column=6, data_range=string.ascii_letters + string.digits,
    #                     str_length=4))
    #
    # print(data_sampling(data_type='bool', num=6000, row=1000, column=6, data_range=(0, 100)))
