from models.cart import Cart
from models.product import Product

shopping_cart = {}


def create_cart(currency_rate, shipping_charge=0):
    return Cart(currency_rate, shipping_charge)


def get_cart(currency_rate, shipping_charge=0):
    return create_cart(Cart(currency_rate, shipping_charge))


def calculate_total(context):
    cart = get_cart(currency_rate=context['currency_rate'],
                    shipping_charge=context['shipping_charge'])
    products = context['products']
    for p_dict in products:
        product = Product(name=p_dict['name'], price=p_dict['price'])
        cart.add_item(
            product=product,
            price=product.price,
            quantity=p_dict['quantity'],
            discounts=p_dict['discounts'],
            taxes=p_dict['taxes']
        )
    print("sub total ", cart.sub_total())
    print("total discount ", cart.total_discount())
    print("total tax ", cart.total_tax())
    print("total ", cart.total())
    print("cart total ", cart.total())
    return cart.total()
