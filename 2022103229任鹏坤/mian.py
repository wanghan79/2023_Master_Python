from homework1 import HomeWork1
from homework2 import HomeWork2
from homework3 import HomeWork3
def main():
    while True:
        print("说明：")
        print(" 作业1对应数字1，作业2对应数字2，作业3对应数字3")
        print(" 输入e时表示退出")
        print("请按要求输入：")
        x=input("请输入1或者2或者3：")
            #执行平时作业3
        if x=='1':
            HomeWork1.dataSampling()
            print("==============================================================")
        elif x == "2":
            # 执行平时作业2
            HomeWork2.dataSampling()
            print("==============================================================")
        elif x== "3":
            # 执行平时作业3
            factory = HomeWork3.MLFactory()
            ml_model = factory.create_ml_model('SVM')
            ml_model.apply()
            print("==============================================================")
        elif x.lower() == "e":
            # 退出程序
            break
        else:
            print("无效的选项，请重新输入！")

if __name__ == '__main__':
    main()