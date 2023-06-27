import numpy as np


class Sampling:
    def __init__(self, nums, n):
        self.nums = nums
        self.n = n

    def generate(self):
        xData = np.random.random((self.nums, self.n))  # 随机生成输入数据
        yData = np.random.randint(2, size=self.nums)   # 随机生成标签数据
        return xData, yData
