"""
python作业2：进行修饰器的训练，对作业1中随机数的封装构建两层修饰
1.Sampling封装为函数或类都行，生成标签(T,F),任意维度的特征和数量
2.CLASS: ML修饰器，SVM,RF,CNN,RNN,（用于修饰1.中的向量并返回预测的标签Predict(T,F)）
3.CLASS: 第二层修饰，评价指标修饰器,ACC,MCC,F1,Recall
"""
from ML import ML
from Sampling import Sampling
from Criteria import Criteria


@Criteria('ACC', 'MCC', 'Recall')
@ML('SVM', 'RF', 'RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.create()


#输入20个含5个特征的样本
data, label, predict, assessment_criteria = dataSampling(20, 5)

print(data)
print(label)  
print(predict)  
print(assessment_criteria)
