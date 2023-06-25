class standards():
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        self._func(*args, **kwargs)

    def ACC(self,data):
        pass
    def MCC(self,data):
        pass
    def F1(self,data):
        pass
    def recall(self,data):
        pass