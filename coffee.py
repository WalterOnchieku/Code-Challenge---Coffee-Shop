class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []#holds all orders for this coffee

        @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1<= len(value)<=15:
            raise ValueError("must be at least 3 characters")
        self._name = value

    def add_order(self, order):
        self._orders.append(order)#appends order to coffee's order list

    def orders(self):
        return self._orders #returns list of all ordert for the coffeee

    def customers(self):
        #Returns a unique list of customers who have ordered this coffee
        return list({order.customer for order in self._orders})

    def num_orders(self):
        #Returns the total number of orders for this coffee
        return len(self._orders)

    def average_price(self):
        #Returns the average price of all orders for this coffee
        if not self._orders:
            return 0  # If no orders, return 0 as the average price
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)