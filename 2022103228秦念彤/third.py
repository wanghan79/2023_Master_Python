import random
import string
class LearningMethodFactory:
    def get_learning_method(self, method):
        if method == "SVM":
            return SVM()
        elif method == "RF":
            return RF()
        elif method == "CNN":
            return CNN()
        elif method == "RNN":
            return RNN()


class EvaluationMetricFactory:
    def get_evaluation_metric(self, metric):
        if metric == "ACC":
            return ACC()
        elif metric == "MCC":
            return MCC()
        elif metric == "F1":
            return F1()
        elif metric == "RECALL":
            return RECALL()


class SVM:
    pass


class RF:
    pass


class CNN:
    pass


class RNN:
    pass


class ACC:
    pass


class MCC:
    pass


class F1:
    pass


class RECALL:
    pass


learning_method_factory = LearningMethodFactory()
evaluation_metric_factory = EvaluationMetricFactory()

methods = ["SVM", "RF", "CNN", "RNN"]
metrics = ["ACC", "MCC", "F1", "RECALL"]

for method in methods:
    learning_method = learning_method_factory.get_learning_method(method)
    print(learning_method)

for metric in metrics:
    evaluation_metric = evaluation_metric_factory.get_evaluation_metric(metric)
    print(evaluation_metric)