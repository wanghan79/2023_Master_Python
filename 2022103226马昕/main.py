import homework1
import homework2
import homework3

def run_homework(homework_number):
    if homework_number == 1:
        print("Running Homework 1:")
        int_data=homework1.dataSampling(int={'start': 1, 'end': 100, 'num': 10})
        print("Integer data:", int_data)
        float_data=homework1.dataSampling(float={'start': 0, 'end': 1, 'num': 5})
        print("Float data:", float_data)
        str_data=homework1.dataSampling(str={'length': 5, 'num': 3})
        print("String data:", str_data)
    elif homework_number == 2:
        print("Running Homework 2:")
        int_data = homework2.dataSampling(int={'start': 1, 'end': 100, 'num': 10})
        print("Integer data:", int_data)
        float_data = homework2.dataSampling(float={'start': 0, 'end': 1, 'num': 5})
        print("Float data:", float_data)
        str_data = homework2.dataSampling(str={'length': 5, 'num': 3})
        print("String data:", str_data)
    elif homework_number == 3:
        print("Running Homework 3:")
        int_data = homework3.dataSampling(int={'start': 1, 'end': 100, 'num': 10})
        print("Integer data:", int_data)
        float_data = homework3.dataSampling(float={'start': 0, 'end': 1, 'num': 5})
        print("Float data:", float_data)
        str_data = homework3.dataSampling(str={'length': 5, 'num': 3})
        print("String data:", str_data)
    else:
        print("Invalid homework number.")

if __name__ == "__main__":
    while True:
        try:
            homework_number = int(input("Please enter the homework number (1, 2, or 3): "))
            run_homework(homework_number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid homework number.")
