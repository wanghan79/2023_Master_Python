# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/12
@Auth    : song
@File    : full_code.py
@IDE     : PyCharm
@Edition : 001
@Describe:
平时作业3：
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架。
"""
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef, recall_score, f1_score

from python_homework_2.task_data_sampling import rand_integer as get_label
from python_homework_2.task_data_sampling import data_sampling as get_data


class MLFactory:
    def __init__(self, **kwargs) -> None:
        pass

    def __call__(self, *args, **kwargs) -> None:
        pass


class SVM(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        module = svm.SVC(kernel='linear')

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)


class RF(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        module = RandomForestClassifier()

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)


class CNN(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        return list()


class RNN(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        return list()


class MCFactory:
    def __init__(self, **kwargs) -> None:
        pass

    def __call__(self, *args, **kwargs) -> None:
        pass


class ACC(MCFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, true_label, pred_label) -> float:
        return accuracy_score(true_label, pred_label)


class MCC(MCFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, true_label, pred_label) -> float:
        return matthews_corrcoef(true_label, pred_label)


class Recall(MCFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, true_label, pred_label) -> float:
        return recall_score(true_label, pred_label, average='micro')


class F1Score(MCFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, true_label, pred_label) -> float:
        return f1_score(true_label, pred_label, average='micro')


class TaskTest:
    def __init__(self, **kwargs) -> None:
        data_type = kwargs['data_type']
        column = kwargs['column']
        train_set_num = kwargs['train_set_num']
        test_set_num = kwargs['test_set_num']
        data_range = kwargs['data_range']
        label_range = kwargs['label_range']
        x_elem_num = train_set_num * column
        y_elem_num = test_set_num * column

        self.x_train = get_data(data_type=data_type, num=x_elem_num, row=train_set_num, column=column,
                                data_range=data_range)
        self.x_label = get_label(train_set_num, label_range)

        self.y_test = get_data(data_type=data_type, num=y_elem_num, row=test_set_num, column=column,
                               data_range=data_range)
        self.y_label = get_label(test_set_num, label_range)

    def __call__(self, ml_name, mc_name) -> float:
        x_train = self.x_train
        x_label = self.x_label
        y_test = self.y_test
        y_label = self.y_label

        pred_label = eval(ml_name)()(x_train, x_label, y_test, y_label)
        true_label = y_label
        return eval(mc_name)()(true_label, pred_label)


if __name__ == '__main__':
    # 测试
    # print('prediction accuracy: ',
    #       TaskTest(data_type='int', column=6, train_set_num=1000, test_set_num=20, data_range=(1, 100),
    #                label_range=(0, 1))('SVM', 'ACC'))
    pass
