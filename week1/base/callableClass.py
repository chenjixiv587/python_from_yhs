class ClassFunc:
    def __call__(self):
        return "func called"


cf = ClassFunc()
cf()
cf2 = cf


def func():
    pass


print(dir(func))
"""
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__',
 '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', 
 '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', 
 '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', 
 '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""
