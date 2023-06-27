from work1 import work1
from work2 import datasamplying
from work3.work3 import run_work3


def main():
    while True:

        x = input("请输入1-3中的一个数字，以运行对应的作业，输入Q或者q表示退出：")
        if x == '1':
            # 执行作业1
            work1.run_work1()
            print("---------作业1结束---------")
        elif x == "2":
            # 执行作业2
            datasamplying.dataSampling_run()
            print("---------作业2结束---------")
        elif x == "3":
            # 执行作业3
            run_work3()
            print("---------作业3结束---------")
        elif x.lower() == "q":
            # 退出程序
            break
        else:
            print("输入无效！请重新输入")


if __name__ == '__main__':
    main()
