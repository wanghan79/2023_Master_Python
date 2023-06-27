import os

while (True):
    index = input("请输入作业编号(1-3):")
    print("作业" + index + "运行结果:")

    FILE_DIC = {'1': 'python ./homework1/rand_create.py',
                '2': 'python ./homework2/datasamplying.py',
                '3': 'python ./homework3/factoryMethod.py'}

    if index in FILE_DIC:
        os.system(FILE_DIC[index])
    else:
        print("无效的输入")

    print('-' * 100)
