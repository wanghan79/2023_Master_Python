import os

"""
Python节课作业：
将三次作业集成，实现控制台交互，提示用户输入需要展示的作业号（1、2、3）
自动运行相应作业案例，并将结果输出到控制台
"""

while (True):
    index = input("输入需要展示的作业号（1、2、3）:")
    if index == '1':
        os.system('python homework1.py')
    elif index == '2':
        os.system('python homework2.py')
    elif index == '3':
        os.system('python homework3.py')
    else:
        print("输入的作业号有误，已退出")
        break
