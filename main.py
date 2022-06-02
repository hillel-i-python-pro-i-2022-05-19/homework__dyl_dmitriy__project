from cart import CartItem
from goods import Goods


class Shop(object):
    "" "Keep" ""


def __init__(self):
    # Keep all goods
    self.shops = []
    # goods store
    self.cart = []
    # load product
    self.load()


def load(self):
    "" "Keep goods" ""


self.add(Goods('Goods1', 3299, 100))
self.add(Goods('Goods2', 1288, 100))
self.add(Goods('Goods3', 1299, 100))
self.add(Goods('Goods4', 6288, 100))


def add(self, good):
    """
             New item identifire
             : param good: New good
    :return: None
    """
    good.id = len(self.shops) + 1
    self.shops.append(good)


def print_line(self):
    print('-' * 50)


def print_double_line(self):
    print('=' * 50)


def list(self):
    "" "Product list" ""
    print("Product selection:")
    self.print_double_line()
    # product list
    for g in self.shops:
        print("%s       %s        %s" % (g.id, g.name, g.price))
        self.print_line()

    def list_cart(self):
        "" "product list total cost" ""

    self.print_line()
    total = 0.0
    for item in self.cart:
        print('%s     =￥%s' % (item, item.amout()))
        total += item.amout()
    self.print_line()
    print("total amount: ￥ % .2
    f" total)

    def add_to_cart(self):
        "" "add item to cart" ""

    print('\n')
    g_id = input(
        'product id:')

    if len(g_id) == 0:
        # check
        total = 0.0
        for item in self.cart:
            total += item.amout()
        self.print_line()
        print("bill payment:.% .2
        f " total)

        # empty
        self.cart.clear()
        print("successful payment!")


        elif g_id == '0':
        self.cart.clear()
        print("Cart is empty!")
        else:
        # product id
        idx = int(g_id) - 1
        # take out
        goods = self.shops[idx]
        self.print_line()
        print(goods)

        count = int(input('enter purchase:'))
        # availability
    while count > goods.stock:
        count = int(input('reintroduce:'))

    # change item
    is_exsts = False
    for item in self.cart:
        if item.goods == goods:
            # reduce item in cart
            is_exsts = True
            item.count += count
            # decrease
            goods.stock -= count

    if is_exsts == False:
        # add product
        goods.stock -= count
        self.cart.append(CartItem(goods, count))

        # total cost
    self.list_cart()

    def run(self):
        "" "application launch" ""
        print(«shop online»)
        print('v1.0')
        print('\n')

        self.list()

        while True:
            self.add_to_cart()

        shop = Shop()
        shop.run()
