import os

while(True):
    index = input("Enter the number:1 , 2 or 3")
    print("This is the result of homework " + index + ":")
    if index == '1':
        os.system('python ./H1/rand_create.py')
    elif index == '2':
        os.system('python ./H2/datasamplying.py')
    elif index == '3':
        os.system('python ./H3/factoryMethod.py')
    print('*' * 80)
