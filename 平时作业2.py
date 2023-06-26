import random

def mlMethod(method):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"{method} - {result}")
        return wrapper
    return decorator

def accuracyMetric(metric):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"{metric} - {result}")
        return wrapper
    return decorator

@mlMethod('SVM')
@accuracyMetric('ACC')
def svm_accuracy(data):
    return random.random()

@mlMethod('RF')
@accuracyMetric('MCC')
def rf_mcc(data):
    return random.random()

@mlMethod('CNN')
@accuracyMetric('F1')
def cnn_f1(data):
    return random.random()

@mlMethod('RNN')
@accuracyMetric('RECALL')
def rnn_recall(data):
    return random.random()

# 调用示例
svm_accuracy('data')
rf_mcc('data')
cnn_f1('data')
rnn_recall('data')
