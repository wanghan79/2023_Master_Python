#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_homework
@File    ：script1.py
@Author  ：yang
@Date    ：2023/6/26 17:17 
'''
'''
交现随机数据结构生成封装函数dataSampling(**kwargs)以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下;
1.采用关键亭参数作为随机数据结构及数量的输入;
2.在不修改代码的前提下，根据kwargs定义内容卖现任意数量、任意难度、一层深度的随机数据结构生成;
3.其中随机数涵盖int，fioat和str三种类型
'''
import random


def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        # print(key, value)
        if key == 'int':
            result.append(random.randint(*value))
        elif key == 'float':
            result.append(random.uniform(*value))
        elif key == 'str':
            length = random.randint(*value)
            result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length)))
        elif key == 'list':
            result.append([i for i in range(value[0][0], value[0][1])])

    return result


def dataRenderer(data, level=0):
    if isinstance(data, (int, float, str)):
        print('    ' * level + str(data))
    elif isinstance(data, list):
        print('    ' * level + '[')
        for item in data:
            dataRenderer(item, level + 1)
        print('    ' * level + ']')
    elif isinstance(data, dict):
        print('    ' * level + '{')
        for key, value in data.items():
            print('    ' * (level + 1) + str(key) + ':')
            dataRenderer(value, level + 2)
        print('    ' * level + '}')


# 调用示例1
print('example'.center(50, '='))
result1 = dataSampling(int=(1, 100), float=(0, 100), str=(5, 10), list=[(1, 10)], dict={int: (0, 100)})
dataRenderer(result1)
