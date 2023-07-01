# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/12
@Auth    : song
@File    : task_metrics.py
@IDE     : PyCharm
@Edition : 001
@Describe: hhh
"""
from functools import wraps

from sklearn.metrics import accuracy_score, matthews_corrcoef, recall_score, f1_score


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