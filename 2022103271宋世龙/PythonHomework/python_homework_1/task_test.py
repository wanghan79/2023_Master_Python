# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/12
@Auth    : song
@File    : task_test.py
@IDE     : PyCharm
@Edition : 001
@Describe: hhh
"""
import numpy

from python_homework_1.task_data_sampling import data_sampling as get_data, rand_integer as get_label
from python_homework_1.task_models import MyModels
from python_homework_1.task_metrics import MyMetrics


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
    print(data_sampling(data_type='int', column=6, train_set_num=1000, test_set_num=20, data_range=(1, 100),
                        label_range=(0, 1)))
    # pass
