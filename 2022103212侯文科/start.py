from task1 import task1_run
from task2 import task2_run
from task3 import task3_run
def main():
    while True:
        print("说明：")
        print(" 作业1对应数字1，作业2对应数字2，作业3对应数字3")
        print(" 输入e时表示退出")
        print("请按要求输入：")
        x=input("请输入1或者2或者3：")
        if x=='1':
            task1_run()
            print("==============================================================")
        elif x == "2":
            # 执行平时作业2
            task2_run()
            print("==============================================================")
        elif x== "3":
            # 执行平时作业3
            task3_run()
            print("==============================================================")
        elif x.lower() == "e":
            # 退出程序
            break
        else:
            print("无效的选项，请重新输入！")

if __name__ == '__main__':
    main()