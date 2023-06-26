import project1
import project2
import project3


def show_menu():
    print("请选择要展示的作业号:")
    print("1. 作业1 - 随机数据结构生成函数")
    print("2. 作业2 - 修饰器技术")
    print("3. 作业3 - 类工厂设计模式")
    print("0. 退出")


def run_job1():
    print("运行作业1示例:")
    # 在这里调用作业1的函数和示例
    # 测试示例
    print(project1.dataSampling(int=3))
    print(project1.dataSampling(float=3))
    print(project1.dataSampling(str=3))
    print(project1.dataSampling(int=2, float=4, str=1))



def run_job2():
    print("运行作业2示例:")
    # 在这里调用作业2的函数和示例
    # 随机生成一些数据用于测试
    int_data = project1.dataSampling(int=5)
    float_data = project1.dataSampling(float=3)
    str_data = project1.dataSampling(str=2)

    print("随机 int 数据：", int_data)
    print("随机 float 数据：", float_data)
    print("随机 str 数据：", str_data)

    # 使用修饰器进行机器学习操作和评价指标操作
    svm_rf_accuracy_mcc_result = project2.svm_rf_accuracy_mcc([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
    print("SVM + RF 精度评估：", svm_rf_accuracy_mcc_result)

    cnn_rf_svm_score_result = project2.cnn_rf_svm_score([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
    print("CNN + RF + SVM 评价指标：", cnn_rf_svm_score_result)


def run_job3():
    print("运行作业3示例:")
    # 在这里调用作业3的函数和示例
    svm_acc_factory = project3.ModelFactory()
    svm_acc_model = svm_acc_factory.create_model('SVM', 'ACC')
    svm_acc_result = svm_acc_model.fit(project3.dataSampling(int=5), [1, 0, 1, 1, 0])
    svm_acc_pred = svm_acc_model.predict(project3.dataSampling(int=5))
    print("SVM + ACC：", svm_acc_result, svm_acc_pred)

    rf_mcc_factory = project3.ModelFactory()
    rf_mcc_model = rf_mcc_factory.create_model('RF', 'MCC')
    rf_mcc_result = rf_mcc_model.fit(project3.dataSampling(int=5), [1, 0, 1, 1, 0])
    rf_mcc_pred = rf_mcc_model.predict(project3.dataSampling(int=5))
    print("RF + MCC：", rf_mcc_result, rf_mcc_pred)

    cnn_f1_factory = project3.ModelFactory()
    cnn_f1_model = cnn_f1_factory.create_model('CNN', 'F1')
    cnn_f1_result = cnn_f1_model.fit(project3.dataSampling(int=5), [1, 0, 1, 1, 0])
    cnn_f1_pred = cnn_f1_model.predict(project3.dataSampling(int=5))
    print("CNN + F1：", cnn_f1_result, cnn_f1_pred)


while True:
    show_menu()
    choice = input("请输入作业号: ")

    if choice == "1":
        run_job1()
    elif choice == "2":
        run_job2()
    elif choice == "3":
        run_job3()
    else:
        print("无效的选项，请重新输入！")
