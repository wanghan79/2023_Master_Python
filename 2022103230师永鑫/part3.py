import torch
import random
import string
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
"""
采用类工厂设计模式实现作业2需求，以及相应的调用示例，主要考察点是应用创建模式搭建科学实验基本框架
"""

class MLFactory:
    def create_model(self, method):
        if method == 'SVM':
            return SVMModel()
        elif method == 'RF':
            return RFModel()
        elif method == 'CNN':
            return CNNModel()
        elif method == 'RNN':
            return RNNModel()
        else:
            print(f"Error: Invalid machine learning method '{method}'.")
            return None

    def create_metric(self, metric_func):
        if metric_func == 'ACC':
            return AccuracyMetric()
        elif metric_func == 'MCC':
            return MCCMetric()
        elif metric_func == 'F1':
            return F1Metric()
        elif metric_func == 'RC':
            return RecallMetric()
        else:
            print(f"Error: Invalid metric function '{metric_func}'.")
            return None


class Model:
    def process_data(self, data):
        raise NotImplementedError


class SVMModel(Model):
    def process_data(self, data):
        print("Using SVM method to process the data...")
        X = data  # Assume input data format is a 2D list, each sample as a sublist
        y = [0, 1, 0, 1]  # Assume binary classification problem, 0 and 1 represent two classes
        clf = svm.SVC()  # Create SVM classifier object
        clf.fit(X, y)  # Train the model using training data
        return clf


class RFModel(Model):
    def process_data(self, data):
        print("Using Random Forest method to process the data...")
        X = data  # Assume input data format is a 2D list, each sample as a sublist
        y = [0, 1, 0, 1]  # Assume binary classification problem, 0 and 1 represent two classes
        clf = RandomForestClassifier()  # Create Random Forest classifier object
        clf.fit(X, y)  # Train the model using training data
        return clf


class CNNModel(Model):
    def process_data(self, data):
        print("Using CNN method to process the data...")
        model = "CNN model"  # Placeholder, replace with actual CNN model
        return model


class RNNModel(Model):
    def process_data(self, data):
        print("Using RNN method to process the data...")
        model = "RNN model"  # Placeholder, replace with actual RNN model
        return model


class Metric:
    def calculate(self, data):
        raise NotImplementedError


class AccuracyMetric(Metric):
    def calculate(self, data):
        y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
        accuracy = (y_true == y_pred).mean()
        return accuracy


class MCCMetric(Metric):
    def calculate(self, data):
        y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
        tp = ((y_true == 1) & (y_pred == 1)).sum()
        tn = ((y_true == 0) & (y_pred == 0)).sum()
        fp = ((y_true == 0) & (y_pred == 1)).sum()
        fn = ((y_true == 1) & (y_pred == 0)).sum()
        mcc = (tp * tn - fp * fn) / ((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)) ** 0.5
        return mcc


class F1Metric(Metric):
    def calculate(self, data):
        y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
        tp = ((y_true == 1) & (y_pred == 1)).sum()
        fp = ((y_true == 0) & (y_pred == 1)).sum()
        fn = ((y_true == 1) & (y_pred == 0)).sum()
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        return f1


class RecallMetric(Metric):
    def calculate(self, data):
        y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
        tp = ((y_true == 1) & (y_pred == 1)).sum()
        fn = ((y_true == 1) & (y_pred == 0)).sum()
        recall = tp / (tp + fn)
        return recall


def data_sampling(length=1, dimension=1):
    result = []

    for _ in range(dimension):
        sample = []
        for _ in range(length):
            data_type = random.choice(['int', 'float', 'str'])
            if data_type == 'int':
                sample.append(random.randint(0, 100))
            elif data_type == 'float':
                sample.append(round(random.uniform(0, 1), 2))
            elif data_type == 'str':
                sample.append(''.join(random.choices(string.ascii_letters, k=5)))
        result.append(sample)

    return result


# 示例代码

# 创建工厂对象
factory = MLFactory()

# 创建模型实例
svm_model = factory.create_model('SVM')
rf_model = factory.create_model('RF')

# 创建评估指标实例
accuracy_metric = factory.create_metric('ACC')
mcc_metric = factory.create_metric('MCC')

# 生成数据
data = data_sampling(length=5, dimension=1)

# 使用模型处理数据
svm_result = svm_model.process_data(data)
rf_result = rf_model.process_data(data)

# 使用指标计算结果
accuracy = accuracy_metric.calculate(data)
mcc = mcc_metric.calculate(data)

# 输出结果
print(svm_result)
print(rf_result)
print(accuracy)
print(mcc)
def run():
    # 第三次作业的代码
    print("这是第三次作业")
run()  # 调用run()函数可以执行第二次作业的代码