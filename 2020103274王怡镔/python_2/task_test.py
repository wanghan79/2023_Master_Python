# -*- coding: utf-8 -*-

from python_2.task_data_sampling import data_sampling


def test():
    # 测试
    return data_sampling(data_type='int', column=4, train_set_num=10000, test_set_num=40, data_range=(1, 1000),
                        label_range=(0, 1))
