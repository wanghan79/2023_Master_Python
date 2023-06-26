# -*- coding: utf-8 -*-

from homework1 import data_sampling
from homework1 import data_sampling as data
from homework1 import random_int as label
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef, recall_score, f1_score


class ModelFactory:
    def __init__(self, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass


class SVM(ModelFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label):
        module = svm.SVC(kernel='linear')
        module.fit(x_train, x_label)
        module.fit(y_test, y_label)
        return module.predict(y_test)


class RF(ModelFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) :
        module = RandomForestClassifier()
        module.fit(x_train, x_label)
        module.fit(y_test, y_label)
        return module.predict(y_test)


class CNN(ModelFactory):
    pass

class RNN(ModelFactory):
    pass


class EvaluationFactory:
    def __init__(self, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass


class ACC(EvaluationFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, ground_label, pred_label):
        return accuracy_score(ground_label, pred_label)


class MCC(EvaluationFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, ground_label, pred_label) -> float:
        return matthews_corrcoef(ground_label, pred_label)


class Recall(EvaluationFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, ground_label, pred_label):
        return recall_score(ground_label, pred_label, average='micro')


class F1Score(EvaluationFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, ground_label, pred_label):
        return f1_score(ground_label, pred_label, average='micro')


class Test:
    def __init__(self, **kwargs):
        data_type = kwargs.get('data_type')
        column = kwargs.get('column')
        data_range = kwargs.get('data_range')
        label_range = kwargs.get('label_range')
        train_data = kwargs.get('train_data')
        test_data = kwargs.get('test_data')
        x_num = train_data * column
        y_num = test_data * column
        self.x_train = data(data_type=data_type, num=x_num, row=train_data, column=column, data_range=data_range)
        self.x_label = label(train_data, label_range)
        self.y_test = data(data_type=data_type, num=y_num, row=test_data, column=column, data_range=data_range)
        self.y_label = label(test_data, label_range)
    def __call__(self, ML_choice, MC_choice):
        x_train = self.x_train
        x_label = self.x_label
        y_test = self.y_test
        y_label = self.y_label
        pred_label = eval(ML_choice)()(x_train, x_label, y_test, y_label)
        ground_label = y_label
        return eval(MC_choice)()(ground_label, pred_label)



def test3():
    test = Test(data_type='int', column=5, data_range=(1, 100), label_range=(0, 1), train_data=1000, test_data=100)('SVM', 'ACC')
    #print(test)
    return test

test3()