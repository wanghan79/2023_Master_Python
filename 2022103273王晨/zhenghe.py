import random
import string
from os import name
from zuoye1 import dataSampling1
from zuoye2 import dataSampling2
from zuoye3 import methods, learning_method_factory, metrics, evaluation_metric_factory


def main():
    print("Enter the homework number to run the example (1, 2, or 3):")
homework_number = int(input())
if homework_number == 1:
    print("Running example for Homework 1")
    example = dataSampling1(int=(-10, 10, 5), float=(-5.0, 5.0, 7), str=(6, 4))
    print(example)

elif homework_number == 2:
    print("Running example for Homework 2")
    example = dataSampling2(int=(-10, 10, 5), float=(-5.0, 5.0, 7), str=(6, 4))
    print(example)

elif homework_number == 3:
    print("Running example for Homework 3")
    for method in methods:
        learning_method = learning_method_factory.get_learning_method(method)
        print(learning_method)

    for metric in metrics:
        evaluation_metric = evaluation_metric_factory.get_evaluation_metric(metric)
        print(evaluation_metric)

else:
    print("Invalid input. Please enter 1, 2, or 3.")

if name == "main":
    main()