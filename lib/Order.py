from typing import List
from Customer import Customer
from Coffee import Coffee

class Order:
    all: List['Order'] = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        # validation delegated to property setters
        self._customer = None
        self._coffee = None
        self._price = None

        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)

    def __repr__(self):
        return f"Order(customer={self.customer!r}, coffee={self.coffee!r}, price={self.price})"

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, value: Customer):
        if not isinstance(value, Customer):
            raise TypeError('Order.customer must be a Customer instance')
        self._customer = value

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @coffee.setter
    def coffee(self, value: Coffee):
        if not isinstance(value, Coffee):
            raise TypeError('Order.coffee must be a Coffee instance')
        self._coffee = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError('Order.price must be a number')
        val = float(value)
        if not (1.0 <= val <= 10.0):
            raise ValueError('Order.price must be between 1.0 and 10.0')
        self._price = val