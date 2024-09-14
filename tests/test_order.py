import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Latte")

    order = Order(customer=customer, coffee=coffee, price=4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_order_customer_validation():
    coffee = Coffee(name="Latte")
    with pytest.raises(ValueError):
        Order(customer=None, coffee=coffee, price=4.5)  # Invalid customer

def test_order_coffee_validation():
    customer = Customer(name="Alice")
    with pytest.raises(ValueError):
        Order(customer=customer, coffee=None, price=4.5)  # Invalid coffee

def test_order_price_validation():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Latte")

    with pytest.raises(ValueError):
        Order(customer=customer, coffee=coffee, price=0.5)  # Price too low

    with pytest.raises(ValueError):
        Order(customer=customer, coffee=coffee, price=11.0)  # Price too high

    order = Order(customer=customer, coffee=coffee, price=5.0)
    assert order.price == 5.0
