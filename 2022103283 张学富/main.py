import os

while(True):
    print("请输入要求展示的作业编号(1-3):")
    lab = input()
    print("结果:")
    if lab == '1':
        os.system('python ./H1/rand_create.py')
    elif lab == '2':
        os.system('python ./H2/datasamplying.py')
    elif lab == '3':
        os.system('python ./H3/factoryMethod.py')
    print("")
