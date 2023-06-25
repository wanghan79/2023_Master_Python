from function1 import dataSampling,dataSamplingDecorator
from function2 import mlDecorator
from function3 import MLFactory


def run_homework(homework_number):
    if homework_number == 1:
        data_sampling_result = dataSamplingDecorator(dataSampling)()
        print(data_sampling_result)
    elif homework_number == 2:
        @mlDecorator(['SVM', 'RF'], ['ACC', 'MCC'])
        def data_sampling_decorator_example():
            # 示例代码，可根据实际需求修改
            data = dataSampling(numbers=10, floats=10, strings=2)
            return data

        data_sampling_decorator_example()
    elif homework_number == 3:
        factory = MLFactory()
        ml_model = factory.create_ml_model('RF')
        ml_model.apply()
    else:
        print("无效的选项")


def function():
    print("=== 调用不同功能 ===")
    print("1. 平时作业1 - 随机数据结构生成")
    print("2. 平时作业2 - 修饰器扩展")
    print("3. 平时作业3 - 类工厂设计模式")
    print("4. 退出程序")
    print("================")


if __name__ == '__main__':
    while True:
        function()
        number = input("请输入要展示的作业号（输入4退出）：")
        if number == '4':
            break
        try:
            homework_number = int(number)
            run_homework(homework_number)
        except ValueError:
            print("无效的选项")
