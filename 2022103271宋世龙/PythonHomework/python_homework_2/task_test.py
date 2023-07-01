# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/12
@Auth    : song
@File    : task_test.py
@IDE     : PyCharm
@Edition : 001
@Describe: hhh
"""
from python_homework_2.task_data_sampling import rand_integer as get_label
from python_homework_2.task_data_sampling import data_sampling as get_data
from python_homework_2.task_metrics import ACC, MCC, Recall, F1Score
from python_homework_2.task_models import SVM, RF, CNN, RNN


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
    print('Test1 prediction accuracy: ',
          TaskTest(data_type='int', column=6, train_set_num=1000, test_set_num=20, data_range=(1, 100),
                   label_range=(0, 1))('SVM', 'ACC'))
    print('Test2 prediction accuracy: ',
          TaskTest(data_type='int', column=6, train_set_num=1000, test_set_num=20, data_range=(1, 100),
                   label_range=(0, 1))('RF', 'Recall'))
    # pass
