import os
# 集成 主函数 调取三个Python程序
while(True):
    index = input("enter 1 2 3:")
    if index == '1':
        os.system('python 1.py')
    elif index == '2':
        os.system('python 2.py')
    elif index == '3':
        os.system('python 3.py')
