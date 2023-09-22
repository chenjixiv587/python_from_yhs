class Customer:
    def __init__(self, name, goods=None):
        self.name = name
        if goods is None:
            goods = []
        self.goods = goods

    def buy(self, goods_name):
        self.goods.append(goods_name)

    def pay(self):
        for good in self.goods:
            print(good)


c1 = Customer('chen')
c1.buy('apple')
c1.pay()

c2 = Customer('wei')
c2.buy('pinapple')
c2.pay()
