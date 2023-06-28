class RNN:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 1


class CNN:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 2


class RF:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 3


class SVM:
    def __init__(self, data):
        self.data = data

    def prediction(self):
        return self.data + 4


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
filename = 'E:\python_homework\H3\config.txt'
l = []
with open(filename, 'r') as f:
    line = f.readline()
    while line != "":
        l.append(line.strip())
        line = f.readline()

# 创建工厂实例ML，每个模型的输入数据都是2023
ML = FactoryML()

for i in l:
    ML.addML(eval(i)(2023))

for i in ML.getML():
    print(i.prediction())
