from typing import List, Optional
from Order import Order
from Coffee import Coffee

class Customer:
    all: List['Customer'] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Customer.all.append(self)

    def __repr__(self):
        return f"Customer('{self.name}')"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Customer name must be a string')
        value = value.strip()
        if len(value) < 1 or len(value) > 15:
            raise ValueError('Customer name must be between 1 and 15 characters')
        self._name = value

    def orders(self) -> List[Order]:
        """Return a list of Order instances for this customer."""
        return [o for o in Order.all if o.customer is self]

    def coffees(self) -> List[Coffee]:
        """Return unique Coffee instances this customer has ordered (preserve order)."""
        seen = []
        for o in self.orders():
            if o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee: Coffee, price: float) -> Order:
        """Create an order for this customer and given coffee at price."""
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Optional['Customer']:
        """
        Return the Customer who has spent the most on the provided coffee.
        Returns None if no orders for that coffee.
        """
        if not isinstance(coffee, Coffee):
            raise TypeError('most_aficionado expects a Coffee instance')

        totals = {}
        for o in [ord for ord in Order.all if ord.coffee is coffee]:
            totals[o.customer] = totals.get(o.customer, 0.0) + o.price

        if not totals:
            return None
        # find customer with max total; if tie, returns first encountered max
        winner = max(totals.items(), key=lambda kv: kv[1])[0]
        return winner