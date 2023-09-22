
class Human(object):
    def __init__(self, name) -> None:
        self.name = name
        self.age = 18
    # 对属性进行拦截

    def __getattr__(self, item):
        """如果调用属性的时候，没有这个属性，就返回这个方法里面的值"""
        print("the default thing.")

    def __getattribute__(self, item):
        # 优先级最大
        # 属性存在或者不存在 都会经过 __getattribute__
        """调用属性的时候  如果没有 就会抛出异常"""
        print('__getattribute__')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100


h1 = Human('chen')
h1.fly  # the default thing.
h1.name
