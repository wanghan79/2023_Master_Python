import homework1
import homework2
import homework3


def run():
    while True:
        id = input("请输入作业号: 1-3：")

        if id == "1":
            run_job1()
        elif id == "2":
            run_job2()
        elif id == "3":
            run_job3()
        else:
            print("无效的选项，请重新输入！")

def run_job1():
    print("作业1:")
    # 在这里调用作业1的函数和示例
    # 测试示例
    print(homework1.dataSampling(int=3))
    print(homework1.dataSampling(float=6, shape=(2, 3)))
    print(homework1.dataSampling(str=3))
    print(homework1.dataSampling(int=2, float=4, str=1))



def run_job2():
    print("作业2:")
    # 在这里调用作业2的函数和示例
    # 随机生成一些数据用于测试
    int_data = homework1.dataSampling(int=5)
    float_data = homework1.dataSampling(float=3)
    str_data = homework1.dataSampling(str=2)

    print("生成int型数据：", int_data)
    print("生成float型数据：", float_data)
    print("生成str数据：", str_data)

    # 使用修饰器进行机器学习操作和评价指标操作
    svm_rf_accuracy_mcc_result = homework2.svm_rf_accuracy_mcc([0, 1, 1, 0, 1, 1, 1, 0, 0, 0])
    print("使用SVM和RF：", svm_rf_accuracy_mcc_result)

    cnn_rf_svm_score_result = homework2.cnn_rf_svm_score([1, 0, 0, 1, 1, 1, 1, 1, 0, 0])
    print("使用CNN~RF~SVM：", cnn_rf_svm_score_result)


def run_job3():
    print("作业3:")
    # 在这里调用作业3的函数和示例
    svm_acc = homework3.Model_Factory()
    svm_acc_model = svm_acc.create_model('SVM', 'ACC')
    svm_acc_result = svm_acc_model.fit(homework3.dataSampling(int=5), [0, 1, 1, 0, 1])
    svm_acc_pred = svm_acc_model.predict(homework3.dataSampling(int=5))
    print("SVM的acc指标为：", svm_acc_result, svm_acc_pred)

    rf_mcc = homework3.Model_Factory()
    rf_mcc_model = rf_mcc.create_model('RF', 'MCC')
    rf_mcc_result = rf_mcc_model.fit(homework3.dataSampling(int=5), [0, 1, 1, 0, 1])
    rf_mcc_pred = rf_mcc_model.predict(homework3.dataSampling(int=5))
    print("RF的mcc指标为：", rf_mcc_result, rf_mcc_pred)

    cnn_f1 = homework3.Model_Factory()
    cnn_f1_model = cnn_f1.create_model('CNN', 'F1')
    cnn_f1_result = cnn_f1_model.fit(homework3.dataSampling(int=5), [0, 1, 1, 0, 1])
    cnn_f1_pred = cnn_f1_model.predict(homework3.dataSampling(int=5))
    print("CNN的F1指标为：", cnn_f1_result, cnn_f1_pred)


if __name__ == '__main__':
    run()
