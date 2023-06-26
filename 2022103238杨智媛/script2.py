#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_homework
@File    ：script2.py
@Author  ：yang
@Date    ：2023/6/26 17:18 
'''
'''
采用修饰器技术对作业1随机数搁结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法(SVM,RFCNNRNN)操作，
四种精度指标(ACCMCCF1RECALL)操作以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下;
1.修饰器类型不限，可以是函数修饰器或类修饰器;
2.实现两个修饰器，通过修饰器券数 (*args)实现机醒学习方法和验证指标操作的任意组合;
'''
import random

def ml(method):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"{method} - {result}")
        return wrapper
    return decorator


def accuracy(metric):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"{metric} - {result}")
        return wrapper
    return decorator

@ml('SVM')
@accuracy('ACC')
def svm_accuracy(data):
    return random.random()

@ml('RF')
@accuracy('MCC')
def rf_mcc(data):
    return random.random()

@ml('CNN')
@accuracy('F1')
def cnn_f1(data):
    return random.random()

@ml('RNN')
@accuracy('RECALL')
def rnn_recall(data):
    return random.random()
