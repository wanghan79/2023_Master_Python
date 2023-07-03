import os

while(True):
    index = input("请输入作业号（1-3）:")
    print("作业" + index + "结果:")
    if index == '1':
        os.system('python ./作业1/rand_create.py')
    elif index == '2':
        os.system('python ./作业2/datasamplying.py')
    elif index == '3':
        os.system('python ./作业3/factoryMethod.py')
    else:
        print("错误输入！")
    print('*' * 90)
