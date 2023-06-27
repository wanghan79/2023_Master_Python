from task1 import dataSampling
from task2 import processRandomData
from task3 import   processRandomML

def main():
    while True:
        print("Please enter the job number (1, 2, or 3):")
        job_number = input()
        
        if job_number == '1':
            print("Running Job 1:")
            result = dataSampling(
                int_data=(int, (1, 100)),
                float_data=(float, (0.0, 1.0)),
                str_data=(str, (5, 10))
            )
            print("Result:", result)
        elif job_number == '2':
            result=processRandomData(
            (int, (1, 100)),
            (float, (0.0, 1.0)),
            (str, (5, 10))
             )
            print("Result:", result)
        elif job_number == '3':
            print("Running Job 3:")
            result=processRandomML(
                (int, (1, 100)),
                (float, (0.0, 1.0)),
                (str, (5, 10))
            )
            print("Result:", result)
        else:
            print("Invalid job number. Please try again.")
        
        print("----------------------------")


if __name__ == '__main__':
    main()
