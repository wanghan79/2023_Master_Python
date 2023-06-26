# -*- coding: utf-8 -*-


import numpy
from homework1 import data_sampling as data
from homework1 import random_int as label
from functools import wraps
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef, recall_score, f1_score



class Metrics:
    def __init__(self, *args):
        self._metrics = args

    def __call__(self, func):
        metrics = self._metrics
        @wraps(func)
        def wrapper(*args, **kwargs):
            models, pred_labels, ground_label = func(*args, **kwargs)
            pred_result = []
            pred_accuracy = dict()
            for lab in pred_labels:
                pred_rlt = dict()
                for mtr in metrics:
                    if mtr == 'ACC':
                        pred_rlt[mtr] = self.ACC(ground_label, lab)
                    elif mtr == 'MCC':
                        pred_rlt[mtr] = self.MCC(ground_label, lab)
                    elif mtr == 'RECALL':
                        pred_rlt[mtr] = self.RECALL(ground_label, lab)
                    elif mtr == 'F1_score':
                        pred_rlt[mtr] = self.F1_score(ground_label, lab)
                pred_result.append(pred_rlt)
            for j, mod in enumerate(models):
                pred_accuracy[mod] = pred_result[j]
            return pred_accuracy
        return wrapper
    @staticmethod
    def ACC(y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    @staticmethod
    def MCC(y_true, y_pred):
        return matthews_corrcoef(y_true, y_pred)

    @staticmethod
    def RECALL(y_true, y_pred):
        return recall_score(y_true, y_pred, average='micro')

    @staticmethod
    def F1_score(y_true, y_pred):
        return f1_score(y_true, y_pred, average='micro')


class Models:
    def __init__(self, *args):
        self._model = args

    def __call__(self, func):
        models = self._model

        @wraps(func)
        def wrapper(*args, **kwargs):
            x_trn, x_lab, y_tst, y_lab = func(*args, **kwargs)
            pred_labels = []
            for mod in models:
                if mod == 'SVM':
                    label = self.SVM(x_trn, x_lab, y_tst, y_lab)
                elif mod == 'RF':
                    label = self.RF(x_trn, x_lab, y_tst, y_lab)
                elif mod == 'CNN':
                    pass
                elif mod == 'RNN':
                    pass
                pred_labels.append(label)
            return models, pred_labels, y_lab
        return wrapper

    def SVM(self, x_train, x_label, y_test, y_label):
        module = svm.SVC(kernel='linear')
        module.fit(x_train, x_label)
        module.fit(y_test, y_label)
        return module.predict(y_test)

    def RF(self, x_train, x_label, y_test, y_label):
        module = RandomForestClassifier()
        module.fit(x_train, x_label)
        module.fit(y_test, y_label)
        return module.predict(y_test)

    def CNN(self, x_train, x_label, y_test, y_label):
        pass

    def RNN(self, x_train, x_label, y_test, y_label):
        pass




@Metrics('ACC', 'MCC', 'RECALL', 'F1_score')
@Models('SVM')
def Test(**kwargs):
    data_type = kwargs.get('data_type')
    column = kwargs.get('column')
    data_range = kwargs.get('data_range')
    label_range = kwargs.get('label_range')
    train_data = kwargs.get('train_data')
    test_data = kwargs.get('test_data')
    x_num = train_data * column
    y_num = test_data * column
    x_train = data(data_type=data_type, num=x_num, row=train_data, column=column, data_range=data_range)
    x_label = label(train_data, label_range)
    y_test = data(data_type=data_type, num=y_num, row=test_data, column=column, data_range=data_range)
    y_label = label(test_data, label_range)
    return x_train, x_label, y_test, y_label


def test2():
    test = Test(data_type='int', column=5, data_range=(1, 100), label_range=(0, 1), train_data=1000, test_data=100)
    #print(test)
    return test

test2()