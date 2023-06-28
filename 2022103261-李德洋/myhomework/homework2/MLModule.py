from MLPackage.ML_Functions import functionSampling
# 定义一个修饰器函数
def random_data_decorator(ml_method):
    # 内部函数，用于包装原始的随机数据结构生成函数
    def wrapper(func):
        # 在函数调用前的操作
        def inner_function(*args, **kwargs):
            # 机器学习方法操作
            if ml_method == 'SVM':
                # 执行 SVM 操作
                svm_result = functionSampling(func_type='svm')
            elif ml_method == 'RF':
                # 执行 RF 操作
                rf_result = functionSampling(func_type='rf')
            elif ml_method == 'CNN':
                # 执行 CNN 操作
                cnn_result = functionSampling(func_type='cnn')
            elif ml_method == 'RNN':
                # 执行 RNN 操作
                rnn_result = functionSampling(func_type='rnn')

            # 调用原始函数
            return func(*args, **kwargs)

        # 返回内部函数
        return inner_function

    # 返回修饰器函数
    return wrapper

# 定义一个原始的随机数据结构生成函数
def generate_random_data():
    # 生成随机数据的逻辑
    pass

# 调用修饰器函数修饰原始函数
@random_data_decorator(ml_method='SVM')
def generate_random_data_svm():
    return generate_random_data()

@random_data_decorator(ml_method='RF')
def generate_random_data_rf():
    return generate_random_data()

@random_data_decorator(ml_method='CNN')
def generate_random_data_cnn():
    return generate_random_data()

@random_data_decorator(ml_method='RNN')
def generate_random_data_rnn():
    return generate_random_data()

# 调用修饰后的函数
# svm_data = generate_random_data_svm()
# rf_data = generate_random_data_rf()
# cnn_data = generate_random_data_cnn()
# rnn_data = generate_random_data_rnn()
