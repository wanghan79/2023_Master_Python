import random
import string

def dataSampling(**kwargs):
    """
       生成指定形状和数据类型的数据样本
       参数:
       shape (list): 数组的形状，默认为 [1, ]
       data_type (list): 数据类型，默认为 ["int"]
       返回:
       生成的数据样本
       异常:
       ValueError: 如果参数值不合法
       示例:
       >>> result = dataSampling(shape=[3,], data_type=['float'])
       >>> print(result)
       [-7.14, -76.37, 32.9]
       """
    shape=kwargs.get("shape",[1,])
    data_type = kwargs.get("data_type", ["int"])
    for i in shape:
        if i<0:
            raise ValueError("shape参数不能为负数")
        elif i==0:
            raise ValueError("shape参数不能为0")

    return _generate_data(shape,data_type)

def _generate_data(shape, data_type):
    if len(shape) == 0:
        if len(data_type) == 1:
            if data_type[0] == "int":
                return (random.randint(-100, 100))
            elif data_type[0] == "float":
                return (round(random.uniform(-100.0, 100.0), 2))
            elif data_type[0] == "str":
                return (''.join(random.choices(string.ascii_letters, k=8)))
            else:
                raise ValueError("data_type参数类型应该是整形，浮点型，字符型")
        else:
            res = []
            for i in range(len(data_type)):
                if data_type[i] == "int":
                    res.append(random.randint(-100, 100))
                elif data_type[i] == "float":
                    res.append(round(random.uniform(-100.0, 100.0), 2))
                elif data_type[i] == "str":
                    res.append(''.join(random.choices(string.ascii_letters, k=8)))
                else:
                    raise ValueError("data_type参数类型应该是整形，浮点型，字符型")
            return res
    else:
        return [_generate_data(shape=shape[1:], data_type=data_type) for _ in range(shape[0])]



def main():
    print(dataSampling(shape=[3, ], data_type=['float']))
    print(dataSampling(shape=[3, 4], data_type=['int']))
    print(dataSampling(shape=[2, 3], data_type=['int', 'str']))

if __name__ == '__main__':
    main()








