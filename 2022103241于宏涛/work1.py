import random

"""
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1. 采用关键字参数作为随机数据结构及数量的输入；
2. 在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3. 其中随机数涵盖int，float和str三种类型。
"""


# 随机数据结构生成函数
def dataSampling(**kwargs):
    new_shape, type1 = kwargs.get('shape'), kwargs.get('type')
    print('我想要一个{}维度的随机数据，其中每个元素的类型是{}'.format(new_shape, type1))

    # 计算列表长度，即new_shape的每一个元素乘起来
    data_len = 1
    for _ in new_shape:
        data_len *= _

    # 根据type生成数据
    res = []
    for _ in range(data_len):
        tmp = []
        for data_type in type1:
            if data_type == int:
                tmp.append(random.randint(1, 100))
            elif data_type == float:
                tmp.append(round(random.uniform(0, 100), 3))
            elif data_type == str:
                tmp.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10))))
            else:
                print(f'unsupported data type: {data_type}')
        res.append(tmp)

    # print('当前获取的随机列表为{}, 我想要的维度是{}.'.format(res, new_shape))
    return reshape(res, new_shape)


def reshape(res, new_shape):
    new_len = len(res)

    if (len(new_shape) == 1):
        return res

    # 每次拿最后n个元素组成一个列表
    for n in new_shape[::-1]:
        # print("----------")
        lst = []
        for _ in range(new_len // n):   # 拿几次
            tmp = res[-n:]      # 切片，取最后n个元素
            # print("tmp:", tmp)
            lst.insert(0, tmp)  # 头插
            res = res[:-n]      # 剩下的切片重新赋值

        # print("lst:", lst)
        res = lst
        new_len //= n

    return res


# 调用示例
def main():
    results = dataSampling(shape=(3, 2, 2), type=(int, str, float, int))
    print(results)


if __name__ == '__main__':
    main()

