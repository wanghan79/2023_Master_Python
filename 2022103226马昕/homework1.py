import random
import string

def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == "int":
            result.extend(random.sample(range(value['start'], value['end'] + 1), value['num']))
        elif key == "float":
            result.extend([random.uniform(value['start'], value['end']) for _ in range(value['num'])])
        elif key == "str":
            result.extend([''.join(random.choices(string.ascii_letters + string.digits, k=value['length'])) for _ in range(value['num'])])
    return result
# 生成10个范围在1到100之间的整数
int_data = dataSampling(int={'start': 1, 'end': 100, 'num': 10})
print("Integer data:", int_data)

# 生成5个范围在0到1之间的浮点数
float_data = dataSampling(float={'start': 0, 'end': 1, 'num': 5})
print("Float data:", float_data)

# 生成3个长度为5的随机字符串
str_data = dataSampling(str={'length': 5, 'num': 3})
print("String data:", str_data)
