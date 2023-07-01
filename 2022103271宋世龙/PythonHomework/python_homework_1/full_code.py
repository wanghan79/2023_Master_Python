# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/12
@Auth    : song
@File    : full_code.py
@IDE     : PyCharm
@Edition : 001
@Describe:
平时作业2：
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。
主要考察点是带参数修饰器的使用，具体要求如下：
1.	修饰器类型不限，可以是函数修饰器或类修饰器；
2.	实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""

# test1
# def my_dec(org_func):
#     def wrapper():
#         print('原方法执行前')
#         org_func()
#         print('原方法执行后')
#
#     return wrapper


# @my_dec
# def dec_test():
#     print('原方法')


# dec_test()


# test2
# def try_one_try(func):
#     def wrapper(**kwargs):
#         result = func(**kwargs)
#         result = result[0]
#         result[:20] = [0] * 20  # 将列表前20个元素置零
#         return result

#     return wrapper


import numpy

from functools import wraps

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef, recall_score, f1_score

from python_homework_1.task_data_sampling import data_sampling as get_data, rand_integer as get_label


class MyMetrics:
    def __init__(self, *args) -> None:
        self._metrics = args

    def __call__(self, func) -> wraps:
        metrics = self._metrics

        @wraps(func)
        def wrapper(*args, **kwargs) -> func:
            models, pred_labels, true_labels = func(*args, **kwargs)

            # print(models)
            # print(pred_labels)
            # print(true_labels)

            pred_result = list()
            pred_accuracy = dict()

            for lab in pred_labels:
                pred_rlt = dict()

                for mtr in metrics:
                    if mtr == 'acc':
                        pred_rlt[mtr] = self.acc(true_labels, lab)
                    elif mtr == 'mcc':
                        pred_rlt[mtr] = self.mcc(true_labels, lab)
                    elif mtr == 'recall':
                        pred_rlt[mtr] = self.recall(true_labels, lab)
                    elif mtr == 'f1_score':
                        pred_rlt[mtr] = self.f1_score(true_labels, lab)
                    else:
                        return 'Sorry, there is an unsupported metric in your input. Stay tuned'

                pred_result.append(pred_rlt)

            for j, mod in enumerate(models):
                pred_accuracy[mod] = pred_result[j]
            return pred_accuracy

        return wrapper

    @staticmethod
    def acc(y_true, y_pred) -> float:
        """
        评价指标 accuracy
        :param y_true: 真实标签
        :param y_pred: 预测标签
        :return:
        """
        return accuracy_score(y_true, y_pred)

    @staticmethod
    def mcc(y_true, y_pred) -> float:
        return matthews_corrcoef(y_true, y_pred)

    @staticmethod
    def recall(y_true, y_pred) -> float:
        return recall_score(y_true, y_pred, average='micro')

    @staticmethod
    def f1_score(y_true, y_pred) -> float:
        return f1_score(y_true, y_pred, average='micro')


class MyModels:
    def __init__(self, *args) -> None:
        self._model = args

    def __call__(self, func) -> wraps:
        models = self._model

        @wraps(func)
        def wrapper(*args, **kwargs) -> func:
            x_trn, x_lab, y_tst, y_lab = func(*args, **kwargs)
            pred_labels = list()
            for mod in models:
                if mod == 'svm':
                    label = self.svm(x_trn, x_lab, y_tst, y_lab)
                elif mod == 'rf':
                    label = self.rf(x_trn, x_lab, y_tst, y_lab)
                elif mod == 'cnn':
                    label = self.cnn()
                elif mod == 'rnn':
                    label = self.rnn()
                else:
                    return 'Sorry, there is an unsupported model in your input. Stay tuned'
                pred_labels.append(label)
            return models, pred_labels, y_lab

        return wrapper

    def svm(self, x_train, x_label, y_test, y_label) -> list:
        module = svm.SVC(kernel='linear')

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)

    def rf(self, x_train, x_label, y_test, y_label) -> list:
        module = RandomForestClassifier()

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)

    def cnn(self) -> list:
        return list()

    def rnn(self) -> list:
        return list()


# 使用由'模型类'和'评价指标类'构建的两个修饰器修饰'随机数据结构生成函数'
@MyMetrics('acc', 'mcc', 'recall', 'f1_score')
@MyModels('svm', 'rf')
def data_sampling(**kwargs) -> numpy.ndarray or list:
    data_type = kwargs['data_type']
    column = kwargs['column']
    train_set_num = kwargs['train_set_num']
    test_set_num = kwargs['test_set_num']
    data_range = kwargs['data_range']
    label_range = kwargs['label_range']
    x_elem_num = train_set_num * column
    y_elem_num = test_set_num * column

    x_train = get_data(data_type=data_type, num=x_elem_num, row=train_set_num, column=column, data_range=data_range)
    x_label = get_label(train_set_num, label_range)

    y_test = get_data(data_type=data_type, num=y_elem_num, row=test_set_num, column=column, data_range=data_range)
    y_label = get_label(test_set_num, label_range)

    return x_train, x_label, y_test, y_label


if __name__ == '__main__':
    # 测试
    # print(data_sampling(data_type='int', column=6, train_set_num=1000, test_set_num=20, data_range=(1, 100),
    #                     label_range=(0, 1)))
    pass
