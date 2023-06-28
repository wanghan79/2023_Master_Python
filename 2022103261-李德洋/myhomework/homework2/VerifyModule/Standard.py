import numpy as np
import torch

# 计算准确率
def calculate_acc(targets, predictions):
    targets = targets.numpy()
    predictions = predictions.numpy()
    correct = np.sum(targets == predictions)
    total = targets.shape[0]
    acc = correct / total
    return acc

# 计算Matthews相关系数
def calculate_mcc(targets, predictions):
    targets = targets.numpy()
    predictions = predictions.numpy()
    tn = np.sum(np.logical_and(targets == 0, predictions == 0))
    fp = np.sum(np.logical_and(targets == 0, predictions == 1))
    fn = np.sum(np.logical_and(targets == 1, predictions == 0))
    tp = np.sum(np.logical_and(targets == 1, predictions == 1))
    # mcc = (tp * tn - fp * fn) / np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    # 引入平滑因子
    smooth = 1e-10
    mcc = (tp * tn - fp * fn) / np.sqrt(
        (tp + fp + smooth) * (tp + fn + smooth) * (tn + fp + smooth) * (tn + fn + smooth))
    return mcc

# 计算F1得分
def calculate_f1(targets, predictions):
    targets = targets.numpy()
    predictions = predictions.numpy()
    tp = np.sum(np.logical_and(targets == 1, predictions == 1))
    fp = np.sum(np.logical_and(targets == 0, predictions == 1))
    fn = np.sum(np.logical_and(targets == 1, predictions == 0))
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * (precision * recall) / (precision + recall + 1e-8)
    return f1

# 计算召回率
def calculate_recall(targets, predictions):
    targets = targets.numpy()
    predictions = predictions.numpy()
    tp = np.sum(np.logical_and(targets == 1, predictions == 1))
    fn = np.sum(np.logical_and(targets == 1, predictions == 0))
    recall = tp / (tp + fn + 1e-8)
    return recall

# 生成随机数
# targets = torch.randint(0, 2, (100,))
# predictions = torch.randint(0, 2, (100,))

# 计算指标
# acc = calculate_acc(targets, predictions)
# mcc = calculate_mcc(targets, predictions)
# f1 = calculate_f1(targets, predictions)
# recall = calculate_recall(targets, predictions)
#
# print("准确率:", acc)
# print("Matthews相关系数:", mcc)
# print("F1得分:", f1)
# print("召回率:", recall)
