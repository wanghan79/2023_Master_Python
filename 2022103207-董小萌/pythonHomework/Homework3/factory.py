import random
from functools import wraps

import numpy as np

from Homework1 import data_sampling
# 平时作业3：
# 采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架


class SVMModel:

    def train(self, data):
        print('Training...')
        return np.random.random(size=len(data))

    def SVM(self, data, label):
        print('SVM running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result


class RFModel:
    def train(self, data):
        print('Training...')
        return np.random.random(size=len(data))

    def RF(self, data, label):
        print('RF running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result


class CNNModel:
    def train(self, data):
        print('Training...')
        return np.random.random(size=len(data))

    def CNN(self, data, label):
        print('CNN running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result


class RNNModel:
    def train(self, data):
        print('Training...')
        return np.random.random(size=len(data))

    def RNN(self, data, label):
        print('RNN running.')
        traindata = self.train(data)
        result = np.random.randint(2, size=len(label))
        # 计算
        return result


class MLModelsFactory:

    def __init__(self, MLM = ''):
        self.MLM = MLM

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Model : {MLM} '.format(MLM=self.MLM))
            data, label = func(*args, **kwargs)
            results = None
            if self.MLM == "SVM":
                print('Modle is SVM')
                model = SVMModel()
                results = model.SVM(data, label)
            elif self.MLM == "RF":
                print('Modle is RF')
                model = RFModel()
                results = model.RF(data, label)
            elif self.MLM == "CNN":
                print('Modle is CNN')
                model = CNNModel()
                results = model.CNN(data, label)
            elif self.MLM == "RNN":
                print('Modle is RNN')
                model = RNNModel()
                results = model.RNN(data, label)
            return data, label, results

        return wrapper

class ACCStandards:

    def ACC(self, label, results):
        print('ACC running.')
        predict = random.random()
        # 计算
        return predict


class MCCStandards:

    def MCC(self, label, results):
        print('MCC running.')
        predict = random.random()
        # 计算
        return predict


class F1Standards:

    def F1(self, label, results):
        print('F1 running.')
        predict = random.random()
        # 计算
        return predict


class RecallStandards:

    def Recall(self, label, results):
        print('Recall running.')
        predict = random.random()
        # 计算
        return predict


class StandardsFactory:

    def __init__(self, EVAL = None):
        self.EVAL = EVAL

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Eval : {EVAL} '.format(EVAL=self.EVAL))
            data, label, results = func(*args, **kwargs)
            predict = None
            if self.EVAL == "ACC":
                print('EVAL with ACC')
                standards = ACCStandards()
                predict = standards.ACC(label, results)
            elif self.EVAL == "MCC":
                print('EVAL with MCC')
                standards = MCCStandards()
                predict = standards.MCC(label, results)
            elif self.EVAL == "F1":
                print('EVAL with F1')
                standards = F1Standards()
                predict = standards.F1(label, results)
            elif self.EVAL == "Recall":
                print('EVAL with Recall')
                standards = RecallStandards()
                predict = standards.Recall(label, results)
            return data, label, results, predict

        return wrapper


@StandardsFactory(EVAL='ACC')
@MLModelsFactory(MLM='SVM')
def SVM_ACC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='MCC')
@MLModelsFactory(MLM='SVM')
def SVM_MCC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='F1')
@MLModelsFactory(MLM='SVM')
def SVM_F1(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='Recall')
@MLModelsFactory(MLM='SVM')
def SVM_Recall(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='ACC')
@MLModelsFactory(MLM='RF')
def RF_ACC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='MCC')
@MLModelsFactory(MLM='RF')
def RF_MCC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='F1')
@MLModelsFactory(MLM='RF')
def RF_F1(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='Recall')
@MLModelsFactory(MLM='RF')
def RF_Recall(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='ACC')
@MLModelsFactory(MLM='CNN')
def CNN_ACC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='MCC')
@MLModelsFactory(MLM='CNN')
def CNN_MCC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='F1')
@MLModelsFactory(MLM='CNN')
def CNN_F1(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='Recall')
@MLModelsFactory(MLM='CNN')
def CNN_Recall(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='ACC')
@MLModelsFactory(MLM='RNN')
def RNN_ACC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='MCC')
@MLModelsFactory(MLM='RNN')
def RNN_MCC(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='F1')
@MLModelsFactory(MLM='RNN')
def RNN_F1(traindata, labeldata):
    return traindata, labeldata


@StandardsFactory(EVAL='Recall')
@MLModelsFactory(MLM='RNN')
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

# data = {'int': 3}
# case1 = data_sampling.data_sampling(**data)[0]
# case2 = data_sampling.data_sampling(**data)[0]
# case3 = data_sampling.data_sampling(**data)[0]
# print(case1, case2, case3)
# load(case1, case2, case3)

def select_standards(model_index, train_data, label_data):
    print("1. ACC")
    print("2. MCC")
    print("3. F1")
    print("4. Recall")
    name = input("请输入要选择的序号：")
    if name == '1':
        load(model_index, 0, train_data, label_data)
    elif name == '2':
        load(model_index, 1, train_data, label_data)
    elif name == '3':
        load(model_index, 2, train_data, label_data)
    elif name == '4':
        load(model_index, 3, train_data, label_data)
    else:
        print("输入有误请重新输入！")


def select_Model(train_data, label_data):
    print("1. SVM")
    print("2. RF")
    print("3. CNN")
    print("4. RNN")
    name = input("请输入要选择的序号：")
    if name == '1':
        select_standards(0, train_data, label_data)
    elif name == '2':
        select_standards(1, train_data, label_data)
    elif name == '3':
        select_standards(2, train_data, label_data)
    elif name == '4':
        select_standards(3, train_data, label_data)
    else:
        print("输入有误请重新输入！")
