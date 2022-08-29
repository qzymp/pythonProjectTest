class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    # @price.getter
    # def original_price(self):
    #     return self.original_price

goods = Goods()
print(goods.price)
goods.price = 200
print(goods.price)


