import numpy as np


class Sampling:
    def __init__(self, nums, n):
        self.nums = nums
        self.n = n

    def create(self):
        x_data = np.random.random((self.nums, self.n))
        y_data = np.random.randint(2, size=len(x_data))
        return x_data, y_data
