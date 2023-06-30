# -*- coding: utf-8 -*-

from sklearn.metrics import accuracy_score, matthews_corrcoef, recall_score, f1_score


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

