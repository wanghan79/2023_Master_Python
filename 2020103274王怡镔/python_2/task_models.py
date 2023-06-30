# -*- coding: utf-8 -*-


from functools import wraps

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier


class MyModels:
    def __init__(self, *args):
        self._model = args

    def __call__(self, func):
        models = self._model

        @wraps(func)
        def wrapper(*args, **kwargs):
            x_trn, x_lab, y_tst, y_lab = func(*args, **kwargs)
            pred_labels = list()
            for mod in models:
                if mod == 'svm':
                    label = self.svm(x_trn, x_lab, y_tst, y_lab)
                elif mod == 'rf':
                    label = self.rf(x_trn, x_lab, y_tst, y_lab)
                elif mod == 'cnn':
                    label = self.cnn()
                elif mod == 'rnn':
                    label = self.rnn()
                else:
                    return 'Sorry, there is an unsupported model in your input. Stay tuned'
                pred_labels.append(label)
            return models, pred_labels, y_lab

        return wrapper

    def svm(self, x_train, x_label, y_test, y_label):
        module = svm.SVC(kernel='linear')

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)

    def rf(self, x_train, x_label, y_test, y_label):
        module = RandomForestClassifier()

        module.fit(x_train, x_label)
        module.fit(y_test, y_label)

        return module.predict(y_test)

    def cnn(self):
        return list()

    def rnn(self):
        return list()
