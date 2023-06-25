import subprocess

def run_python_file(file_path):
    """
    运行指定的Python文件，并捕获其输出结果。

    Parameters:
        file_path: str，要运行的Python文件的路径。

    Returns:
        运行结果的标准输出。
    """
    result = subprocess.run(["python", file_path], capture_output=True, text=True)
    return result.stdout


def main():
    print("Welcome to the Random Data Generation Tool!")
    print("Please enter the number of the job you want to run:")
    print("1. Generate a random integer")
    print("2. Generate a list of random floats")
    print("3. Generate a random string")

    while True:
        try:
            job_number = int(input("Enter job number (1/2/3): "))
            if job_number in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter a valid job number.")
        except ValueError:
            print("Invalid input. Please enter a valid job number.")

    file_path = None

    if job_number == 1:
        file_path = "随机生成函数.py"
    elif job_number == 2:
        file_path = "修饰器.py"
    elif job_number == 3:
        file_path = "工厂.py"

    if file_path:
        result = run_python_file(file_path)
        print("Job output:")
        print(result)
    else:
        print("Invalid job number. No file to run.")


if __name__ == '__main__':
    main()
