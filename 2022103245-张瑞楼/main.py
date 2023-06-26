import random
from work1 import dataSampling
from work2 import dataSampling as dw2
from work3 import processRandomData

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


@DataSamplingFactory.createDataSampling(int=5, float=5, str=5)
def processRandomData(data):
    # 数据处理
    print("Processing random data:", data)

def main():
    while True:
        print("输入项目编号以执行不同任务：")
        print("1. 项目1")
        print("2. 项目2")
        print("3. 项目3")
        print("输入'0'退出")
        choice = input("请输入编号：")

        if choice == "1":
            # 平时作业一
            data = dataSampling(int=3, float=3, str=3)
            print(data)
        elif choice == "2":
            # 平时作业二
            dw2()
        elif choice == "3":
            # 平时作业三
            processRandomData()
        elif choice == "0":
            # 退出程序
            break
        else:
            print("编号无效，请重新输入")


if __name__ == "__main__":
    main()