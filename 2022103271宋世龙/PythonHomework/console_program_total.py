# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/15
@Auth    : song
@File    : console_program_total.py
@IDE     : PyCharm
@Edition : 001
@Describe: 结课作业：
建立完整项目工程，将三次平时作业集成在一个工程中，实现控制台交互，提示用户输入要求展示的作业号（1、2或3），自动运行相应作业示例，并将结果输出到控制台。
"""
import os
import time


def console_program_homework_num():
    while True:
        homework_num = input('Please enter the python homework number: ')
        if homework_num in ['0', '1', '2']:
            print('\nRunning python homework {}...\n'.format(homework_num)), time.sleep(2), print(
                'Running results as follows...\n'), time.sleep(1)
            os.system('python python_homework_{}/full_code.py'.format(homework_num))
            break
        else:
            print('Your input is incorrect. Please re-enter')
            continue


console_program_homework_num()
# test1
# class A:
#     def __call__(self, *args, **kwargs):
#         print('test A')
#
#
# a = A()
# a()

# test2
# class Cache:
#     def __init__(self, func):
#         self.func = func
#         self.data = {}
#
#     def __call__(self, *args, **kwargs):
#         func = self.func
#         data = self.data
#         key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
#         if key in data:
#             result = data.get(key)
#             print('cached')
#         else:
#             result = func(*args, **kwargs)
#             data[key] = result
#             print('calculated')
#         return result
#
#
# @Cache
# def rectangle_area(length, width):
#     return length * width
#
#
# # rectangle_area(2, 3)
# rectangle_area(2, 3)

# test3
# a = [0, 1, 2, 3]
# b = ['a', 'b', 'c', 'd']
# d = list()
# for i in a:
#     for j in b:
#         c = [i, j]
#         d.append(c)
#
# print(d)

# test4
# from sklearn.metrics import matthews_corrcoef
#
# print(matthews_corrcoef([1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#                         [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]))

# test5
# class Animal(object):
#     def eat(self):
#         print("动物吃东西")
#
#
# class Cat(Animal):
#     def eat(self):
#         print("猫吃鱼")
#         # 格式一：父类名.方法名(对象)
#         Animal.eat(self)
#         # 格式二:super(本类名,对象).方法名()
#         super(Cat, self).eat()
#         # 格式三:super()方法名()
#         super().eat()
#
#
# cat1 = Cat()
# cat1.eat()
# print(cat1)

# test6
# def funcA(num1):
#     def funcB(num2):
#         return num1 + num2
#
#     return funcB
#
#
# funcAdd1 = funcA(1)
# y = funcAdd1(10)
# print(y)
# # y 结果为 11
#
# print(funcA(1)(10))

# test7
# from abc import ABCMeta, abstractmethod
#
# """
# 建立一个可乐的抽象类，百事可乐和可口可乐继承这个抽象类
# ABCMeta是python的一个元类，用于在Python程序中创建抽象基类，抽象基类中声明的抽象方法，使用abstractmethod装饰器装饰。
# """
#
#
# class Coke(metaclass=ABCMeta):
#
#     @abstractmethod
#     def drink(self, a):
#         pass
#
#
# class Kekou(Coke):
#     def drink(self, a):
#         print(a)
#         print('喝可口可乐')
#
#
# class Baishi(Coke):
#     def drink(self, a):
#         print(a)
#         print('喝百事可乐')
#
#
# """
# 建立快餐店类，也就是所说的工厂类，让它生产可乐。
# 当用户需要可乐时，只需要告诉快餐店做一份什么品牌的可乐，告诉快餐店可乐的名字，然后快餐店使用make_coke方法做可乐，返回了你所需要的对象
# 拿到可口可乐的对象，就可以调用自己实现的方法了。
# """
#
#
# class Fast_food_restaurant:
#     def make_coke(self, name):
#         a = 1
#         # eval（类名）返回的是一个class类型的对象
#         return eval(name)(a)
#
#
# kfc = Fast_food_restaurant()
# coke = kfc.make_coke('Kekou')
# coke.drink(1)
