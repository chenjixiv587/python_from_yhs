def outer(func):
    def inner(a, b):
        print(f'the first is {a}')
        result = func(a, b)
        print(f'the second is {b}')
        return result
    return inner


@outer
def add_two(a, b):
    return a + b


print(add_two(1, 2))
