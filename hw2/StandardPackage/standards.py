import math


class standards(object):

    def __init__(self, *args):
        self._standard = args

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            results = list()
            for standard in self._standard:
                if standard == "ACC":
                    result = self.ACC(data)
                elif standard == "MCC":
                    result = self.MCC(data)
                elif standard == "F1":
                    result = self.F1(data)
                elif standard == "RECALL":
                    result = self.RECALL(data)
                else:
                    result = self.Recall(data)
            return results.append(result)
        return wrapper

    def ACC(self, data):
        if not data:
            return None
        tp = 0  # true positive
        tn = 0  # true negative
        fp = 0  # false positive
        fn = 0  # false negative
        for row in data:
            true_label = row[0]
            predicted_label = row[1]
            if true_label == predicted_label:
                if true_label == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if true_label == 1:
                    fn += 1
                else:
                    fp += 1
        acc = (tp + tn) / len(data)
        return acc

    def MCC(self, data):
        if not data:
            return None
        tp = 0  # true positive
        tn = 0  # true negative
        fp = 0  # false positive
        fn = 0  # false negative
        for row in data:
            true_label = row[0]
            predicted_label = row[1]
            if true_label == predicted_label:
                if true_label == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if true_label == 1:
                    fn += 1
                else:
                    fp += 1
        denominator = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
        if denominator == 0:
            return 0
        mcc = (tp * tn - fp * fn) / math.sqrt(denominator)
        return mcc

    def F1(self, data):
        if not data:
            return None
        tp = 0  # true positive
        tn = 0  # true negative
        fp = 0  # false positive
        fn = 0  # false negative
        for row in data:
            true_label = row[0]
            predicted_label = row[1]
            if true_label == predicted_label:
                if true_label == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if true_label == 1:
                    fn += 1
                else:
                    fp += 1
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        if precision + recall == 0:
            return 0
        f1 = 2 * precision * recall / (precision + recall)
        return f1

    def RECALL(self, data):
        if not data:
            return None
        tp = 0  # true positive
        tn = 0  # true negative
        fp = 0  # false positive
        fn = 0  # false negative
        for row in data:
            true_label = row[0]
            predicted_label = row[1]
            if true_label == predicted_label:
                if true_label == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if true_label == 1:
                    fn += 1
                else:
                    fp += 1
        if tp + fn == 0:
            return 0
        recall = tp / (tp + fn)
        return recall
