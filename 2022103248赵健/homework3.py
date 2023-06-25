import random

class DataFactory:
    def createData(self):
        # 创建数据的逻辑
        data = random.randint(1, 100)
        return data

class ModelFactory:
    def createModel(self):
        # 创建模型的逻辑
        model = "模型A"
        return model

class Experiment:
    def __init__(self, dataFactory, modelFactory):
        self.dataFactory = dataFactory
        self.modelFactory = modelFactory

    def run(self):
        # 执行实验的逻辑
        data = self.dataFactory.createData()
        model = self.modelFactory.createModel()
        print("数据：", data)
        print("模型：", model)

def main():
    dataFactory = DataFactory()
    modelFactory = ModelFactory()
    experiment = Experiment(dataFactory, modelFactory)
    experiment.run()

if __name__ == "__main__":
    main()
