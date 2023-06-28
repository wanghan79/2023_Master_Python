
def svm(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator SVM finished")
        return result
    return wrapper

def rf(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator RF finished")
        return result
    return wrapper

def cnn(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator CNN finished")
        return result
    return wrapper

def rnn(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator RNN finished")
        return result
    return wrapper

def acc(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator ACC finished")
        return result
    return wrapper

def mcc(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator MCC finished")
        return result
    return wrapper

def f1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator F1 finished")
        return result
    return wrapper

def recall(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # 调用被修饰的修饰器
        print("Decorator RECALL finished")
        return result
    return wrapper

@acc
@svm
def svm_acc(ob):
    print("随机值为：", ob)

@mcc
@svm
def svm_mcc(ob):
    print("随机值为：", ob)

@f1
@svm
def svm_f1(ob):
    print("随机值为：", ob)

@recall
@svm
def svm_recall(ob):
    print("随机值为：", ob)

@acc
@rf
def rf_acc(ob):
    print("随机值为：", ob)


@mcc
@rf
def rf_mcc(ob):
    print("随机值为：", ob)


@f1
@rf
def rf_f1(ob):
    print("随机值为：", ob)


@recall
@rf
def rf_recall(ob):
    print("随机值为：", ob)


@acc
@cnn
def cnn_acc(ob):
    print("随机值为：", ob)


@mcc
@cnn
def cnn_mcc(ob):
    print("随机值为：", ob)


@f1
@cnn
def cnn_f1(ob):
    print("随机值为：", ob)


@recall
@cnn
def cnn_recall(ob):
    print("随机值为：", ob)

@acc
@rnn
def rnn_acc(ob):
    print("随机值为：", ob)


@mcc
@rnn
def rnn_mcc(ob):
    print("随机值为：", ob)


@f1
@rnn
def rnn_f1(ob):
    print("随机值为：", ob)


@recall
@rnn
def rnn_recall(ob):
    print("随机值为：", ob)

def solve(*args):
    str1 = args[0]
    str2 = args[1]
    ob = args[2]
    if str1== "svm" and str2== "acc":
        svm_acc(ob)
    elif str1== "svm" and str2== "mcc":
        svm_mcc(ob)
    elif str1 == "svm" and str2 == "f1":
        svm_f1(ob)
    elif str1 == "svm" and str2 == "recall":
        svm_recall(ob)
    elif str1== "rf" and str2== "acc":
        rf_acc(ob)
    elif str1== "rf" and str2== "mcc":
        rf_mcc(ob)
    elif str1 == "rf" and str2 == "f1":
        rf_f1(ob)
    elif str1 == "rf" and str2 == "recall":
        rf_recall(ob)
    elif str1== "cnn" and str2== "acc":
        cnn_acc(ob)
    elif str1== "cnn" and str2== "mcc":
        cnn_mcc(ob)
    elif str1 == "cnn" and str2 == "f1":
        cnn_f1(ob)
    elif str1 == "cnn" and str2 == "recall":
        cnn_recall(ob)
    elif str1== "rnn" and str2== "acc":
        rnn_acc(ob)
    elif str1== "rnn" and str2== "mcc":
        rnn_mcc(ob)
    elif str1 == "rnn" and str2 == "f1":
        rnn_f1(ob)
    elif str1 == "rnn" and str2 == "recall":
        rnn_recall(ob)


