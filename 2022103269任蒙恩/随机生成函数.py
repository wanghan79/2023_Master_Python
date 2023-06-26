import random
import string

def generate_random(data_type, num=1, **kwargs):
    """
    生成随机数据的函数

    Parameters:
        data_type: str，要生成的数据类型，包括'int', 'float', 'str'。
        num: int，要生成的数据个数，默认为1。
        kwargs: dict，根据不同数据类型，可接受不同的参数，包括'int'类型的'start'和'end'，
                'float'类型的'start'和'end'，'str'类型的'length'。

    Returns:
        生成的随机数据，根据不同的数据类型返回不同类型的数据。
    """
    try:
        if data_type == 'int':
            start = kwargs.get('start', 0)
            end = kwargs.get('end', 100)
            return random.randint(start, end)
        elif data_type == 'float':
            start = kwargs.get('start', 0.0)
            end = kwargs.get('end', 1.0)
            return random.uniform(start, end)
        elif data_type == 'str':
            length = kwargs.get('length', 5)
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        else:
            raise ValueError("Invalid data type: {}".format(data_type))
    except Exception as e:
        print("Error: {}".format(e))


# 生成一个整数
num1 = generate_random('int')
print(num1)
# 生成10个整数
num_list = [generate_random('int') for _ in range(10)]
print(num_list)
# 生成一个浮点数
float1 = generate_random('float')
print(float1)
# 生成一个长度为10的随机字符串
str1 = generate_random('str', length=10)
print(str1)
