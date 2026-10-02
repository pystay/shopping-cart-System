from models import Product, User

class CartItem:
    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    @property
    def subtotal(self):
        return self.product.product_price * self.quantity

class ShoppingCart:  #购物车类
    def __init__(self, user: User, catalog: dict):
        self.user = user
        self.catalog = catalog   #{商品ID：Product对象}
        self.items = []          #存 CartItem 对象
    #添加函数
    def add_item(self, product_id: str, quantity: int = 1):
        """
        加入购物车逻辑
        步骤：
        1，先检查 product_id是否在 self.catalog 里。 不在就返回ValueError
        2, 遍历 self.itmes, 看看这个商品是否已经在购物车里。
        3，如果已经存在，增加对应的 CartItem 的 quantity.
        4, 如果不存在， 创建新的 CartItem, 并追加到 self.Items.
        """
        if product_id not in self.catalog:  #检擦商品
            raise ValueError(f"该商品ID {product_id} 不存在！")

        product = self.catalog[product_id]

        for item in self.items:
            if item.product.product_id == product_id:
                #已存在，增加数量
                item.quantity += quantity
                return #添加完成后，返回结果

        new_item = CartItem(product, quantity)
        self.items.append(new_item)
    #删除函数
    def remove_item(self, product_id: str):
        '''移除商品'''
        for i, item in enumerate(self.items):
            if item.product.product_id == product_id:
                self.items.pop(i)
                return #找到并删除，最后返回函数

        #若找不到商品将返回错误
        raise ValueError(f"该商品ID {product_id} 未存在！")

    #计算系统
    def compute_total(self):
        '''计算购物车商品总价（原价）'''
        total = 0
        for item in self.items:
            total += item.subtotal
        return total

    #购物车展示
    def show_cart(self):
        '''打印购物车内容'''
        if not self.items:
            print("购物车未有需支付商品!!!")
            return

        print(f"=== {self.user.user_name} 的购物车 ===")
        for item in self.items:
            print(f"{item.product.product_name} x {item.quantity} = ￥{item.subtotal:.2f}")
            print(f"总价： ￥{self.compute_total():.2f}")
            print("================================")
