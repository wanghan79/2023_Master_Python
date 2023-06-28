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

class FactoryML():
    def __init__(self):
        self.MLs = []

    def getML(self):
        return self.MLs

    def addML(self, ML):
        self.MLs.append(ML)
filename = ':\python\third\txt.txt'
l = []
with open(filename, 'r') as f:
    line = f.readline()
    while line != "":
        l.append(line.strip())
        line = f.readline()
ML = FactoryML()

for i in l:
    ML.addML(eval(i)(2023))

for i in ML.getML():
    print(i.prediction())
