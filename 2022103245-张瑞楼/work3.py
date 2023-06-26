import random

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

@DataSamplingFactory.createDataSampling(int=3, float=3, str=3)
def processRandomData(data):
    # 在这里对数据进行处理
    print("Processing random data:", data)
