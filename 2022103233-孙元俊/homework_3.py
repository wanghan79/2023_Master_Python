import random
import string
from sklearn import svm, ensemble
from sklearn.metrics import accuracy_score, matthews_corrcoef, f1_score, recall_score


class DataSampling:
    def __init__(self, *args):
        self.data_types = args

    def __call__(self, func):
        def wrapper():
            result = []
            for data_type, data_num in self.data_types:
                if data_type == 'int':
                    result.extend(random.sample(range(1, 100), data_num))
                elif data_type == 'float':
                    result.extend([random.uniform(1, 100) for _ in range(data_num)])
                elif data_type == 'str':
                    result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 50))) for _ in range(data_num)])
            return func(result)
        return wrapper


class MLMethod:
    def __init__(self, methods):
        self.method = methods.upper()

    def __call__(self, func):
        def wrapper(data):
            if self.method == 'SVM':
                print("********************\n使用SVM支持向量机!")
            elif self.method == 'RF':
                print("********************\n使用RF随机森林!")
            elif self.method == 'CNN':
                print("********************\n使用CNN!")
            elif self.method == 'RNN':
                print("********************\n使用RNN!")
            return func(data)
        return wrapper


class AccuracyMetric:
    def __init__(self, metric):
        self.metric = metric.upper()

    def __call__(self, func):
        def wrapper(data):
            if self.metric == 'ACC':
                print("********************\n使用ACC精度验证!\n********************")
            elif self.metric == 'MCC':
                print("********************\n使用MCC精度验证!\n********************")
            elif self.metric == 'F1':
                print("********************\n使用F1精度验证!\n********************")
            elif self.metric == 'RECALL':
                print("********************\n使用RECALL精度验证!\n********************")
            return func(data)
        return wrapper


a, b, c = map(int, input("请分别输入需要产生int, float, str的个数：").split())
method, acc = input("请输入深度学习方法（SVM, RF, CNN, RNN）和精度验证(ACC, MCC, F1, RECALL):").split()


# 调用示例
@DataSampling(('int', a), ('float', b), ('str', c))
@MLMethod(method)
@AccuracyMetric(acc)
def processRandomData(data):
    print("随机数据结构:", data)


processRandomData()
