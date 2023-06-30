import random

def mlMethod(func):
    def wrapper(*args):
        print(f"Applying {func.__name__} method...")
        result = func(*args)
        return result
    return wrapper

def evalMetric(func):
    def wrapper(*args):
        print(f"Evaluating with {func.__name__} metric...")
        result = func(*args)
        return result
    return wrapper

@mlMethod
def svm():
    print("SVM method")

@mlMethod
def rf():
    print("RF method")

@mlMethod
def cnn():
    print("CNN method")

@mlMethod
def rnn():
    print("RNN method")

@evalMetric
def acc():
    print("ACC metric")

@evalMetric
def mcc():
    print("MCC metric")

@evalMetric
def f1():
    print("F1 metric")

@evalMetric
def recall():
    print("RECALL metric")

if __name__=='__main__':
    svm()
    acc()
