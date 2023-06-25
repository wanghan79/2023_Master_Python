import random

def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.randint(0, value))
        elif key == 'float':
            result.append(random.uniform(0, value))
        elif key == 'str':
            result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=value)))
    return result

def svmClassification(data):
    # 实现SVM分类算法
    result = "SVM分类算法结果"
    return result

def rfClassification(data):
    # 实现随机森林分类算法
    result = "随机森林分类算法结果"
    return result

def cnnClassification(data):
    # 实现卷积神经网络分类算法
    result = "卷积神经网络分类算法结果"
    return result

def rnnClassification(data):
    # 实现循环神经网络分类算法
    result = "循环神经网络分类算法结果"
    return result

def ACC(result):
    # 实现ACC验证指标操作
    evaluation_result = "ACC验证指标结果"
    return evaluation_result

def MCC(result):
    # 实现MCC验证指标操作
    evaluation_result = "MCC验证指标结果"
    return evaluation_result

def F1(result):
    # 实现F1验证指标操作
    evaluation_result = "F1验证指标结果"
    return evaluation_result

def RECALL(result):
    # 实现RECALL验证指标操作
    evaluation_result = "RECALL验证指标结果"
    return evaluation_result

def classification(data):
    # 分类算法的实现逻辑
    result = "分类结果"
    accuracy = 0.85
    precision = 0.78
    recall = 0.92
    f1_score = 0.84
    return result, accuracy, precision, recall, f1_score


# 修饰器函数
def evaluation_decorator(*args):
    def decorator(func):
        def wrapper(data):
            print("分类算法结果:")
            classification_result = func(data)  # 修复：保存分类算法的结果
            for arg, result in zip(args, classification_result):
                print(f"{arg}分类结果:", result)

                print("验证指标结果:")
                evaluation_result = []
                evaluation_result.append(ACC(result))
                evaluation_result.append(MCC(result))
                evaluation_result.append(F1(result))
                evaluation_result.append(RECALL(result))

                print(f"{arg}验证指标结果:")
                for evaluation in evaluation_result:
                    print(evaluation)
                print()
        return wrapper
    return decorator

@evaluation_decorator("SVM", "RF", "CNN", "RNN")
def generateRandomData(data):
    return [svmClassification(data), rfClassification(data), cnnClassification(data), rnnClassification(data)]

if __name__ == "__main__":
    data = dataSampling(int=100, float=10.0, str=5)
    generateRandomData(data)
