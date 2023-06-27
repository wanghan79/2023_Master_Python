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

    def addML(self, name, ML):
        self.MLs.append({"name": name, "ML": ML})


list = ['SVM', 'RF', 'CNN', 'RNN']
ML = FactoryML()

for i in list:
    ML.addML(i, eval(i)(1))

print("FactoryML begin form 1:")
for i in ML.getML():
    print(i["name"], i["ML"].prediction())
