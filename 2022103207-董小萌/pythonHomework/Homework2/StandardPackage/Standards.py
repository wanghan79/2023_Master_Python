import random

import numpy as np
from functools import wraps
class Standards:
    # 被修饰的函数以及函数自己的参数
    def __init__(self, EVAL = ''):
        self.EVAL = EVAL

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Eval : {EVAL} '.format(EVAL=self.EVAL))
            data, label, results = func(*args, **kwargs)
            predict = None
            if self.EVAL == "ACC":
                print('EVAL with ACC')
                predict = self.ACC(label, results)
            elif self.EVAL == "MCC":
                print('EVAL with MCC')
                predict = self.MCC(label, results)
            elif self.EVAL == "F1":
                print('EVAL with F1')
                predict = self.F1(label, results)
            elif self.EVAL == "Recall":
                print('EVAL with Recall')
                predict = self.Recall(label, results)
            return data, label, results, predict
        return wrapper

    def ACC(self, label, results):
        print('ACC running.')
        predict = random.random()
        # 计算
        return predict

    def MCC(self, label, results):
        print('MCC running.')
        predict = random.random()
        # 计算
        return predict

    def F1(self, label, results):
        print('F1 running.')
        predict = random.random()
        # 计算
        return predict

    def Recall(self, label, results):
        print('Recall running.')
        predict = random.random()
        # 计算
        return predict

