import random
# 作业2
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
    result = "SVM"
    return result

def rfClassification(data):
    result = "随机森林"
    return result
def cnnClassification(data):
    result = "卷积神经网络"
    return result

def rnnClassification(data):
    result = "循环神经网络"
    return result

def ACC(result):
    evaluation_result = "ACC"
    return evaluation_result

def MCC(result):
    evaluation_result = "MCC"
    return evaluation_result

def F1(result):
    evaluation_result = "F1"
    return evaluation_result

def RECALL(result):
    evaluation_result = "RECALL"
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
            classification_result = func(data) 
            for arg, result in zip(args, classification_result):
                evaluation_result = []
                evaluation_result.append(ACC(result))
                evaluation_result.append(MCC(result))
                evaluation_result.append(F1(result))
                evaluation_result.append(RECALL(result))
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
