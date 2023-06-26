import torch
import random
import string
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
"""
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
1.	修饰器类型不限，可以是函数修饰器或类修饰器；
2.	实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""
# 机器学习方法修饰器
def mlMethod(method):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if method == 'SVM':
                result = svm_method(data)
            elif method == 'RF':
                result = rf_method(data)
            elif method == 'CNN':
                result = cnn_method(data)
            elif method == 'RNN':
                result = rnn_method(data)
            else:
                print(f"Error: Invalid machine learning method '{method}'.")
                return None
            return result
        return wrapper
    return decorator

# 精度指标修饰器
def metric(metric_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if metric_func == 'ACC':
                result = acc_metric(data)
            elif metric_func == 'MCC':
                result = mcc_metric(data)
            elif metric_func == 'F1':
                result = f1_metric(data)
            elif metric_func == 'RC':
                result = recall_metric(data)
            else:
                print(f"Error: Invalid metric function '{metric_func}'.")
                return None
            return result
        return wrapper
    return decorator

# 随机数据结构生成函数

@metrics_decorator('ACC', 'MCC')
@ml_decorator('SVM', 'RF')
def dataSampling(length=1, dimension=1):
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




def svm_method(data):
    print("Using SVM method to process the data...")
    X = data  # Assume input data format is a 2D list, each sample as a sublist
    y = [0, 1, 0, 1]  # Assume binary classification problem, 0 and 1 represent two classes
    clf = svm.SVC()  # Create SVM classifier object
    clf.fit(X, y)  # Train the model using training data
    return clf



def rf_method(data):
    print("Using Random Forest method to process the data...")
    X = data  # Assume input data format is a 2D list, each sample as a sublist
    y = [0, 1, 0, 1]  # Assume binary classification problem, 0 and 1 represent two classes
    clf = RandomForestClassifier()  # Create Random Forest classifier object
    clf.fit(X, y)  # Train the model using training data
    return clf



def cnn_method(data):
    print("Using CNN method to process the data...")
    model = "CNN model"  # Placeholder, replace with actual CNN model
    return model



def rnn_method(data):
    print("Using RNN method to process the data...")
    model = "RNN model"  # Placeholder, replace with actual RNN model
    return model



def acc_metric(data):
    y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
    accuracy = (y_true == y_pred).mean()
    return accuracy



def mcc_metric(data):
    y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
    tp = ((y_true == 1) & (y_pred == 1)).sum()
    tn = ((y_true == 0) & (y_pred == 0)).sum()
    fp = ((y_true == 0) & (y_pred == 1)).sum()
    fn = ((y_true == 1) & (y_pred == 0)).sum()
    mcc = (tp * tn - fp * fn) / ((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)) ** 0.5
    return mcc



def f1_metric(data):
    y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
    tp = ((y_true == 1) & (y_pred == 1)).sum()
    fp = ((y_true == 0) & (y_pred == 1)).sum()
    fn = ((y_true == 1) & (y_pred == 0)).sum()
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1



def recall_metric(data):
    y_true, y_pred = data  # Assume data is a tuple or list containing true labels and predicted labels
    tp = ((y_true == 1) & (y_pred == 1)).sum()
    fn = ((y_true == 1) & (y_pred == 0)).sum()
    recall = tp / (tp + fn)
    return recall


data = dataSampling(length=5, dimension=1)

rnn_result = rnn_method(data)
rf_result = mlMethod(method='RF')(data)

accuracy = metric(metric_func='ACC')(data)

# 输出结果
print(rnn_result)
print(rf_result)
print(accuracy)


def run():
    # 第二次作业的代码
    print("这是第二次作业")
run()  # 调用run()函数可以执行第二次作业的代码
