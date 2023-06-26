#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_homework
@File    ：main.py
@Author  ：yang
@Date    ：2023/6/26 17:21 
'''
import random
from script1 import dataSampling, dataRenderer
from script2 import svm_accuracy, rf_mcc, cnn_f1, rnn_recall
from script3 import Factory

def Script1():
    # result1 = dataSampling(int=(1, 100), float=(0, 100), str=(5, 10), list=[(1, 10)])
    result1 = dataSampling(int=(1, 100), float=(0, 100), str=(5, 10))
    dataRenderer(result1)

def Script2():

    svm_accuracy(1024)
    rf_mcc(1024)
    cnn_f1(1024)
    rnn_recall(1024)

def Script3():

    factory = Factory('SVM', 'RF', 'ACC', 'F1')

    data_sampling = factory.generate_sampling()

    data = data_sampling(int=(1, 100), float=(0.0, 1.0), str='yangyang')
    print(data)


def test(choice):
    if choice == 1:
        Script1()
    elif choice == 2:
        Script2()
    elif choice == 3:
        Script3()



if __name__ == "__main__":

    print("choose which script do you want to test")

    while True:
        try:
            choice = int(input("Please enter the script number: 1, 2 or 3, "))
            test(choice)

        except ValueError:
            print("There is something wrong with your input")
