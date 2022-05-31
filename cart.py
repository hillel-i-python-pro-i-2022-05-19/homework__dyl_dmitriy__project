from goods import Goods


class CartItem(object):
    # Корзина товаров
    def __init__(self, goods, count):
        self.goods = goods
        self.count = count

    def __str__(self):
        #  f является заполнителем для десятичного типа
        return '%s(￥%.2f)*%s' % (self.goods.name,
                                 self.goods.price, self.count)

        # Рассчитать подытог продукта

    def amout(self):
        return self.goods.price * self.count


if __name__ == '__main__':
    goods = Goods('Goods1', 2999, 100)
    # Создайте объект продукта корзины покупок, вам нужно передать объект продукта
    item = CartItem(goods, 2)
    money = item.amout()
    print(money)
