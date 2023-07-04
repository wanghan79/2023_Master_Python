import os
import subprocess

t = input("请输入一个1或2或3,执行homework1或homework2或homework3:")
if t == 1:
    os.system("python homework1.py -c")
elif t == 2:
    os.system("python homework2.py -c")
elif t == 3:
    os.system("python homework3.py -c")
