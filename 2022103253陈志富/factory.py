from DataSampling import DataSampling
from MLPackage.MLModels import MLModels
from StandardPackage.Standards import Standards

class DataStructureGenerator:
    DataSampling


class MLMethodFactory:
    def create_ml_method(self, *args):
        print("Creating machine learning method:", args)
        MLModels(args)
        pass


class EvaluationMetricFactory:
    def create_evaluation_metric(self, *args):
        print("Creating evaluation metric:", *args)
        Standards(args)
        pass
