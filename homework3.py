import random
import string

from homework1 import dataSampling

# 不同机器学习方法的预测函数模拟
def svm_predict():
    return [random.randint(0, 1) for i in range(10)]


def rf_predict():
    return [random.randint(0, 1) for i in range(10)]


def cnn_predict():
    return [random.randint(0, 1) for i in range(10)]


def rnn_predict():
    return [random.randint(0, 1) for i in range(10)]


# 不同评价指标的计算函数模拟
def acc(y_true, y_pred):
    accuracy = sum([1 for i in range(len(y_true)) if y_true[i] == y_pred[i]]) / len(y_true)
    return accuracy


def mcc(y_true, y_pred):
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp += 1
        elif y_true[i] == 0 and y_pred[i] == 0:
            tn += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            fp += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    denominator = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    numerator = (tp * tn - fp * fn)
    mcc = numerator / denominator ** 0.5 if denominator != 0 else 0
    return mcc


def f1(y_true, y_pred):
    precision, recall = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i] and y_true[i] == 1:
            precision += 1
            recall += 1
        elif y_true[i] == y_pred[i] and y_true[i] == 0:
            pass
        elif y_true[i] != y_pred[i] and y_true[i] == 0:
            precision += 1
        elif y_true[i] != y_pred[i] and y_true[i] == 1:
            recall += 1

    precision = precision / ([1 for j in range(len(y_pred)) if y_pred[j] == 1].count(1))
    recall = recall / ([1 for j in range(len(y_true)) if y_true[j] == 1].count(1))
    f1_score = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0
    return f1_score


def recall(y_true, y_pred):
    tp, fn = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i] == 1:
            tp += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    recall = tp / (tp + fn) if tp + fn != 0 else 0
    return recall


class ModelFactory:
    class ModelBase:
        def __init__(self, metric):
            self.metric = metric

        def fit(self, train_data, train_label):
            raise NotImplementedError("fit method not implemented")

        def predict(self, test_data):
            raise NotImplementedError("predict method not implemented")

    class SVMModel(ModelBase):
        def __init__(self, metric):
            super().__init__(metric)

        def fit(self, train_data, train_label):
            self.model = svm_predict()

        def predict(self, test_data):
            return svm_predict()

    class RFModel(ModelBase):
        def __init__(self, metric):
            super().__init__(metric)

        def fit(self, train_data, train_label):
            self.model = rf_predict()

        def predict(self, test_data):
            return rf_predict()

    class CNNModel(ModelBase):
        def __init__(self, metric):
            super().__init__(metric)

        def fit(self, train_data, train_label):
            self.model = cnn_predict()

        def predict(self, test_data):
            return cnn_predict()

    class RNNModel(ModelBase):
        def __init__(self, metric):
            super().__init__(metric)

        def fit(self, train_data, train_label):
            self.model = rnn_predict()

        def predict(self, test_data):
            return rnn_predict()

    def create_model(self, model_name, metric):
        if model_name == 'SVM':
            return self.SVMModel(metric)
        elif model_name == 'RF':
            return self.RFModel(metric)
        elif model_name == 'CNN':
            return self.CNNModel(metric)
        elif model_name == 'RNN':
            return self.RNNModel(metric)
        else:
            raise ValueError("unsupported model")

# svm_acc_factory = ModelFactory()
# svm_acc_model = svm_acc_factory.create_model('SVM', 'ACC')
# svm_acc_result = svm_acc_model.fit(dataSampling(int=5), [1, 0, 1, 1, 0])
# svm_acc_pred = svm_acc_model.predict(dataSampling(int=5))
# print("SVM + ACC：", svm_acc_result, svm_acc_pred)
#
# rf_mcc_factory = ModelFactory()
# rf_mcc_model = rf_mcc_factory.create_model('RF', 'MCC')
# rf_mcc_result = rf_mcc_model.fit(dataSampling(int=5), [1, 0, 1, 1, 0])
# rf_mcc_pred = rf_mcc_model.predict(dataSampling(int=5))
# print("RF + MCC：", rf_mcc_result, rf_mcc_pred)
#
# cnn_f1_factory = ModelFactory()
# cnn_f1_model = cnn_f1_factory.create_model('CNN', 'F1')
# cnn_f1_result = cnn_f1_model.fit(dataSampling(int=5), [1, 0, 1, 1, 0])
# cnn_f1_pred = cnn_f1_model.predict(dataSampling(int=5))
# print("CNN + F1：", cnn_f1_result, cnn_f1_pred)