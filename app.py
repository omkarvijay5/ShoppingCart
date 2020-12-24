from services.shopping_cart import calculate_total

from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=['POST'])
def shopping_cart():
    """
    example payload
    payload = {
        'currency_rate': 1,
        'shipping_charge': 0,
        'products': [
            {
                'name': 'T-shirt', 'price': 500,
                'discounts': [],
                'quantity': 2,
                'taxes': [{'amount': 18, 'type':'percentage'}]
            },
            {
                'name': 'Jacket', 'price': 2500,
                'discounts': [
                    {'amount': '50', 'type': 'percentage'}
                ],
                'quantity': 1,
                'taxes': [{'amount': 18, 'type':'percentage'}]
             },
            {
                'name': 'Shoes', 'price': 5000,
                'discounts': [{'amount': '10', 'type':'percentage'}], 'quantity': 1,
                'taxes': [{'amount': 18, 'type': 'percentage'}]
            },
        ]
    }
    :return: cart total
    """
    if request.method == 'POST':
        payload = request.get_json()
        total = str(calculate_total(payload))
        return total


if __name__ == "__main__":
    app.run()
