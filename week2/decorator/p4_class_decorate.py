from functools import wraps


class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs) -> None:
        pass

    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def inner():
            pass
        return inner
