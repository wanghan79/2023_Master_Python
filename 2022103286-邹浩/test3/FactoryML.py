from CNN import CNN
from RF import RF
from RNN import RNN
from SVM import SVM

data = 1
class FactoryML():
    def __init__(self):
        self.MLS = []

    def getML(self):
        return self.MLs

    def addML(self, ML):
        self.MLs.append(ML)

filename = 'config.txt'
result = []
f = open(filename, 'r')
fn = f.readlines()

RM = FactoryML()
for i in result:
    # if i.strip() == 'SVM':
    #     model = SVM(data)
    # if i.strip() == 'CNN':
    #     model = CNN(data)
    # if i.strip() == 'RF':
    #     model = RF(data)
    # if i.strip() == 'RNN':
    #     model = RNN(data)
    # eval转换字符串为类名
    model = eval(i)(data)

    RM.addML(model)
#return result

# print(FactoryML('config.txt'))

for x in RM.getML():
    print(x.prediction())