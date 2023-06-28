from homework1.DataModule import dataSampling
from homework3.Factory import FactoryML
from homework2.MLModule import generate_random_data_svm,generate_random_data_rf,generate_random_data_cnn,generate_random_data_rnn
from homework2.MLModule import functionSampling

if __name__ == "__main__":
    choice_homework = input("请输入要检查的作业(1、2、3)：")
    if_continue = '1'
    while if_continue != '0':
        if choice_homework == '1':
            data_type = input("此作业要求输入类型(int、float、str)：")
            if (data_type == 'int') or (data_type == 'float') or (data_type == 'str'):
                length = input("输入长度：")
                if length.isdigit():
                    dataSampling(data_type = data_type ,length = length)
            else:
                print("输入类型错误")

        elif choice_homework == '2':
            func_type = input("选择模型类型(rnn、cnn、rf、svm)：")
            if func_type == 'rnn':
                generate_random_data_rnn()
            elif func_type == 'cnn':
                generate_random_data_cnn()
            elif func_type == 'rf':
                generate_random_data_rf()
            elif func_type == 'svm':
                generate_random_data_svm()
            else:
                print("输入类型错误")

        elif choice_homework == '3':
            model_list = FactoryML("homework3/config.txt")
            for i in model_list:
                functionSampling(i)
        else:
            choice_homework = input("请输入要检查的作业(1、2、3)：")
            continue

        if_continue = input("是否继续 0退出 其他继续：")
        if if_continue != '0':
            choice_homework = input("请输入要检查的作业(1、2、3)：")

    print("检查完毕")