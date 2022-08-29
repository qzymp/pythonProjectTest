class Goods:
    @property
    def price(self):
        return 'laowang'

obj = Goods()

# 自动执行 @property 修饰的方法，
result = obj.price

print(result)

