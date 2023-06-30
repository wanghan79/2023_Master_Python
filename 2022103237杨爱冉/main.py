import random

from work1 import dataSampling


class DataSamplingFactory:
    @staticmethod
    def createDataSampling(**kwargs):
        def dataSampling(func):
            def wrapper(*args):
                result = []
                for data_type, data_num in kwargs.items():
                    if data_type == "int":
                        result.extend(random.sample(range(1, 100), data_num))
                    elif data_type == "float":
                        result.extend([random.uniform(0, 1) for _ in range(data_num)])
                    elif data_type == "str":
                        result.extend([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(data_num)])
                return func(result, *args)

            return wrapper

        return dataSampling


@DataSamplingFactory.createDataSampling(int=5, float=3, str=4)
def processRandomData(data):
    # 在这里对数据进行处理
    print("Processing random data:", data)


def main():
    while True:
        print("请选择作业号：")
        print("1. 作业1")
        print("2. 作业2")
        print("3. 作业3")
        print("输入'q'退出")
        choice = input("请输入作业号：")

        if choice == "1":
            # 执行平时作业1
            data = dataSampling(int=5, float=3, str=4)
            print(data)
        elif choice == "2":
            # 执行平时作业2
            processRandomData()
        elif choice == "3":
            # 执行平时作业3
            processRandomData()
        elif choice.lower() == "q":
            # 退出程序
            break
        else:
            print("无效的选项，请重新输入！")


if __name__ == "__main__":
    main()
