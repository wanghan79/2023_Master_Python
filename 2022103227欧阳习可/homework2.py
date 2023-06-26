import random


# 修饰器函数，用于选择机器学习方法
def ml_method_decorator(ml_method):
    def wrapper(random_data_func):
        def decorated_func(*args, **kwargs):
            # 生成随机数据
            data = random_data_func(*args, **kwargs)

            # 使用机器学习方法进行操作
            if ml_method == 'SVM':
                # 执行SVM操作
                print("执行SVM操作")
            elif ml_method == 'RF':
                # 执行Random Forest操作
                print("执行Random Forest操作")
            elif ml_method == 'CNN':
                # 执行CNN操作
                print("执行CNN操作")
            elif ml_method == 'RNN':
                # 执行RNN操作
                print("执行RNN操作")
            else:
                print("未知的机器学习方法")

            return data

        return decorated_func

    return wrapper


# 修饰器函数，用于选择验证指标操作
def metric_decorator(metric):
    def wrapper(random_data_func):
        def decorated_func(*args, **kwargs):
            # 生成随机数据
            data = random_data_func(*args, **kwargs)

            # 执行验证指标操作
            if metric == 'ACC':
                # 计算准确率
                print("计算准确率")
            elif metric == 'MCC':
                # 计算MCC
                print("计算MCC")
            elif metric == 'F1':
                # 计算F1值
                print("计算F1值")
            elif metric == 'RECALL':
                # 计算召回率
                print("计算召回率")
            else:
                print("未知的验证指标")

            return data

        return decorated_func

    return wrapper


# 随机数据结构生成函数
models = ['SVM','RF','CNN','RNN']
metrics = ['ACC','MCC','F1','RECALL']
@ml_method_decorator(random.choice(models))
@metric_decorator(random.choice(metrics))
def generate_random_data_structure(num_samples):
    data = []
    for _ in range(num_samples):
        data.append(random.randint(0, 10))
    return sum(data)
# 调用示例
data = generate_random_data_structure(5)
print(data)
