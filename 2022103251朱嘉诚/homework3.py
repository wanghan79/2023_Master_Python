import random
import string
from abc import ABC, abstractmethod

# 随机数据生成函数
def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, tuple) and len(value) == 2:
            dataType = value[0]
            dataNumber = value[1]
            if dataType == int:
                result[key] = random.sample(range(1, 101), dataNumber)
            elif dataType == float:
                result[key] = [round(random.uniform(1.0, 100.0),2) for i in range(dataNumber)]
            elif dataType == str:
                result[key] = [''.join(random.sample(string.ascii_letters + string.digits, 8)) for i in range(dataNumber)]
    return result

# 分类器抽象基类
class Classifier(ABC):
    @abstractmethod #@abstractmethod为抽象方法，含@abstractmethod的类不能被实例化，继承了含@abstractmethod方法的子类必须复写所有@abstractmethod装饰的方法。类似于Java的抽象
    def train(self, data):
        pass
    @abstractmethod
    def evaluate(self):
        pass

# SVM分类器
class SVMClassifier(Classifier):
    def __init__(self):
        print("使用SVM分类器进行训练")
    def train(self, data):
        # 进行SVM分类器训练
        pass
    def evaluate(self):
        print("ACC: 0.85")
        print("MCC: 0.5")
        print("F1: 0.67")
        print("RECALL: 0.75")

# 随机森林分类器
class RFClassifier(Classifier):
    def __init__(self):
        print("使用随机森林分类器进行训练")
    def train(self, data):
        # 进行随机森林分类器训练
        pass
    def evaluate(self):
        print("ACC: 0.87")
        print("MCC: 0.52")
        print("F1: 0.69")
        print("RECALL: 0.77")

# 卷积神经网络分类器
class CNNClassifier(Classifier):
    def __init__(self):
        print("使用卷积神经网络进行训练")
    def train(self, data):
        # 进行卷积神经网络训练
        pass
    def evaluate(self):
        print("ACC: 0.88")
        print("MCC: 0.56")
        print("F1: 0.71")
        print("RECALL: 0.78")

# 循环神经网络分类器
class RNNClassifier(Classifier):
    def __init__(self):
        print("使用循环神经网络进行训练")
    def train(self, data):
        # 进行循环神经网络训练
        pass
    def evaluate(self):
        print("ACC: 0.86")
        print("MCC: 0.53")
        print("F1: 0.68")
        print("RECALL: 0.76")

# 分类器工厂类
class ClassifierFactory:
    @staticmethod
    def create(classifierName):
        if classifierName == "SVM":
            return SVMClassifier()
        elif classifierName == "RF":
            return RFClassifier()
        elif classifierName == "CNN":
            return CNNClassifier()
        elif classifierName == "RNN":
            return RNNClassifier()
        else:
            return None

# 主程序
def main():
    # 生成随机数据
    data = dataSampling(intdata= (int, 10), floatdata= (float, 5), strdata= (str, 2))

    # 创建分类器
    classifier = ClassifierFactory.create("RF")

    # 训练分类器并输出评估结果
    classifier.train(data)
    classifier.evaluate()

if __name__ == "__main__":
    main()

# 生成随机数据
data = dataSampling(intdata= (int, 10), floatdata= (float, 5), strdata= (str, 2))

# 创建分类器
classifier = ClassifierFactory.create("RF")

# 训练分类器并输出评估结果
classifier.train(data)
classifier.evaluate()