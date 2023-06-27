import os
import work_1 as w1

"""
Python节课作业：
    将三次作业集成，实现控制台交互，提示用户输入需要展示的作业号（1、2、3）
    自动运行相应作业案例，并将结果输出到控制台
"""

while (True):
    index = input("输入需要展示的作业号（1、2、3）:")
    if index == '1':
        result = w1.dataSampling(int={'num': 5, 'start': 1, 'end': 10},
                                 float={'num': 5, 'low': 0.0, 'high': 1.0},
                                 str={'num': 5, 'length': 6})
        print(result)
    elif index == '2':
        os.system('python work_2.py')
    elif index == '3':
        os.system('python work_3.py')
    print('-' * 100)
