
class OriginalClass:
    def __init__(self):
        self.attribute = None

    def operation(self):
        print("随机值为:", self.attribute)


def svm(decorated_class):
    class SVM:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("SVM finished")

    return SVM

def rf(decorated_class):
    class RF:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("RF finished")

    return RF

def cnn(decorated_class):
    class CNN:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("CNN finished")

    return CNN

def rnn(decorated_class):
    class RNN:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("RNN finished")

    return RNN


def acc(decorated_class):
    class ACC:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("ACC finished")

    return ACC

def mcc(decorated_class):
    class MCC:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("MCC finished")

    return MCC

def f1(decorated_class):
    class F1:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("F1 finished")

    return F1

def recall(decorated_class):
    class RECALL:
        def __init__(self, decorated):
            self.decorated = decorated

        def operation(self):
            self.decorated.operation()
            print("ACC finished")

    return RECALL

def solve(*args):
    str1 = args[0]
    str2 = args[1]
    ob = args[2]
    result = None

    original_obj = OriginalClass()
    original_obj.attribute = ob

    decorated_class_1 = decorated_obj_1 = None
    decorated_class_2 = decorated_obj_2 = None

    if str1 == "svm":
        decorated_class_1 = svm(OriginalClass)
    elif str1 == "rf":
        decorated_class_1 = rf(OriginalClass)
    elif str1 == "cnn":
        decorated_class_1 = cnn(OriginalClass)
    elif str1 == "rnn":
        decorated_class_1 = rnn(OriginalClass)

    decorated_obj_1 = decorated_class_1(original_obj)

    if str2 == "acc":
        decorated_class_2 = acc(decorated_class_1)
    elif str2 == "mcc":
        decorated_class_2 = mcc(decorated_class_1)
    elif str2 == "f1":
        decorated_class_2 = f1(decorated_class_1)
    elif str2 == "recall":
        decorated_class_2 = recall(decorated_class_1)

    decorated_obj_2 = decorated_class_2(decorated_obj_1)
    decorated_obj_2.operation()