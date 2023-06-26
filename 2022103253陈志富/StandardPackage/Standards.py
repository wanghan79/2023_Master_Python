import numpy as np


class Standards:
    def __init__(self, *args):
        self._standards = args

    def __call__(self, func):
        def wrapper(y_true, y_pred):
            results = []
            for standard in self._standards:
                if standard == "ACC":
                    result = self.ACC(y_true, y_pred)
                elif standard == "MCC":
                    result = self.MCC(y_true, y_pred)
                elif standard == "F1":
                    result = self.F1(y_true, y_pred)
                elif standard == "recall":
                    result = self.recall(y_true, y_pred)
                else:
                    print("Standard error!")
                results.append(result)
            return results
        return wrapper

    def ACC(self, y_true, y_pred):
        """
        Compute Accuracy.
        """
        correct = np.sum(y_true == y_pred)
        accuracy = float(correct) / len(y_true)
        return accuracy

    def MCC(self, y_true, y_pred):
        """
        Compute Matthews Correlation Coefficient.
        """
        tp = np.sum(np.logical_and(y_true == 1, y_pred == 1))
        tn = np.sum(np.logical_and(y_true == 0, y_pred == 0))
        fp = np.sum(np.logical_and(y_true == 0, y_pred == 1))
        fn = np.sum(np.logical_and(y_true == 1, y_pred == 0))

        numerator = (tp * tn - fp * fn)
        denominator = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        if denominator == 0:
            return 0
        else:
            return numerator / denominator

    def F1(self, y_true, y_pred):
        """
        Compute F1 score.
        """
        tp = np.sum(np.logical_and(y_true == 1, y_pred == 1))
        fp = np.sum(np.logical_and(y_true == 0, y_pred == 1))
        fn = np.sum(np.logical_and(y_true == 1, y_pred == 0))

        precision = tp / (tp + fp)
        recall = tp / (tp + fn)

        if precision + recall == 0:
            return 0
        else:
            f1 = 2 * precision * recall / (precision + recall)
            return f1

    def recall(self, y_true, y_pred):
        """
        Compute Recall.
        """
        tp = np.sum(np.logical_and(y_true == 1, y_pred == 1))
        fn = np.sum(np.logical_and(y_true == 1, y_pred == 0))

        recall = tp / (tp + fn)

        return recall