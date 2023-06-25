import homework1
import homework2
import homework3

def main():
    while True:
        print("请选择要展示的作业号（1、2或3），输入 'q' 退出：")
        choice = input("作业号：")

        if choice == '1':
            data = homework1.dataSampling(int=100, float=10.0, str=5, length=5)
            print("随机数据生成结果：", data)
        elif choice == '2':
            data = homework1.dataSampling(int=100, float=10.0, str=5, length=5)
            result = homework2.classification(data)
            print("分类算法结果：", result)

        elif choice == '3':
            homework3.main()
        elif choice == 'q':
            print("退出程序")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()
