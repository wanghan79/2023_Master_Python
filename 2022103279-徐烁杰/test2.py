import random
from sklearn.metrics import accuracy_score, matthews_corrcoef, f1_score, recall_score
import numbers
import numpy as np

def machineLearningMethodDecorator(*methods):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            print("原始数据:", data)
            filtered_data = [x for x in data if isinstance(x, numbers.Number)]  # 仅保留数值类型数据
            labels = np.array([1 if x > np.mean(filtered_data) else 0 for x in filtered_data])  # 将数据转换为二分类标签
            for method in methods:
                predicted_labels = np.array([random.choice([0, 1]) for _ in range(len(labels))])  # 随机生成预测标签
                accuracy = accuracy_score(labels, predicted_labels)
                mcc = matthews_corrcoef(labels, predicted_labels)
                f1 = f1_score(labels, predicted_labels)
                recall = recall_score(labels, predicted_labels)
                print("计算精度指标:{}方法 - ACC: {:.2f}, MCC: {:.2f}, F1: {:.2f}, RECALL: {:.2f}".format(method, accuracy, mcc, f1, recall))
        return wrapper
    return decorator

@machineLearningMethodDecorator('SVM', 'RF', 'CNN', 'RNN')
def dataSampling(**kwargs):
    result = []
    for data_type, data_count in kwargs.items():
        if data_type == 'int':
            result.extend(random.sample(range(1, 100), data_count))
        elif data_type == 'float':
            result.extend([random.uniform(1, 100) for _ in range(data_count)])
        elif data_type == 'str':
            result.extend([''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5)) for _ in range(data_count)])
    return result

def main():
    while True:
        print("请输入要展示的作业号（1、2或3），输入q退出：")
        command = input()
        if command == 'q':
            break
        elif command == '1':
            break
        elif command == '2':
            int_num = int(input("请输入需要随机生成的int数量："))
            float_num = int(input("请输入需要随机生成的float数量："))
            # str_num = int(input("请输入需要随机生成的str数量："))
            result = dataSampling(int=int_num, float=float_num, str=0)
            print(result)
        elif command == '3':
            break
        else:
            print("无效的命令，请重新输入。")

if __name__ == '__main__':
    main()
