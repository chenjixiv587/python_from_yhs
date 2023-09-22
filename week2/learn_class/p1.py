class Human(object):
    live = True

    def __init__(self, name):
        self.name = name


chen = Human('chen')
wei = Human('wei')

print(Human.live)
print(chen.name)
print(chen.live)
chen.live = False
print(chen.live)
print(Human.live)
print(Human.__dict__)
print(chen.__dict__)
