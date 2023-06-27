'''
平时作业3：
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架
'''
import random


class RNN:
    def __init__(self, data):
        self.data = data

    def predict(self):
        return self.data + random.random() * 10


class CNN:
    def __init__(self, data):
        self.data = data

    def predict(self):
        return self.data + random.random() * 10


class RF:
    def __init__(self, data):
        self.data = data

    def predict(self):
        return self.data + random.random() * 10


class SVM:
    def __init__(self, data):
        self.data = data

    def predict(self):
        return self.data + random.random() * 10


# 工厂方法模式
class FactoryML():
    def __init__(self):
        self.MLs = []

    def getML(self):
        return self.MLs

    def addML(self, name, ML):
        self.MLs.append({"name": name, "ML": ML})


# 读取文件，将字符串添加到列表modelList中，按行读取
filename = 'homework3/list.txt'
modelList = []
with open(filename, 'r') as f:
    line = f.readline()
    while line != "":
        modelList.append(line.strip())
        line = f.readline()

# 创建工厂实例ML，每个模型的输入数据都是1024
ML = FactoryML()

for i in modelList:
    ML.addML(i, eval(i)(1024))

for i in ML.getML():
    print(i["name"], i["ML"].predict())
