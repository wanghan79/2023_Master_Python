import math
from functools import wraps

'''
作为第二层修饰器，先接收第一层修饰器的返回值
'''


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
        '''
        使用一个模型标签和真实值计算混淆矩阵
        :param label:
        :param pre:
        :return: TP, TN, FP, FN
        '''
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
