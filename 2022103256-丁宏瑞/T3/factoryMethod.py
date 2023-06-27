'''
平时作业3：
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架
'''
class RNN:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 9


class CNN:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 2


class RF:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 29


class SVM:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 92


'''
工厂方法模式
'''


class FactoryML():
    def __init__(self):
        self.MLs = []

    def getML(self):
        return self.MLs

    def addML(self, ML):
        self.MLs.append(ML)


# 读取txt文件，将字符添加到列表l中，按行读取
filename = 'T3/Config.txt'
list = []
with open(filename, 'r') as f:
    line = f.readline()
    while line != "":
        list.append(line.strip())
        line = f.readline()

# 创建工厂实例ML，每个模型的输入数据都是2023
ML = FactoryML()

for i in list:
    ML.addML(eval(i)(1992))

for i in ML.getML():
    print(i.prediction())
