import random
import string
class LMF:
    def get_L_M(self, method):
        if method == "SVM":
            return SVM()
        elif method == "RF":
            return RF()
        elif method == "CNN":
            return CNN()
        elif method == "RNN":
            return RNN()

class EMF:
    def get_E_M(self, metric):
        if metric == "ACC":
            return ACC()
        elif metric == "MCC":
            return MCC()
        elif metric == "F1":
            return F1()
        elif metric == "RECALL":
            return RECALL()

class SVM: pass
class RF: pass
class CNN: pass
class RNN: pass
class ACC: pass
class MCC: pass
class F1: pass
class RECALL: pass

L_M_F = LMF()
E_M_F = EMF()

methods = ["SVM", "RF", "CNN", "RNN"]
metrics = ["ACC", "MCC", "F1", "RECALL"]

for method in methods:
    L_M = L_M_F.get_learning_method(method)
    print(L_M)

for metric in metrics:
    E_M = E_M_F.get_evaluation_metric(metric)
    print(E_M)