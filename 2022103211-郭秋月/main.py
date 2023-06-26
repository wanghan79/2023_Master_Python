"""
结课作业：
建立完整项目工程，将三次平时作业集成在一个工程中，实现控制台交互，提示用户输入要求展示的作业号（1、2或3），自动运行相应作业示例，并将结果输出到控制台。
"""

import MasterJob1
import MasterJob2
import MasterJob3


def example1():
    print("Job 1 Result:", MasterJob1.dataSampling(int=100, float=10.0, str=5))


def example2():
    print("Job 2 Result:", MasterJob2.dataSampling(int=50, float=5.0, str=3))


def example3():
    MasterJob3.MLMethodFactory().create_ml_method("RF")
    MasterJob3.EvaluationMetricFactory().create_evaluation_metric("F1")
    print("Job 3 Result:", MasterJob3.DataStructureGenerator(int=200, float=20.0, str=8).get_data_structure())


def run_example(example_number):
    if example_number == 1:
        example1()
    elif example_number == 2:
        example2()
    elif example_number == 3:
        example3()
    else:
        print("Invalid example number!")


def main():
    print("Please enter the job number to run (1, 2, or 3), or enter 'q' to quit.")
    while True:
        user_input = input("Enter job number: ")
        if user_input == 'q':
            break
        try:
            run_example(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid job number or 'q' to quit.")
    print("End")


if __name__ == '__main__':
    main()

