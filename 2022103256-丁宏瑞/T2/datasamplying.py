"""
平时作业2：
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
1.	修饰器类型不限，可以是函数修饰器或类修饰器；
2.	实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""
from ML import ML
from Sampling import Sampling
from Criteria import Criteria


@Criteria('ACC', 'MCC', 'Recall')
@ML('SVM', 'RF', 'RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.create()


# 示例：输入10个含5个特征的样本，输出真实lable之后输出每个模型输出的label
data, label, predict, assessment_criteria = dataSampling(10, 5)

print(data)
print(label)  # (10)
print(predict)  # (3,10),分别是装饰器中三个模型的预测
print(assessment_criteria)
