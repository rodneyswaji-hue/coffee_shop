from typing import List
from Order import Order

class Coffee:
    all: List['Coffee'] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Coffee.all.append(self)

    def __repr__(self):
        return f"Coffee('{self.name}')"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Coffee name must be a string')
        value = value.strip()
        if len(value) < 3:
            raise ValueError('Coffee name must be at least 3 characters long')
        self._name = value

    def orders(self) -> List[Order]:
        """Return a list of Order instances for this coffee."""
        return [o for o in Order.all if o.coffee is self]

    def customers(self) -> List['Customer']:
        """Return unique Customer instances who ordered this coffee."""
        seen = []
        for o in self.orders():
            if o.customer not in seen:
                seen.append(o.customer)
        return seen

    def num_orders(self) -> int:
        """Number of times this coffee has been ordered."""
        return len(self.orders())

    def average_price(self) -> float:
        """Average price of this coffee across its orders. Returns 0.0 if no orders."""
        ords = self.orders()
        if not ords:
            return 0.0
        return sum(o.price for o in ords) / len(ords)