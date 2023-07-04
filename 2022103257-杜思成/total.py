import random
import string
from os import name
from zuoye1 import dataSampling1
from zuoye2 import dataSampling2
from zuoye3 import methods, learning_method_factory, metrics, evaluation_metric_factory


def main():
    print("输入序号运行 (1, 2, or 3):")
homework_number = int(input())
if homework_number == 1:
    print("执行作业1")
    example = dataSampling1(int=(-10, 10, 5), float=(-5.0, 5.0, 7), str=(6, 4))
    print(example)

elif homework_number == 2:
    print("执行作业2")
    example = dataSampling2(int=(-10, 10, 5), float=(-5.0, 5.0, 7), str=(6, 4))
    print(example)

elif homework_number == 3:
    print("执行作业3")
    for method in methods:
        learning_method = learning_method_factory.get_learning_method(method)
        print(learning_method)

    for metric in metrics:
        evaluation_metric = evaluation_metric_factory.get_evaluation_metric(metric)
        print(evaluation_metric)

else:
    print("输入错误请输入 1, 2 或 3.")

if name == "main":
    main()
