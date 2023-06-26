import random
from task1 import dataSampling
from task2 import mlMethod,accuracyMetric
from task3 import MLFactory,SVM,RF,CNN,RNN

def run_task1():
    result = dataSampling(int=(1, 100), float=(0, 1), str=(5, 10))
    print(result)

def run_task2():
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
    svm_accuracy(256)
    rf_mcc(256)
    cnn_f1(256)
    rnn_recall(256)

def run_task3():
    svm = SVM()
    svm.accuracy(256)

    rf = RF()
    rf.mcc(256)

    cnn = CNN()
    cnn.f1(256)

    rnn = RNN()
    rnn.recall(256)


def run(number):
    if number == 1:
        run_task1()
    elif number == 2:
        run_task2()
    elif number == 3:
        run_task3()



if __name__ == "__main__":
    while True:
        try:
            number = int(input("请输入作业号(1/2/3): "))
            run(number)
            break
        except ValueError:
            print("输入有误，请确认作业号后重新运行！")