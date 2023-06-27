import os

while(True):
    index = input("Please enter the homework number you want to display （1-3）:")
    print("This is the result of homework " + index + ":")
    if index == '1':
        os.system('python ./homework1/rand_create.py')
    elif index == '2':
        os.system('python ./homework2/datasamplying.py')
    elif index == '3':
        os.system('python ./homework3/factoryMethod.py')
    print('-' * 100)
1