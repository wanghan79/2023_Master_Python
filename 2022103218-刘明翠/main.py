from data_sampling import dataSampling
from machine_learning import machineLearningDecorator
from class_factory import DataSamplingFactory


def main():
    print("请选择要运行的作业示例：")
    print("1. 平时作业1 - 随机数据结构生成封装函数")
    print("2. 平时作业2 - 修饰器技术与机器学习方法、精度指标操作")
    print("3. 平时作业3 - 类工厂设计模式")

    choice = input("请输入作业号：")
    global dataSampling
    if choice == '1':
        print("运行平时作业1示例：")
        data = dataSampling(int=(1, 100), float=(0.0, 1.0), str='abcdefghijklmnopqrstuvwxyz')
        print("随机数据：", data)
    elif choice == '2':
        print("运行平时作业2示例：")

        @machineLearningDecorator('SVM', 'RF', 'ACC', 'F1')
        def sample_func(**kwargs):
            return kwargs

        result = sample_func(int=(1, 100), float=(0.0, 1.0), str='abcdefghijklmnopqrstuvwxyz')
        print("修饰器示例结果：", result)
    elif choice == '3':
        print("运行平时作业3示例：")

        factory = DataSamplingFactory('SVM', 'RF', 'ACC', 'F1')
        dataSampling = factory.create_data_sampling()

        data = dataSampling(int=(1, 100), float=(0.0, 1.0), str='abcdefghijklmnopqrstuvwxyz')
        print("类工厂示例结果：", data)
    else:
        print("无效的作业号，请重新运行程序并输入有效的作业号。")


if __name__ == '__main__':
    main()
