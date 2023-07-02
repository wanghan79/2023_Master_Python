import random
import string
from os import name
from homework-one import Sample1
from homework-two import Sample2
from homework-three import methods, L_M_F, metrics, E_M_F

def main():
    print("Enter the homework number to run the instance (1, 2, or 3):")
homework_number = int(input())
if homework_number == 1:
    print("Running instance for Homework 1")
    instance = Sample1(int=(-1, 2, -3), float=(-2.0, 4.0, 5), str=(3, 2))
    print(instance)

elif homework_number == 2:
    print("Running instance for Homework 2")
    instance = Sample2(int=(-2, 2, 1), float=(-3.0, 2.0, 4), str=(2, 3))
    print(instance)

elif homework_number == 3:
    print("Running instance for Homework 3")
    for method in methods:
        L_M = L_M_F.get_L_M(method)
        print(L_M)

    for metric in metrics:
        E_M = E_M_F.get_E_M(metric)
        print(E_M)

else:
    print("Invalid input. Please enter 1, 2, or 3.")

if name == "main":
    main()