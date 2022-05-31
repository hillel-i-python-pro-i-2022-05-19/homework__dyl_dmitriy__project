# goods
class Goods(object):
    def __init__(self, name, price, stock):
        self.id = 0
        self.name = name
        self.price = price
        self.stock = stock
        # content output

    def __str__(self):
        return 'id:s\n' \
               'name: s \ n' \
               'price: s \ n' \
               'id: s \ n' % (self.id, self.name, self.price,
                                      self.stock)


if __name__ == '__main__':
    goods = Goods('Goods1', 2999, 100)
    print(goods)
    goods2 = Goods('Goods2', 3666, 100)
    print(goods2)
