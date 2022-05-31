from goods import Goods


class CartItem(object):
    # shopping cart
    def __init__(self, goods, count):
        self.goods = goods
        self.count = count

    def __str__(self):
        #   decimal type
        return '%s(￥%.2f)*%s' % (self.goods.name,
                                 self.goods.price, self.count)

        # shopping carttotal goods

    def amout(self):
        return self.goods.price * self.count


if __name__ == '__main__':
    goods = Goods('Goods1', 2999, 100)
    # product object
    item = CartItem(goods, 2)
    money = item.amout()
    print(money)
