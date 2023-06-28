import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from VerifyModule.Standard import calculate_acc,calculate_recall,calculate_mcc,calculate_f1
# SVM 模型
class SVM(nn.Module):
    def __init__(self, input_dim):
        super(SVM, self).__init__()
        self.fc = nn.Linear(input_dim, 1)

    def forward(self, x):
        out = self.fc(x)
        return out

# RF 模型
class RandomForest(nn.Module):
    def __init__(self, input_dim):
        super(RandomForest, self).__init__()
        self.fc = nn.Linear(input_dim, 1)

    def forward(self, x):
        out = self.fc(x)
        return out

# CNN 模型
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(32 * 4 * 4, 64)
        self.fc2 = nn.Linear(64, 2)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 32 * 4 * 4)
        x = torch.relu(self.fc1(x))
        out = self.fc2(x)
        return out

# RNN 模型
class RNN(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(RNN, self).__init__()
        self.rnn = nn.RNN(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 2)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])
        return out

# 生成 100 * 10 * 10 的随机数
data = np.random.randint(0, 1000, (100, 10, 10))

# 转换为PyTorch的Tensor
data_tensor = torch.from_numpy(data).float()

def functionSampling(func_type):
    if func_type == 'svm':
        # SVM 模型训练和预测
        svm_model = SVM(input_dim=100)
        svm_criterion = nn.HingeEmbeddingLoss()
        svm_optimizer = optim.SGD(svm_model.parameters(), lr=0.01)
        # 真实标签
        svm_labels = torch.randint(0, 2, (100,))
        svm_labels = svm_labels.float()

        svm_optimizer.zero_grad()
        svm_outputs = svm_model(data_tensor.view(100, -1))
        svm_loss = svm_criterion(svm_outputs.squeeze(), svm_labels)
        svm_loss.backward()
        svm_optimizer.step()

        svm_prediction = torch.sign(svm_outputs).detach().numpy()
        svm_prediction = np.where(svm_prediction == -1, 0, svm_prediction)
        svm_prediction = torch.from_numpy(svm_prediction)
        # print("SVM 预测结果:", svm_prediction)
        print("SVM 准确率:{} ;\nMatthews相关系数: {} ;\nF1得分: {};\n召回率: {}\n".format(calculate_acc(svm_labels,svm_prediction), calculate_mcc(svm_labels,svm_prediction), calculate_f1(svm_labels,svm_prediction), calculate_recall(svm_labels,svm_prediction)))
        return svm_prediction

    elif func_type == 'rf':
        # RF 模型训练和预测
        rf_model = RandomForest(input_dim=100)
        rf_criterion = nn.BCEWithLogitsLoss()
        rf_optimizer = optim.Adam(rf_model.parameters(), lr=0.01)
        # 真实标签
        rf_labels = torch.randint(0, 2, (100,))
        rf_labels = rf_labels.float()

        rf_optimizer.zero_grad()
        rf_outputs = rf_model(data_tensor.view(100, -1))
        rf_loss = rf_criterion(rf_outputs.squeeze(), rf_labels)
        rf_loss.backward()
        rf_optimizer.step()

        rf_prediction = torch.sigmoid(rf_outputs).detach().numpy()
        rf_prediction = np.where(rf_prediction > 0.5, 1, 0)
        rf_prediction = torch.from_numpy(rf_prediction)
        print("RF 准确率:{} ;\nMatthews相关系数: {} ;\nF1得分: {};\n召回率: {}\n".format(
            calculate_acc(rf_labels, rf_prediction), calculate_mcc(rf_labels, rf_prediction),
            calculate_f1(rf_labels, rf_prediction), calculate_recall(rf_labels, rf_prediction)))
        # print("RF 预测结果:", rf_prediction)
        return rf_prediction

    elif func_type == 'rnn':
        # RNN 模型训练和预测
        rnn_model = RNN(input_dim=10, hidden_dim=32)
        rnn_criterion = nn.CrossEntropyLoss()
        rnn_optimizer = optim.Adam(rnn_model.parameters(), lr=0.01)
        # 真实标签
        rnn_labels = torch.randint(0, 2, (100,)).long()

        rnn_optimizer.zero_grad()
        rnn_outputs = rnn_model(data_tensor)
        rnn_loss = rnn_criterion(rnn_outputs, rnn_labels)
        rnn_loss.backward()
        rnn_optimizer.step()

        rnn_prediction = torch.argmax(rnn_outputs, dim=1).detach().numpy()
        rnn_prediction = torch.from_numpy(rnn_prediction)
        print("RNN 准确率:{} ;\nMatthews相关系数: {} ;\nF1得分: {};\n召回率: {}\n".format(
            calculate_acc(rnn_labels, rnn_prediction), calculate_mcc(rnn_labels, rnn_prediction),
            calculate_f1(rnn_labels, rnn_prediction), calculate_recall(rnn_labels, rnn_prediction)))
        # print("RNN 预测结果:", rnn_prediction)
        return rnn_prediction

    elif func_type == 'cnn':
        # CNN 模型训练和预测
        cnn_model = CNN()
        cnn_criterion = nn.CrossEntropyLoss()
        cnn_optimizer = optim.Adam(cnn_model.parameters(), lr=0.01)
        # 真实标签
        cnn_labels = torch.randint(0, 2, (100,)).long()

        cnn_optimizer.zero_grad()
        cnn_outputs = cnn_model(data_tensor.unsqueeze(1))
        cnn_loss = cnn_criterion(cnn_outputs, cnn_labels)
        cnn_loss.backward()
        cnn_optimizer.step()

        cnn_prediction = torch.argmax(cnn_outputs, dim=1).detach().numpy()
        cnn_prediction = torch.from_numpy(cnn_prediction)
        print("CNN 准确率:{} ;\nMatthews相关系数: {} ;\nF1得分: {};\n召回率: {}\n".format(
            calculate_acc(cnn_labels, cnn_prediction), calculate_mcc(cnn_labels, cnn_prediction),
            calculate_f1(cnn_labels, cnn_prediction), calculate_recall(cnn_labels, cnn_prediction)))
        return cnn_prediction
    return null

# 调用
# result = functionSampling(func_type = 'cnn')






