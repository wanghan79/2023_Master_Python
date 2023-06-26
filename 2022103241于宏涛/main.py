import work1
import work2
import work3

"""
建立完整项目工程，将三次平时作业集成在一个工程中，实现控制台交互，
提示用户输入要求展示的作业号（1、2或3），自动运行相应作业示例，并将结果输出到控制台。
"""


def main():
    print("输入数字（1、2、3）展示相应作业示例，输入Q或q退出运行。")

    while True:
        user_input = input('输入你的选择，并点击回车: ')

        if user_input == '1':
            work1.main()
        elif user_input == '2':
            work2.main()
        elif user_input == '3':
            work3.main()
        elif user_input.lower() == 'q':
            break
        else:
            print("输入无效，请重新输入！")
        print("--------------------------")


if __name__ == '__main__':
    main()
