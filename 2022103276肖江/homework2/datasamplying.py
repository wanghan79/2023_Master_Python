"""
平时作业2：
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
1.	修饰器类型不限，可以是函数修饰器或类修饰器；
2.	实现两个修饰器，通过修饰器参数（*args）实现机器学习方法和验证指标操作的任意组合；
"""


from standards import standards
from ML import ML
from Sampling import Sampling


@standards('ACC', 'MCC', 'F1', 'Recall')
@ML('SVM', 'RF', 'CNN', 'RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.generate()


# 输入10个含5个特征的样本
data, label, predict, assessmentCriteria = dataSampling(10, 5)

# 输出结果
print("data:", data)  # 输入数据
print("label:", label)  # 标签
print("predict:", predict)  # 模型的预测结果
print("assessmentCriteria:", assessmentCriteria)  # 精度
