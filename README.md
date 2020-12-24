Setup:

command line tool:
python commands/shopping_cart.py

virtualenvwrapper setup:
mkvirtualenv shopping_cart_env
pip install -r requirements.txt

The app is built using pure python object oriented fashion.
It does not connect to any database.

models:
contains all necessary models for the cart

commands:
contains all the command line setup

services:
core logic for calculating total cost resides here


tests:
python tests/cart.py

REST api is built using python flask.
python app.py

url: http://127.0.0.1:5000/
type: post
example payload:
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

