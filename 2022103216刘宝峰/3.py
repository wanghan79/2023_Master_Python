import random
# 作业3
class DataFactory:
    def createData(self):
        data = random.randint(1, 100)
        return data

class ModelFactory:
    def createModel(self):
        model = "A"
        return model

class Experiment:
    def __init__(self, dataFactory, modelFactory):
        self.dataFactory = dataFactory
        self.modelFactory = modelFactory

    def run(self):
        data = self.dataFactory.createData()
        model = self.modelFactory.createModel()
        print(data)
        print(model)

def main():
    dataFactory = DataFactory()
    modelFactory = ModelFactory()
    experiment = Experiment(dataFactory, modelFactory)
    experiment.run()

if __name__ == "__main__":
    main()
