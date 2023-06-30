from task1 import datasampling
from task2 import decorator
from task3 import factory
from pprint import pprint

def run_homework(homework_number):
    if homework_number == 1:
        pprint(f"平时作业1的结果:{datasampling.result}")
    elif homework_number == 2:
        pprint(f"平时作业2的结果:{decorator.result}")
    elif homework_number == 3:
        data = factory.data_sampling.generate_data()
        print(data)
        factory.ml_package.execute(data)
        factory.verify_package.evaluate(data)
    else:
        print("无效的作业号")

if __name__ == '__main__':
    while True:
        homework_number = int(input("请输入要展示的作业号（1、2或3），输入0退出："))
        if homework_number == 0:
            break
        run_homework(homework_number)