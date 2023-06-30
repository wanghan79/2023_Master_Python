import os

while(True):
    index = input("Please enter the number（1-3）:")
    print("The result is " + index + ":")
    if index == '1':
        os.system('python ./test1/Random.py')
    elif index == '2':
        os.system('python ./test2/datasamplying.py')
    elif index == '3':
        os.system('python ./test3/FactoryML.py')
    print('---------------------------------')

