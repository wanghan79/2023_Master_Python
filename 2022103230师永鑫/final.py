import importlib
def run_part(part_num):
    module_name = f"part{part_num}"
    try:
        module = importlib.import_module(module_name)
        module.run()
    except ModuleNotFoundError:
        print(f"第{part_num}次作业尚未完成")

if __name__ == '__main__':
    while True:
        part_num = int(input("请输入作业号（1、2或3），输入0退出："))

        if part_num == 0:
            print("程序已退出。")
            break
        run_part(part_num)


