from MLPackage.ML_Functions import functionSampling

def FactoryML(filename):
    with open(filename, 'r') as f:
        name_list = f.readlines()

    result = []
    for i in name_list:
        # 去除换行符
        i = i.strip()
        result.append(i)
    return result
# 调用
# filename = "config.txt"
# model_list = FactoryML(filename)
# for i in model_list:
#     functionSampling(i)