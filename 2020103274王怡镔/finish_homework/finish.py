from python_1.rand_project import test as py1
from python_2.task_test import test as py2
from python_3.task_test import test as py3

if __name__ == '__main__':
    number = input("please input homework id:")
    if number in ['1', '2', '3']:
        print(eval('py' + number)())
    else:
        print("sorry!")
