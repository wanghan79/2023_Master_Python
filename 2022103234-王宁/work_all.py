import work_one
from work_two import dataSampling
from work_three import run_work3

def main():
    while True:

        x = input("请输入1~3中的一个数字，以运行对应的作业，输入0表示退出：")
        if x == '1':
            # 执行作业1
            work_one.run_work1()
            print("---------作业1到此结束---------")
        elif x == "2":
            # 执行作业2
            dataSampling.dataSampling_run()
            print("---------作业2到此结束---------")
        elif x == "3":
            # 执行作业3
            run_work3()
            print("---------作业3到此结束---------")
        elif x == "0":
            # 退出程序
            break
        else:
            print("输入为无效值！请重新输入！")


if __name__ == '__main__':
    main()
