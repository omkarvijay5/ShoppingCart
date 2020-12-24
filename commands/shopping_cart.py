from services.shopping_cart import calculate_total


def fetch_taxes():
    taxes = []
    tax_count = input("Enter number of taxes to be applied. Press Enter for default 18% GST:")
    if tax_count:
        for k in range(int(tax_count)):
            input("Please enter the tax %s details " % (k + 1))
            amount = int(input("Enter Amount:"))
            tax_type = int(input("Enter the type.\n1. percentage\n 2. amount:"))
            tax_dict = {'amount': amount, 'type': tax_type}
            taxes.append(tax_dict)
    else:
        taxes.append({'amount': 18, 'type': 'percentage'})
    return taxes


def fetch_discounts():
    discounts = []
    discount = input("Enter number of discounts to be applied. Press Enter for no discounts:")
    if discount:
        for j in range(int(discount)):
            print("Please enter the discount %s details " % (j + 1))
            amount = int(input("Enter Amount:"))
            discount_type = int(input("Enter the type.\n1. percentage\n2. amount:\n"))
            discount_type = 'percentage' if discount_type == 1 else 'amount'
            discounts.append({'amount': amount, 'type': discount_type})
    return discounts


def build_cart_context():

    print("Please enter the Shopping Cart details:")
    n = int(input("Enter total number of products in the cart:"))
    context = {
        'currency_rate': 1,
        'shipping_charge': 0,
        'products': []
    }
    for i in range(n):
        print("Please enter product %s details" % (i+1))
        name = input("Product Name:")
        price = int(input("Product price:"))
        quantity = int(input("Quantity:"))
        product_dict = {'name': name, 'price': price, 'quantity': quantity}
        discounts = fetch_discounts()
        taxes = fetch_taxes()
        product_dict['discounts'] = discounts
        product_dict['taxes'] = taxes
        context['products'].append(product_dict)
    return context


def main():
    context = build_cart_context()
    print(calculate_total(context))


if __name__ == "__main__":
    main()

