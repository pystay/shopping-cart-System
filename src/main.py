from models import User, Product
from cart import ShoppingCart, CartItem

if __name__ == '__main__':
    user = User("pystay", 1001)
    product1 = Product("Python_Learn_Book", 101,5001,19.9,10)
    product2 = Product("MEIZU20", 102, 5002,1899.9,20)


    catalog = {product1.product_id: product1, product2.product_id:product2}
    cart = ShoppingCart(user, catalog)

    cart.add_item(101, 2)
    cart.add_item(102, 1)
    cart.add_item(101, 1) #重复购买
    print(f"购物车商品总价：{cart.compute_total():.2f}")
    print(len(cart.items))

    cart.remove_item(101)
    print(len(cart.items))