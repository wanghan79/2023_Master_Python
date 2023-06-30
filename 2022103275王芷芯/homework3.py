import math
import numpy as np

class ModelEvaluator:
    def __init__(self, data, label):
        self.data = data
        self.label = label

    def evaluate(self, predict):
        assessment_criteria = []

        # predict每行对应一个模型标签，单独对每个模型计算各项评估指标，将指标放入一个字典中
        for pre in predict:
            cri_dict = {}
            TP, TN, FP, FN = self.calcultate(self.label, pre)

            cri_dict['ACC'] = self.ACC(TP, TN, len(self.label))
            cri_dict['MCC'] = self.MCC(TP, TN, FP, FN)
            cri_dict['F1'] = self.F1(TP, TN, len(self.label))
            cri_dict['Recall'] = self.Recall(TP, FN)

            assessment_criteria.append(cri_dict)
        return assessment_criteria

    def calcultate(self, label, predict):
        TP, TN, FP, FN = 0, 0, 0, 0
        for i in range(len(label)):
            if label[i] == 1 and predict[i] == 1:
                TP += 1
            elif label[i] == 0 and predict[i] == 0:
                TN += 1
            elif label[i] == 0 and predict[i] == 1:
                FP += 1
            elif label[i] == 1 and predict[i] == 0:
                FN += 1
        return TP, TN, FP, FN

    def ACC(self, TP, TN, label_num):
        acc = (TP + TN) / label_num
        return acc

    def MCC(self, TP, TN, FP, FN):
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FN) * (TP + FP) * (TN + FP) * (TN + FN))
        return mcc

    def F1(self, TP, TN, label_num):
        f1 = 2 * TP / (label_num + TP - TN)
        return f1

    def Recall(self, TP, FN):
        recall = TP / (TP + FN)
        return recall


class SVMModelEvaluator(ModelEvaluator):
    def evaluate(self):
        result = np.random.randint(2, size=(len(self.data)))
        return result


class RFModelEvaluator(ModelEvaluator):
    def evaluate(self):
        result = np.random.randint(2, size=(len(self.data)))
        return result


class CNNModelEvaluator(ModelEvaluator):
    def evaluate(self):
        result = np.random.randint(2, size=(len(self.data)))
        return result


class RNNModelEvaluator(ModelEvaluator):
    def evaluate(self):
        result = np.random.randint(2, size=(len(self.data)))
        return result


class ModelEvaluatorFactory:
    def create_model_evaluator(self, model_type, data, label):
        if model_type == "SVM":
            return SVMModelEvaluator(data, label)
        elif model_type == "RF":
            return RFModelEvaluator(data, label)
        elif model_type == "CNN":
            return CNNModelEvaluator(data, label)
        elif model_type == "RNN":
            return RNNModelEvaluator(data, label)
        else:
            raise ValueError("Invalid model type")


# Example usage
data = np.random.random((10, 5))
label = np.random.randint(2, size=len(data))

factory = ModelEvaluatorFactory()
svm_evaluator = factory.create_model_evaluator("SVM", data, label)
rf_evaluator = factory.create_model_evaluator("RF", data, label)
cnn_evaluator = factory.create_model_evaluator("CNN", data, label)
rnn_evaluator = factory.create_model_evaluator("RNN", data, label)

svm_result = svm_evaluator.evaluate()
rf_result = rf_evaluator.evaluate()
cnn_result = cnn_evaluator.evaluate()
rnn_result = rnn_evaluator.evaluate()

print(data)
print(label)
print(svm_result)
print(rf_result)
print(cnn_result)
print(rnn_result)

# Calculate assessment criteria
criteria = ModelEvaluator(data, label)
assessment_criteria = criteria.evaluate([svm_result, rf_result, cnn_result, rnn_result])

# Print assessment criteria
for i in range(len(assessment_criteria)):
    print(f"Model {i+1}:")
    for key, value in assessment_criteria[i].items():
        print(f"{key}: {value}")
    print()