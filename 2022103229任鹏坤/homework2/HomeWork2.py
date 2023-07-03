"""
平时作业2：
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
1.	修饰器类型不限，可以是函数修饰器或类修饰器；
2.	实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""
import math
from functools import wraps
import numpy as np
class ML:
    def __init__(self, *args):
        self.models = args

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            #接受数据和标签
            data, label = func(*args, **kwargs)
            predict = []
            #记录模型的结果数据
            for model in self.models:
                if model == "SVM":
                    predict.append(list(self.SVM(data)))
                elif model == "RF":
                    predict.append(list(self.RF(data)))
                elif model == "CNN":
                    predict.append(list(self.CNN(data)))
                elif model == "RNN":
                    predict.append(list(self.RNN(data)))
            predict = np.array(predict)
            return data, label, predict  # 返回truth label和predict label
        return wrapped_function

    def SVM(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def RF(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def CNN(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result

    def RNN(self, data):
        result = np.random.randint(2, size=(len(data)))
        return result


class Criteria:
    def __init__(self, *args):
        self.indexs = args
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data, label, predict = func(*args, **kwargs)
            assessment_criteria = []

            # predict每行对应一个模型标签，单独对每个模型计算各项评估指标，将指标放入一个字典中
            for pre in predict:
                cri_dict = {}
                for index in self.indexs:
                    TP, TN, FP, FN = self.calcultate(label, pre)

                    if index == 'ACC':
                        cri_dict['ACC'] = self.ACC(TP, TN, len(label))
                    elif index == 'MCC':
                        cri_dict['MCC'] = self.MCC(TP, TN, FP, FN)
                    elif index == 'F1':
                        cri_dict['F1'] = self.F1(TP, TN, len(label))
                    elif index == 'Recall':
                        cri_dict['Recall'] = self.Recall(TP, FN)

                assessment_criteria.append(cri_dict)
            return data, label, predict, assessment_criteria

        return wrapper

    def calcultate(self, label, pre):
        TP, TN, FP, FN = 0, 0, 0, 0
        for i in range(len(label)):
            if label[i] == 1 and pre[i] == 1:
                TP = TP + 1
            if label[i] == 0 and pre[i] == 0:
                TN = TN + 1
            if label[i] == 0 and pre[i] == 1:
                FP = FP + 1
            if label[i] == 1 and pre[i] == 0:
                FN = FN + 1
        return TP, TN, FP, FN
    def ACC(self, TP, TN, label_num):
        acc = (TP + TN) / label_num
        return acc
    def MCC(self, TP, TN, FP, FN):
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FN) * (TP + FP) * (TN + FP) * (TN + FN))
        return mcc
    def F1(self, TP, TN, label_num):
        f1 = 2 * TP / (label_num + TP - TN)
        return f1
    def Recall(self, TP, FN):
        recall = TP / (TP + FN)
        return recall
class Sampling:
    def __init__(self, nums, n):
        self.nums = nums
        self.n = n

    def create(self):
        x_data = np.random.random((self.nums, self.n))
        y_data = np.random.randint(2, size=len(x_data))
        return x_data, y_data


@Criteria('ACC', 'MCC', 'F1','Recall')
@ML('SVM', 'RF', 'CNN', 'RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.create()


# 测试：输入10个含5个特征的样本，输出真实lable之后输出每个模型输出的label
data, label, predict, assessment_criteria = dataSampling(10, 5)

print(data)
print(label)  # (10)
print(predict)  # (3,10),分别是装饰器中三个模型的预测
print(assessment_criteria)