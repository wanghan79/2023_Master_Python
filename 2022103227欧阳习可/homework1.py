#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 8:47
# @Author  : ouyangxike
# @FileName: random_sample.py
# @Software: PyCharm
import random
import string

def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            start = value[0]
            end = value[1]
            num = value[2]
            result.append([random.randint(start, end) for _ in range(num)])
        elif key == 'float':
            start = value[0]
            end = value[1]
            num = value[2]
            result.append([random.uniform(start, end) for _ in range(num)])
        elif key == 'str':
            length = value[0]
            num = value[1]
            result.append([''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(num)])
    return result
result = dataSampling(int=[1, 10, 5], float=[0.0, 1.0, 5], str=[8, 3])

print(result)
