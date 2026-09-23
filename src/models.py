#用户
class User:
    def __init__(self, user_name:str, user_id:str): #名字，对应id
        self.user_name = user_name
        self.user_id = user_id
    def __str__(self):
        return f"用户名：{self.user_name} | ID：{self.user_id}"
#商品
class Product:
    def __init__(self,product_name, product_id, product_shop_id,product_price, product_numbers):
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
    def __repr__(self):
        return f"Product({self.product_name!r}, id={self.product_id!r})y"

class Admin:
    def __init__(self, admin_name, admin_id):
        self.admin_name = admin_name
        self.admin_id = admin_id
    def __str__(self):
        return (f"=======================管理员模式=======================\n"
                f"|管理员账户:{self.admin_name} | 管理员ID：{self.admin_id}|\n"
                f"======================================================")

class Merchant:
    def __init__(self, merchant_name, merchant_id):
        self.merchant_name = merchant_name
        self.merchant_id = merchant_id
    def __str__(self):
        return (f"************************商家平台*************************\n"
                f"|商家名：{self.merchant_name} | 商家ID:{self.merchant_id}|\n"
                f"*******************************************************")
