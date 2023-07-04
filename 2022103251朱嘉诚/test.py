def namedDecorator(name):
    def run_time(func):
        def wrap(a, b):
            print('this is:{}'.format(name))
            r = func(a, b)
            return r
        return wrap
    return run_time

@namedDecorator("装饰器带参数")
def foo(a, b):
    return a + b

print(foo(2, 45))
