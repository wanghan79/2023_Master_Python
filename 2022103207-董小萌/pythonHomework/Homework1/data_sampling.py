import random

# 平时作业1：
# 实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
# 1.采用关键字参数作为随机数据结构及数量的输入；
# 2.在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
# 3.其中随机数涵盖int，float和str三种类型。



def data_sampling(**kwargs):
    result = []
    for k, v in kwargs.items():
        if k == 'int':
            item = random.randint(0, v)
            result.append(item)
            continue
        elif k == 'float':
            item = random.uniform(0, v)
            result.append(item)
            continue
        elif k == 'str':
            result=''.join(random.choice(v))
            continue
        else:
            continue
    return result

if __name__ == '__main__':
    # kwargs = {'int': 12}
    # kwargs = {'str':['x','y','z','123']}
    kwargs = {'float': 12.5}
    result = data_sampling(** kwargs)
    print(result)