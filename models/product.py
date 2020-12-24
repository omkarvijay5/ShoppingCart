#!/usr/bin/python
# -*- encoding: utf-8 -*-
import random
import string
import uuid


class Option(object):
    """
    Option Object.
    """

    def __init__(self, id, name, code=None, values=[]):
        """
        :param id: Unique Id.
        :param name: Option Name.
        :param code: Option Code.
        :param values: Option Values.
        """
        self.id = id
        self.name = name
        self.code = code
        self.values = values

    def add_value(self, *values):
        self.values.extend(values)


class OptionValue(object):
    """
    OptionValue Object.
    """

    def __init__(self, id, name, code=None, price=0.0):
        """
        :param id: Unique Id.
        :param name: Option Value Name.
        :param code: Option Value Code.
        :param price: Option Value Price.
        """    
        self.id = id
        self.name = name
        self.code = code
        self.price = price


class Product(object):
    """
    Product Object.
    """

    def generate_code(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def __init__(self, name, price, code=None, id=None, options=[]):
        """
        :param id: Unique Id.
        :param name: Product Name.
        :param code: Prodcuct Code.
        :param price: Real Price of Product.
        """
        self.id = id or uuid.uuid1()
        self.code = code or self.generate_code()
        self.price = price
        self.name = name
        self.options = options
