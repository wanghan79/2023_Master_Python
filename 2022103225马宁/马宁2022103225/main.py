import random


def dataSampling(**kwargs):
    result = []
    for datatype, datarange in kwargs.items():
        if datatype == 'int':
            result.append(random.randint(*datarange))
        elif datatype == 'float':
            result.append(random.uniform(*datarange))
        elif datatype == 'str':
            length = random.randint(*datarange)
            result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length)))
    return result


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


class MLFactory:
    def __init__(self, method):
        self.method = method

    def mlMethod(self, func):
        def wrapper(*args):
            result = func(*args)
            print(f"{self.method} - {result}")

        return wrapper

    def accuracyMetric(self, func):
        def wrapper(*args):
            result = func(*args)
            print(f"ACC - {result}")

        return wrapper


def run_homework_1():
    result = dataSampling(int=(1, 100), float=(0, 1), str=(5, 10))
    print(result)


def run_homework_2():
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

    svm_accuracy('data')
    rf_mcc('data')
    cnn_f1('data')
    rnn_recall('data')


def run_homework_3():
    class MLFactory:
        def __init__(self, method):
            self.method = method

        def __call__(self, cls):
            setattr(cls, 'mlMethod', self.mlMethod)
            setattr(cls, 'accuracyMetric', self.accuracyMetric)
            return cls

        @staticmethod
        def mlMethod(func):
            def wrapper(self, *args):
                result = func(self, *args)
                print(f"{type(self).__name__}.{func.__name__} - {result}")

            return wrapper

        @staticmethod
        def accuracyMetric(func):
            def wrapper(self, *args):
                result = func(self, *args)
                print(f"ACC - {result}")

            return wrapper

    @MLFactory('SVM')
    class SVM:
        @MLFactory.mlMethod
        def accuracy(self, data):
            return random.random()

    @MLFactory('RF')
    class RF:
        @MLFactory.mlMethod
        def mcc(self, data):
            return random.random()

    @MLFactory('CNN')
    class CNN:
        @MLFactory.mlMethod
        def f1(self, data):
            return random.random()

    @MLFactory('RNN')
    class RNN:
        @MLFactory.mlMethod
        def recall(self, data):
            return random.random()

    svm = SVM()
    svm.accuracy('data')

    rf = RF()
    rf.mcc('data')

    cnn = CNN()
    cnn.f1('data')

    rnn = RNN()
    rnn.recall('data')


if __name__ == '__main__':
    while True:
        print("请输入要展示的作业号（1、2或3），输入'q'退出：")
        choice = input()

        if choice == '1':
            print("运行平时作业1示例：")
            run_homework_1()
        elif choice == '2':
            print("运行平时作业2示例：")
            run_homework_2()
        elif choice == '3':
            print("运行平时作业3示例：")
            run_homework_3()
        elif choice == 'q':
            print("退出程序。")
            break
        else:
            print("无效的选择，请重新输入。")
