from Homework1 import data_sampling
from Homework2 import decorator
from Homework3 import factory
# 结课作业：
# 建立完整项目工程，将三次平时作业集成在一个工程中，实现控制台交互，
# 提示用户输入要求展示的作业号（1、2或3），自动运行相应作业示例，并将结果输出到控制台。
class homework_factory:

    @staticmethod
    def run_homework(name):
        if name == 'homework1':
            data_type = input("请输入数据类型(int, float, str)：")
            if data_type == 'int':
                data_range = int(input("请输入整数："))
                print("将返回 0 ~ {num} 的随机数:".format(num=data_range))
                kwargs = {data_type: data_range}
                print(data_sampling.data_sampling(** kwargs)[0])
            elif data_type == 'float':
                data_range = float(input("请输入浮点数："))
                print("将返回 0 ~ {num} 的随机数:".format(num=data_range))
                kwargs = {data_type: data_range}
                print(data_sampling.data_sampling(** kwargs)[0])
            elif data_type == 'str':
                data_range = list(input("请输入字符串："))
                print("将返回 {str} 中的随机字符:".format(str=data_range))
                kwargs = {data_type: data_range}
                print(data_sampling.data_sampling(**kwargs)[0])
            else:
                print("输入有误请重新输入！")
        elif name == 'homework2':
            train_data, label_data = decorator.randomdata(5, 5)
            data = {'int': 3}
            case1 = data_sampling.data_sampling(**data)[0]
            case2 = data_sampling.data_sampling(**data)[0]
            print(case1, case2)
            decorator.load(case1, case2, train_data, label_data)
        elif name == 'homework3':
            train_data, label_data = decorator.randomdata(5, 5)
            factory.select_Model(train_data, label_data)


def main():

    while 1:
        hw_number = input("请输入要展示的作业号(1、2或3,0退出）：")
        if hw_number == '1':
            homework_factory.run_homework('homework1')
        elif hw_number == '2':
            homework_factory.run_homework('homework2')
        elif hw_number == '3':
            homework_factory.run_homework('homework3')
        elif hw_number == '0':
            break
        else:
            print("无效的作业号。请输入1、2或3,0退出。")


if __name__ == '__main__':
    main()
