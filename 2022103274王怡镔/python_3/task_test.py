# -*- coding: utf-8 -*-

from python_1.rand_project import rand_integer as get_label
from python_1.rand_project import data_sampling as get_data
from python_3.task_metrics import *
from python_3.task_models import *
from python_3.task_data_sampling import TaskTest


def test():
    # 测试
    return TaskTest(data_type='int', column=6, train_set_num=1000, test_set_num=20, data_range=(1, 100),
                   label_range=(0, 1))('SVM', 'ACC')


# test()
