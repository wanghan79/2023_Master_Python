import math
from functools import wraps

# 第二层修饰器，接收第一层修饰器的返回值并进一步处理


class standards:
    def __init__(self, *args):
        self.indexs = args

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data, label, predict = func(*args, **kwargs)
            assessmentCriteria = []

            # predict每行对应一个模型标签，单独对每个模型计算各项评估指标，将指标放入一个字典中
            for pre in predict:
                criDict = {}
                for index in self.indexs:
                    TP, TN, FP, FN = self.calcultate(label, pre)

                    if index == 'ACC':
                        criDict['ACC'] = self.ACC(TP, TN, len(label))
                    elif index == 'MCC':
                        criDict['MCC'] = self.MCC(TP, TN, FP, FN)
                    elif index == 'F1':
                        criDict['F1'] = self.F1(TP, TN, len(label))
                    elif index == 'Recall':
                        criDict['Recall'] = self.Recall(TP, FN)

                assessmentCriteria.append(criDict)
            return data, label, predict, assessmentCriteria

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

    def ACC(self, TP, TN, labelNum):
        acc = (TP + TN) / labelNum
        return acc

    def MCC(self, TP, TN, FP, FN):
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FN)
                                              * (TP + FP) * (TN + FP) * (TN + FN))
        return mcc

    def F1(self, TP, TN, labelNum):
        f1 = 2 * TP / (labelNum + TP - TN)
        return f1

    def Recall(self, TP, FN):
        recall = TP / (TP + FN)
        return recall
