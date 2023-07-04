from DataSampling.DataSampling import generate_random_data
from MLPackage.MLModels import MLModels
from StandardPackage.Standards import Standards
import factory

# work_2 Test
@Standards("MCC", "ACC")
@MLModels("SVM", "RF", "CNN")
def SentificTest(*args, **kwargs):
    result = generate_random_data(
        **{'data_type': (int, str, float), 'data_range': ((0, 10), ('a', 'xnnn'), (0, 10)), 'data_count': (11, 9, 2)})

    return result

def work_1():
    print("Work_1 Result:")
    result = generate_random_data(
        **{'data_type': (int, str, float), 'data_range': ((0, 10), ('a', 'xnnn'), (0, 10)), 'data_count': (11, 9, 2)})
    print(result)


def work_2():
    print("Work_2 Result:")
    SentificTest()


def work_3():
    # 调用示例
    factory.MLMethodFactory().create_ml_method("SVM", "CNN")
    factory.EvaluationMetricFactory().create_evaluation_metric("MCC")
    factory.DataStructureGenerator()


def run(number):
    if number == 1:
        work_1()
    elif number == 2:
        work_2()
    elif number == 3:
        work_3()
    else:
        print("Invalid number!")


def main():
    print("Welcome to the Test!")
    print("Please enter the number to run (1, 2, or 3), or enter 'q' to quit.")
    while True:
        user_input = input("Enter example number: ")
        if user_input == 'q':
            break
        try:
            run(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid example number or 'q' to quit.")
    print("886!")


if __name__ == '__main__':
    main()