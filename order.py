class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer.add_order(self)
        cofee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def name(self, value):
        if not isinstance(value, customer):
            raise ValueError("customer must be an instance of the customer class")
    self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, coffee):
            raise ValueError("coffee must be an instance of the coffee class")
    self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("price must be between 1.0 and 10.0")
    self._price = value