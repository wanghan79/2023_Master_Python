import random
import string

import numpy as np
"""
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，
四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。
主要考察点是带参数修饰器的使用，具体要求如下：
1. 修饰器类型不限，可以是函数修饰器或类修饰器；
2. 实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""
def ML(*args):
    def outer(f):
        def SVM(data):
            result = np.random.randint(2, size=(len(data)))
            return result

        def RF(data):
            result = np.random.randint(2, size=(len(data)))
            return result

        def CNN(data):
            result = np.random.randint(2, size=(len(data)))
            return result

        def RNN(data):
            result = np.random.randint(2, size=(len(data)))
            return result

        def inner(**kwargs):
            data=f(**kwargs)
            y_true = []
            for i in args:
                y_true.append(np.random.randint(0, 2, len(data)))
            y_true = np.array(y_true)
            predict = []
            for model in args:
                # 2.记录各个模型结果
                if model == "SVM":
                    predict.append(SVM(data))
                elif model == "RF":
                    predict.append(RF(data))
                elif model == "CNN":
                    predict.append(CNN(data))
                elif model == "RNN":
                    predict.append(RNN(data))
            y_pre = np.array(predict)
            return data,y_true,y_pre
        return inner
    return outer

def Metric(*args):
    def outer(f):
        # 计算ACC（平均可用性）
        def calculate_acc(true_labels, predicted_labels):
            total = len(true_labels)
            correct = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred)
            acc = (correct / total)
            return acc

        # 计算MCC（马修斯相关系数）
        def calculate_mcc(true_labels, predicted_labels):
            tp = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred and true == 1)
            tn = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred and true == 0)
            fp = sum(1 for true, pred in zip(true_labels, predicted_labels) if true != pred and true == 0)
            fn = sum(1 for true, pred in zip(true_labels, predicted_labels) if true != pred and true == 1)

            mcc = (tp * tn - fp * fn) / ((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)) ** 0.5
            return mcc

        # 计算F1得分
        def calculate_f1(true_labels, predicted_labels):
            tp = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred and true == 1)
            fp = sum(1 for true, pred in zip(true_labels, predicted_labels) if true != pred and true == 0)
            fn = sum(1 for true, pred in zip(true_labels, predicted_labels) if true != pred and true == 1)

            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1 = 2 * (precision * recall) / (precision + recall)
            return f1

        # 计算Recall（召回率）
        def calculate_recall(true_labels, predicted_labels):
            tp = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred and true == 1)
            fn = sum(1 for true, pred in zip(true_labels, predicted_labels) if true != pred and true == 1)

            recall = tp / (tp + fn)
            return recall

        def inner(**kwargs):
            data,y_true,y_pre=f(**kwargs)
            measure=[]
            for metric in args:
                if metric == "ACC":
                    for y_t, y_p in zip(y_true, y_pre):
                        measure.append({'ACC': calculate_acc(y_t, y_p)})
                elif metric == "MCC":
                    for y_t, y_p in zip(y_true, y_pre):
                        measure.append({'MCC': calculate_mcc(y_t, y_p)})
                elif metric == "F1":
                    for y_t, y_p in zip(y_true, y_pre):
                        measure.append({'MCC': calculate_f1(y_t, y_p)})
                elif metric == "RECALL":
                    for y_t, y_p in zip(y_true, y_pre):
                        measure.append({'MCC': calculate_recall(y_t, y_p)})
            return data,y_true,y_pre,measure
        return inner
    return outer


@Metric("ACC","F1")
@ML("RNN","SVM")
def dataSampling(**kwargs):
    shape=kwargs.get("shape",[1,])
    data_type = kwargs.get("data_type", ["int"])
    for i in shape:
        if i<0:
            raise ValueError("shape参数不能为负数")
        elif i==0:
            raise ValueError("shape参数不能为0")

    return _generate_data(shape,data_type)

def _generate_data(shape, data_type):
    if len(shape) == 0:
        if len(data_type) == 1:
            if data_type[0] == "int":
                return (random.randint(-100, 100))
            elif data_type[0] == "float":
                return (round(random.uniform(-100.0, 100.0), 2))
            elif data_type[0] == "str":
                return (''.join(random.choices(string.ascii_letters, k=8)))
            else:
                raise ValueError("data_type参数类型应该是整形，浮点型，字符型")
        else:
            res = []
            for i in range(len(data_type)):
                if data_type[i] == "int":
                    res.append(random.randint(-100, 100))
                elif data_type[i] == "float":
                    res.append(round(random.uniform(-100.0, 100.0), 2))
                elif data_type[i] == "str":
                    res.append(''.join(random.choices(string.ascii_letters, k=8)))
                else:
                    raise ValueError("data_type参数类型应该是整形，浮点型，字符型")
            return res
    else:
        return [_generate_data(shape=shape[1:], data_type=data_type) for _ in range(shape[0])]

def main():
    data, y_true, y_pre, measure = dataSampling(shape=[10, 5], data_type=['float'])
    print(data)
    print(y_true)
    print(y_pre)
    print(measure)


if __name__ == '__main__':
    main()







