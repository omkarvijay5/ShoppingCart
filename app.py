from services.shopping_cart import calculate_total

from flask import Flask, request, Response
app = Flask(__name__)


@app.route("/", methods=["POST"])
def shopping_cart():
    """
    example payload
    payload = {
        "currency_rate": 1,
        "products": [
            {
                "discounts": [
                ],
                "name": "T-shirt",
                "price": 500,
                "quantity": 2,
                "taxes": [
                    {
                        "amount": 18,
                        "type": "percentage"
                    }
                ]
            },
            {
                "discounts": [
                    {
                        "amount": "50",
                        "type": "percentage"
                    }
                ],
                "name": "Jacket",
                "price": 2500,
                "quantity": 1,
                "taxes": [
                    {
                        "amount": 18,
                        "type": "percentage"
                    }
                ]
            },
            {
                "discounts": [
                    {
                        "amount": "10",
                        "type": "percentage"
                    }
                ],
                "name": "Shoes",
                "price": 5000,
                "quantity": 1,
                "taxes": [
                    {
                        "amount": 18,
                        "type": "percentage"
                    }
                ]
            }
        ],
        "shipping_charge": 0
    }
    :return: cart total
    """
    if request.method == "POST":
        payload = request.get_json()
        if 'products' not in payload:
            return Response("invalid request", status=400)
        total = str(calculate_total(payload))
        return total


if __name__ == "__main__":
    app.run()
