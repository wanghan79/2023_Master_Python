"""
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的四种机器学习方法（SVM,RF,CNN,RNN）操作，四种精度指标（ACC,MCC,F1,RECALL）操作，以及相应的调用示例。
"""
from ML import ML
from Sampling import Sampling
from Criteria import Criteria


@Criteria('ACC', 'MCC','F1', 'Recall')
@ML('SVM', 'RF', 'CNN','RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.create()


# 示例：输入10个含5个特征的样本，输出真实lable之后输出每个模型输出的label
data, label, predict, assessment_criteria = dataSampling(10, 5)

print(data)
print(label)  
print(predict)  
print(assessment_criteria)
