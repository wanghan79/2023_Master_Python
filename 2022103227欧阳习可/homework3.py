import random

# 机器学习方法基类
class MLMethod:
    def operate(self):
        pass

# SVM机器学习方法类
class SVM(MLMethod):
    def operate(self):
        print("执行SVM操作")

# Random Forest机器学习方法类
class RandomForest(MLMethod):
    def operate(self):
        print("执行Random Forest操作")

# CNN机器学习方法类
class CNN(MLMethod):
    def operate(self):
        print("执行CNN操作")

# RNN机器学习方法类
class RNN(MLMethod):
    def operate(self):
        print("执行RNN操作")

# 验证指标基类
class Metric:
    def compute(self):
        pass

# 准确率指标类
class Accuracy(Metric):
    def compute(self):
        print("计算准确率")

# MCC指标类
class MCC(Metric):
    def compute(self):
        print("计算MCC")

# F1指标类
class F1(Metric):
    def compute(self):
        print("计算F1值")

# 召回率指标类
class Recall(Metric):
    def compute(self):
        print("计算召回率")

# 类工厂
class ExperimentFactory:
    def create_ml_method(self, ml_method_name):
        raise NotImplementedError

    def create_metric(self, metric_name):
        raise NotImplementedError

# 具体实验类工厂
class ConcreteExperimentFactory(ExperimentFactory):
    def create_ml_method(self, ml_method_name):
        if ml_method_name == 'SVM':
            return SVM()
        elif ml_method_name == 'RF':
            return RandomForest()
        elif ml_method_name == 'CNN':
            return CNN()
        elif ml_method_name == 'RNN':
            return RNN()
        else:
            raise ValueError("未知的机器学习方法")

    def create_metric(self, metric_name):
        if metric_name == 'ACC':
            return Accuracy()
        elif metric_name == 'MCC':
            return MCC()
        elif metric_name == 'F1':
            return F1()
        elif metric_name == 'RECALL':
            return Recall()
        else:
            raise ValueError("未知的验证指标")

# 随机数据结构生成函数
def generate_random_data_structure(num_samples):
    data = []
    for _ in range(num_samples):
        data.append(random.randint(0, 10))
    return sum(data)

models = ['SVM','RF','CNN','RNN']
metrics = ['ACC','MCC','F1','RECALL']
# 调用示例
experiment_factory = ConcreteExperimentFactory()

ml_method = experiment_factory.create_ml_method(random.choice(models))
metric = experiment_factory.create_metric(random.choice(metrics))

ml_method.operate()
metric.compute()

data = generate_random_data_structure(5)
print(data)
