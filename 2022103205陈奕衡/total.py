from test1 import dataSampling
from test2 import evaluation_decorator
from test3 import EvaluationDecorator


def show_menu():
    print("=== 作业展示 ===")
    print("1. 平时作业1 - 随机数据结构生成")
    print("2. 平时作业2 - 修饰器扩展")
    print("3. 平时作业3 - 类工厂设计模式")
    print("0. 退出程序")
    print("================")


def run_homework(homework_number):
    if homework_number == 1:
        data = dataSampling([int, float, str], [1, 10], 5)
        data_sampling_result = dataSampling(data)()
        print(data_sampling_result)
    elif homework_number == 2:
        @evaluation_decorator()
        def data_sampling_decorator_example():
            # 示例代码，可根据实际需求修改
            data = dataSampling([int, float], [1, 100], 10)
            return data

        data_sampling_decorator_example()
    elif homework_number == 3:
        factory = evaluation_decorator()
        ml_model = factory.create_ml_model('CNN')
        ml_model.apply()
    else:
        print("无效的选项")


if __name__ == '__main__':
    while True:
        show_menu()
        choice = input("请输入要展示的作业号（输入0退出）：")
        if choice == '0':
            break
        try:
            homework_number = int(choice)
            run_homework(homework_number)
        except ValueError:
            print("无效的选项")
