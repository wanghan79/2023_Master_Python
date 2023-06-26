from homework1 import test1
from homework2 import test2
from homework3 import test3

def main():
    print("请选择作业号：")
    print("1. homework1")
    print("2. homework2")
    print("3. homework3")

    while True:
        homework = input("请输入作业号：")
        if homework == "1":
            data = test1()
            print(data)
        elif homework == "2":
            data = test2()
            print(data)
        elif homework == "3":
            data = test3()
            print(data)
        else:
            print("按任意键，程序运行结束！")
            break



if __name__ == "__main__":
    main()