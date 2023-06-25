import os

def show_menu():
    print("请选择要展示的作业号:")
    print("1. 作业1 - 随机数据结构生成函数")
    print("2. 作业2 - 修饰器技术")
    print("3. 作业3 - 类工厂设计模式")
    print("0. 退出")


def run_job1():
    print("*********************\n运行作业1示例:")
    os.system(r'python homework_1.py')


def run_job2():
    print("*********************\n运行作业2示例:")
    os.system(r'python homework_2.py')


def run_job3():
    print("运行作业3示例:")
    os.system(r'python homework_3.py')


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("请输入作业号：")

        if choice == "1":
            run_job1()
        elif choice == "2":
            run_job2()
        elif choice == "3":
            run_job3()
        elif choice == "0":
            break
