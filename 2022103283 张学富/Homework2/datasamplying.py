from ML import ML
from Sampling import Sampling
from Criteria import Criteria


@Criteria('ACC', 'MCC', 'Recall')
@ML('SVM', 'RF', 'RNN')
def dataSampling(nums, features):
    x = Sampling(nums, features)
    return x.create()

data, label, predict, assessment_criteria = dataSampling(6, 5)

print(data)
print(label)
print(predict)
print(assessment_criteria)
