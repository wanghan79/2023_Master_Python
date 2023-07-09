from text1 import dataSampling,dataSamplingDecorator
from text2 import mlDecorator
from text3 import MLFactory



def show_menu():
    print("=== 作业展示 ===")
    print("1. 平时作业1 - 随机数据结构生成")
    print("2. 平时作业2 - 修饰器扩展")
    print("3. 平时作业3 - 类工厂设计模式")
    print("0. 退出程序")
    print("================")


def run_homework(homework_number):
    if homework_number == 1:
        data_sampling_result = dataSamplingDecorator(dataSampling)()
        print(data_sampling_result)
    elif homework_number == 2:
        @mlDecorator(['SVM', 'RF'], ['ACC', 'MCC'])
        def data_sampling_decorator_example():
            # 示例代码，可根据实际需求修改
            data = dataSampling(numbers=5, floats=3, strings=2)
            return data

        data_sampling_decorator_example()
    elif homework_number == 3:
        factory = MLFactory()
        ml_model = factory.create_ml_model('SVM')
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
