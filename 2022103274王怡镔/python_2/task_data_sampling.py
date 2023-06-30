# -*- coding: utf-8 -*-

import numpy
from python_2.task_models import MyModels
from python_2.task_metrics import MyMetrics
from python_1.rand_project import data_sampling as get_data
from python_1.rand_data import rand_integer as get_label


@MyMetrics('acc', 'mcc', 'recall')
@MyModels('rf')
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

