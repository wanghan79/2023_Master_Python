import random

def dataSampling(**kwargs):
    result = []
    for data_type, data_count in kwargs.items():
        if data_type == 'int':
            result.extend(random.sample(range(1, 100), data_count))
        elif data_type == 'float':
            result.extend([random.uniform(1, 100) for _ in range(data_count)])
        elif data_type == 'str':
            result.extend([''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5)) for _ in range(data_count)])
    return result

def main():
    while True:
        print("请输入要展示的作业号（1、2或3），输入q退出：")
        command = input()
        if command == 'q':
            break
        elif command == '1':
            int_num = int(input("请输入需要随机生成的int数量："))
            float_num = int(input("请输入需要随机生成的float数量："))
            str_num = int(input("请输入需要随机生成的str数量："))
            result = dataSampling(int=int_num, float=float_num, str=str_num)
            print(result)
        elif command == '2':
            break
        elif command == '3':
            break
        else:
            print("无效的命令，请重新输入。")


if __name__ == '__main__':
    main()
