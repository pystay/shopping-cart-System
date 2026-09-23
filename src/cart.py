from models import Product, User

class CartItem:
    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    @property
    def subtotal(self):
        return self.product.product_price * self.quantity