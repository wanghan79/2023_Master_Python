import random
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import numpy as np


"""
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，
四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。
主要考察点是带参数修饰器的使用，具体要求如下：
1. 修饰器类型不限，可以是函数修饰器或类修饰器；
2. 实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""


# 机器学习方法修饰器
def ml_decorator(*args):
    def outer_wrapper(func):
        def inner_wrapper(**kwargs):
            # 获取数据和特征数
            data, feature = func(**kwargs)

            # 将数据变成每行一个sample的形式，方便训练和验证
            X = flatten(data)
            X = np.array(X).reshape(len(X) // feature, feature)
            print(f'每一个sample如下：\n{X}')
            X = onehot(X)
            # print(f'onehot之后的sample={X}')

            slicing = int(len(X) * 0.7)  # 七成用作训练集

            global multi_pred_y
            for model in args:
                print(f'正在执行{model}操作...')
                if model == 'SVM':
                    clf = svm_method(data=X[0: slicing])
                    pred_y = clf.predict(X[slicing:])
                    multi_pred_y['SVM'] = list(pred_y)
                elif model == 'RF':
                    clf = rf_method(data=X[0: slicing])
                    pred_y = clf.predict(X[slicing:])
                    multi_pred_y['RF'] = list(pred_y)
                elif model == 'CNN':
                    pred_y = [random.randint(0, 1) for _ in range(samples - slicing)]
                    multi_pred_y['CNN'] = list(pred_y)
                elif model == 'RNN':
                    pred_y = [random.randint(0, 1) for _ in range(samples - slicing)]
                    multi_pred_y['RNN'] = list(pred_y)
                print(f'{model}执行完毕...\n')
            return data, feature
        return inner_wrapper
    return outer_wrapper


# 精度指标修饰器
def metrics_decorator(*args):
    def outer_wrapper(func):
        def inner_wrapper(**kwargs):
            data, feature = func(**kwargs)

            # 根据我设定的规则，为验证集设置标签
            global y_true
            y_true = get_labels(data, feature)
            for metric in args:
                print(f'执行了{metric}操作...')
                if metric == 'ACC':
                    for ml_method, y_pred in multi_pred_y.items():
                        accuracy = acc_metric(y_true=y_true, y_pred=y_pred)
                        print(f'{ml_method}精度={accuracy}')
                elif metric == 'MCC':
                    for ml_method, y_pred in multi_pred_y.items():
                        accuracy = mcc_metric(y_true=y_true, y_pred=y_pred)
                        print(f'{ml_method}精度={accuracy}')
                elif metric == 'F1':
                    for ml_method, y_pred in multi_pred_y.items():
                        accuracy = f1_metric(y_true=y_true, y_pred=y_pred)
                        print(f'{ml_method}精度={accuracy}')
                elif metric == 'RECALL':
                    for ml_method, y_pred in multi_pred_y.items():
                        accuracy = recall_metric(y_true=y_true, y_pred=y_pred)
                        print(f'{ml_method}精度={accuracy}')
                print(f'{metric}操作执行完毕...')
            return data, feature
        return inner_wrapper
    return outer_wrapper


# 随机数据结构生成函数
@metrics_decorator('ACC', 'MCC')
@ml_decorator('SVM', 'RF')
def dataSampling(**kwargs):
    new_shape, type1 = kwargs.get('shape'), kwargs.get('type')
    print('我想要一个{}维度的随机数据，其中每个元素的类型是{}'.format(new_shape, type1))

    # 计算列表长度，即new_shape的每一个元素乘起来
    data_len = 1
    for _ in new_shape:
        data_len *= _

    # 根据type生成数据
    res = []
    for _ in range(data_len):
        tmp = []
        for data_type in type1:
            if data_type == int:
                tmp.append(random.randint(1, 100))
            elif data_type == float:
                tmp.append(round(random.uniform(0, 100), 3))
            elif data_type == str:
                tmp.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10))))
            else:
                print(f'unsupported data type: {data_type}')
        res.append(tmp)

    # print('当前获取的随机列表为{}, 我想要的维度是{}.'.format(res, new_shape))
    return reshape(res, new_shape), len(type1)


def reshape(res, new_shape):
    new_len = len(res)

    # 每次拿最后n个元素组成一个列表
    for n in new_shape[::-1]:
        # print("----------")
        lst = []
        for _ in range(new_len // n):   # 拿几次
            tmp = res[-n:]      # 切片，取最后n个元素
            # print("tmp:", tmp)
            lst.insert(0, tmp)  # 头插
            res = res[:-n]      # 剩下的切片重新赋值

        # print("lst:", lst)
        res = lst
        new_len //= n

    return res


def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def onehot(data):
    encoder = OneHotEncoder()
    data = encoder.fit_transform(data).toarray()
    return data


# 生成样本真实标签的方法
def get_labels(data, feature):
    X = flatten(data)
    X = np.array(X).reshape(len(X) // feature, feature)
    # print("get_labels的data=", X)

    # 找到首个不是str类型元素的索引
    ind = -1
    for i in range(feature):
        if not isinstance(X[i], str):
            ind = i
            break

    # 下一行解释：如果都是str类型元素，随机生成标签
    Y = [random.randint(0, 1) for _ in range(len(X))]
    sum = 0
    if ind != -1:
        for i in range(len(X)):
            sum += int(X[i][ind])
        ave = sum / len(X)
        for i in range(len(X)):
            Y[i] = 1 if int(X[i][ind]) > ave else 0

    return Y[int(len(Y) * 0.7):]


def svm_method(**kwargs):
    X = kwargs.get('data')
    # print(X)

    # 假设标签为二分类问题，0和1代表两个类别
    y = [random.randint(0, 1) for _ in range(len(X))]
    # print("y = ", y)

    # 创建SVM分类器对象
    clf = svm.SVC()
    clf.fit(X, y)
    return clf


def rf_method(**kwargs):
    X = kwargs.get('data')

    # 假设标签为二分类问题，0和1代表两个类别
    y = [random.randint(0, 1) for _ in range(len(X))]

    # 创建随机森林分类器对象
    clf = RandomForestClassifier()
    clf.fit(X, y)  # 使用训练数据进行模型训练
    return clf


def acc_metric(**kwargs):
    y_true = kwargs.get('y_true')
    y_pred = kwargs.get('y_pred')
    count = sum(1 for x, y in zip(y_true, y_pred) if x == y)
    if len(y_true) == 0:
        return 0
    return count / len(y_true)


def mcc_metric(**kwargs):
    y_true = kwargs.get('y_true')
    y_pred = kwargs.get('y_pred')

    tp = sum(1 for x, y in zip(y_true, y_pred) if x == y == 1)
    tn = sum(1 for x, y in zip(y_true, y_pred) if x == y == 0)
    fp = sum(1 for x, y in zip(y_true, y_pred) if x == 0 and y == 1)
    fn = sum(1 for x, y in zip(y_true, y_pred) if x == 1 and y == 0)

    numerator = tp * tn - fp * fn
    denominator = ((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)) ** 0.5
    if denominator == 0:
        return 0
    else:
        return numerator / denominator


def f1_metric(**kwargs):
    y_true = kwargs.get('y_true')
    y_pred = kwargs.get('y_pred')

    tp = sum(1 for x, y in zip(y_true, y_pred) if x == y == 1)
    fp = sum(1 for x, y in zip(y_true, y_pred) if x == 0 and y == 1)
    fn = sum(1 for x, y in zip(y_true, y_pred) if x == 1 and y == 0)

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1


def recall_metric(**kwargs):
    y_true = kwargs.get('y_true')
    y_pred = kwargs.get('y_pred')

    tp = sum(1 for x, y in zip(y_true, y_pred) if x == y == 1)
    fn = sum(1 for x, y in zip(y_true, y_pred) if x == 1 and y == 0)

    recall = tp / (tp + fn)
    return recall


multi_pred_y = dict()
y_true = list()


# 调用示例
def main():
    data, feature = dataSampling(shape=(4, 2, 2), type=(int, str, float))
    print(f"随机生成的数据如下：\n{data}\n")
    print(f'通过机器学习方法得到的验证集预测标签={multi_pred_y}')
    print(f'验证集的真实标签={y_true}')


if __name__ == '__main__':
    main()

