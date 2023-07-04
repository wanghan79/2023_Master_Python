import random
import string

# 定义修饰器，用于进行机器学习方法和验证指标操作的任意组合
from homework1 import dataSampling


def ml_operation(method, metric):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 在被修饰函数func之前进行评价指标操作
            print(f"{method} method {metric} result: ")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 模拟SVM, RF, CNN, RNN的预测结果，并计算精度指标
def svm_predict():
    return [random.randint(0,1) for i in range(10)]
def rf_predict():
    return [random.randint(0,1) for i in range(10)]
def cnn_predict():
    return [random.randint(0,1) for i in range(10)]
def rnn_predict():
    return [random.randint(0,1) for i in range(10)]

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
    precision,recall = 0, 0
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

# 修饰器使用示例
@ml_operation('SVM', 'ACC')
def svm_accuracy(y_true):
    y_pred = svm_predict()
    accuracy = acc(y_true, y_pred)
    return accuracy

@ml_operation('RF', 'MCC')
def rf_mcc(y_true):
    y_pred = rf_predict()
    mcc_score = mcc(y_true, y_pred)
    return mcc_score
@ml_operation('CNN', 'F1-Score')
def cnn_f1(y_true):
    y_pred = cnn_predict()
    f1_score = f1(y_true, y_pred)
    return f1_score

@ml_operation('RNN', 'RECALL')
def rnn_recall(y_true):
    y_pred = rnn_predict()
    recall_score = recall(y_true, y_pred)
    return recall_score

# svm_accuracy([1,0,1,1,0,1,0,1,0,0])
# rf_mcc([1,0,1,1,0,1,0,1,0,0])
# cnn_f1([1,0,1,1,0,1,0,1,0,0])
# rnn_recall([1,0,1,1,0,1,0,1,0,0])

# 两个修饰器的使用示例
@ml_operation('SVM', 'ACC')
@ml_operation('RF', 'MCC')
def svm_rf_accuracy_mcc(y_true):
    svm_result = svm_predict()
    rf_result = rf_predict()
    acc_score = acc(y_true, svm_result)
    mcc_score = mcc(y_true, rf_result)
    return (acc_score, mcc_score)

# 可以根据需要随意组合不同的修饰器参数
@ml_operation('CNN', 'F1-Score')
@ml_operation('RF', 'ACC')
@ml_operation('SVM', 'RECALL')
def cnn_rf_svm_score(y_true):
    cnn_result = cnn_predict()
    rf_result = rf_predict()
    svm_result = svm_predict()
    f1_score = f1(y_true, cnn_result)
    acc_score = acc(y_true, rf_result)
    recall_score = recall(y_true, svm_result)
    return (f1_score, acc_score, recall_score)

# # 随机生成一些数据用于测试
# int_data = dataSampling(int=5)
# float_data = dataSampling(float=3)
# str_data = dataSampling(str=2)
#
# print("随机 int 数据：", int_data)
# print("随机 float 数据：", float_data)
# print("随机 str 数据：", str_data)
#
# # 使用修饰器进行机器学习操作和评价指标操作
# svm_rf_accuracy_mcc_result = svm_rf_accuracy_mcc([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
# print("SVM + RF 精度评估：", svm_rf_accuracy_mcc_result)
#
# cnn_rf_svm_score_result = cnn_rf_svm_score([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
# print("CNN + RF + SVM 评价指标：", cnn_rf_svm_score_result)