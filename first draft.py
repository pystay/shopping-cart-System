#用户
class User:
    def __init__(self, user_name, user_id): #名字，对应id
        self.user_name = user_name
        self.user_id = user_id
    def __str__(self):
        return f"用户名：{self.user_name} | ID：{self.user_id}"
#商品
class Product:
    def __init__(self,product_name, product_id, product_price, product_numbers ,product_shop_id):
        self.product_name = product_name #商品名称
        self.product_id = product_id     #商品ID
        self.product_price = product_price #商品价格
        self.product_numbers = product_numbers #商品数量
        self.product_shop_id = product_shop_id #商品所属商家ID
    def __str__(self):
        return (f"商品名称：{self.product_name}\n"
                f" 商品ID: {self.product_id}\n"
                f"商品价格：{self.product_price}\n"
                f" 商品数量：{self.product_numbers}\n"
                f"商品所属商家ID：{self.product_shop_id}")

class ShoppingCart:
    def __init__(self):
        self.items = {} #商品ID，数量

    def add_item(self,product_id:int, quantity: int = 1):
        #加入购物车逻辑
        pass