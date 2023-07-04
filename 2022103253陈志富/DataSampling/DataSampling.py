import random


def generate_random_data(**kwargs):
    try:
        # 获取关键字参数
        data_type = kwargs.get('data_type')
        data_range = kwargs.get('data_range')
        data_count = kwargs.get('data_count', 1)
        result = []
        # 判断数据范围是否为二元组，如果是则根据数据类型生成相应的随机数序列
        for _ in range(len(data_type)):
            if isinstance(data_range[_], tuple) and len(data_range[_]) == 2:
                if data_type[_] == int:
                    result.append([random.randint(data_range[_][0], data_range[_][1]) for i in range(data_count[_])])
                    continue
                elif data_type[_] == float:
                    result.append([random.uniform(data_range[_][0], data_range[_][1]) for i in range(data_count[_])])
                    continue
                elif data_type[_] == str:
                    result.append([''.join(random.SystemRandom().choice(data_range[_])) for i in range(data_count[_])])
                    continue
                else:
                    raise TypeError("Unsupported data type")
            else:
                raise ValueError("Invalid data range")
        return result
    except Exception as e:
        print("Error: ", str(e))

result=generate_random_data(**{'data_type': (int,str,float), 'data_range': ((0, 10),('a','xnnn'),(0,10)), 'data_count': (11,9,2)})
print(result)