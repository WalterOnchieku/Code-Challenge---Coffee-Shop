class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("customer name must be a string")
        if not 1<= len(value)<=15:
            raise ValueError("must be between 1 and 15 characters")
        self._name = value

    def add_order(self, order):
        self._orders.append(order)#Adds an order to the customer's order list

    def orders(self):
        return self._orders #Returns a list of all orders for this customer

    def coffees(self):
        #returns a list of coffees that the customer has ordered
        return list({order.coffee for order in self._orders}) 

    def create_order(self, coffee, price):
        #creates a new Order for this customer and associates it with a coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of the Coffee class.")
        if not isinstance(price, float):
            raise ValueError("Price must be a float.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        
        # Create a new order
        new_order = Order(customer=self, coffee=coffee, price=price)
        # The order is automatically added to the customer's and coffee's order list
        return new_order