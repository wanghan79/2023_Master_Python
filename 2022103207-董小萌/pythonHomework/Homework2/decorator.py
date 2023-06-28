from Homework2.MLPackage.MLModels import MLModels
from Homework1 import data_sampling
from Homework2.StandardPackage.Standards import Standards
import numpy as np
import math


# 平时作业2：
# 采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）
# 操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
# 1.修饰器类型不限，可以是函数修饰器或类修饰器；
# 2.实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；

@Standards(EVAL='ACC')
@MLModels(MLM='SVM')
def SVM_ACC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='MCC')
@MLModels(MLM='SVM')
def SVM_MCC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='F1')
@MLModels(MLM='SVM')
def SVM_F1(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='Recall')
@MLModels(MLM='SVM')
def SVM_Recall(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='ACC')
@MLModels(MLM='RF')
def RF_ACC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='MCC')
@MLModels(MLM='RF')
def RF_MCC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='F1')
@MLModels(MLM='RF')
def RF_F1(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='Recall')
@MLModels(MLM='RF')
def RF_Recall(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='ACC')
@MLModels(MLM='CNN')
def CNN_ACC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='MCC')
@MLModels(MLM='CNN')
def CNN_MCC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='F1')
@MLModels(MLM='CNN')
def CNN_F1(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='Recall')
@MLModels(MLM='CNN')
def CNN_Recall(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='ACC')
@MLModels(MLM='RNN')
def RNN_ACC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='MCC')
@MLModels(MLM='RNN')
def RNN_MCC(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='F1')
@MLModels(MLM='RNN')
def RNN_F1(traindata, labeldata):
    return traindata, labeldata


@Standards(EVAL='Recall')
@MLModels(MLM='RNN')
def RNN_Recall(traindata, labeldata):
    return traindata, labeldata


def load(model_index, standards_index, data, label):
    if model_index == 0:
        if standards_index == 0:
            data, label, result, predict = SVM_ACC(data, label)
        elif standards_index == 1:
            data, label, result, predict = SVM_MCC(data, label)
        elif standards_index == 2:
            data, label, result, predict = SVM_F1(data, label)
        elif standards_index == 3:
            data, label, result, predict = SVM_Recall(data, label)
    elif model_index == 1:
        if standards_index == 0:
            data, label, result, predict = RF_ACC(data, label)
        elif standards_index == 1:
            data, label, result, predict = RF_MCC(data, label)
        elif standards_index == 2:
            data, label, result, predict = RF_F1(data, label)
        elif standards_index == 3:
            data, label, result, predict = RF_Recall(data, label)
    elif model_index == 2:
        if standards_index == 0:
            data, label, result, predict = CNN_ACC(data, label)
        elif standards_index == 1:
            data, label, result, predict = CNN_MCC(data, label)
        elif standards_index == 2:
            data, label, result, predict = CNN_F1(data, label)
        elif standards_index == 3:
            data, label, result, predict = CNN_Recall(data, label)
    elif model_index == 3:
        if standards_index == 0:
            data, label, result, predict = RNN_ACC(data, label)
        elif standards_index == 1:
            data, label, result, predict = RNN_MCC(data, label)
        elif standards_index == 2:
            data, label, result, predict = RNN_F1(data, label)
        elif standards_index == 3:
            data, label, result, predict = RNN_Recall(data, label)

    print('data = ', data)
    print('label = ', label)
    print('result = ', result)
    print('predict = ', predict)

def randomdata(row, col):
    train_data = np.random.random((row, col))
    label_data = np.random.randint(2, size=row)
    return train_data, label_data
#
# traindata, labeldata = randomdata(5, 5)
# # print(traindata, labeldata)
#
# data = {'int': 3}
# case1 = data_sampling.data_sampling(**data)[0]
# case2 = data_sampling.data_sampling(**data)[0]
# print(case1, case2)
# load(case1, case2, traindata, labeldata)
