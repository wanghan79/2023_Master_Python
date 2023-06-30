# -*- coding: utf-8 -*-

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier


class MLFactory:
    def __init__(self, **kwargs) -> None:
        pass

    def __call__(self, *args, **kwargs) -> None:
        pass


class SVM(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        module = svm.SVC(kernel='linear')

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)


class RF(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        module = RandomForestClassifier()

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)


class CNN(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        return list()


class RNN(MLFactory):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, x_train, x_label, y_test, y_label) -> list:
        return list()
