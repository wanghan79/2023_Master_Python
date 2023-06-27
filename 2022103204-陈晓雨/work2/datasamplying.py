
from work2.Sampling import Sampling
from work2.Criteria import Criteria
from work2.ML import ML


@Criteria('ACC', 'MCC', 'Recall')
@ML('SVM', 'RF', 'RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.create()


def dataSampling_run():
    # 示例：输入10个含5个特征的样本，输出真实lable之后输出每个模型输出的label
    data, label, predict, assessment_criteria = dataSampling(10, 5)
    print(data)
    print(label)  # (10)
    print(predict)  # (3,10),分别是装饰器中三个模型的预测
    print(assessment_criteria)
