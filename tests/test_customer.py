import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer(name="")  # Name is too short
    with pytest.raises(ValueError):
        Customer(name="a" * 16)  # Name is too long

    customer = Customer(name="Alice")
    assert customer.name == "Alice"

def test_create_order():
    customer = Customer(name="Alice")
    coffee = Coffee(name="Espresso")
    order = customer.create_order(coffee=coffee, price=5.0)

    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_customer_orders_and_coffees():
    customer = Customer(name="Alice")
    coffee1 = Coffee(name="Latte")
    coffee2 = Coffee(name="Mocha")

    order1 = customer.create_order(coffee=coffee1, price=3.5)
    order2 = customer.create_order(coffee=coffee2, price=4.0)
    order3 = customer.create_order(coffee=coffee1, price=3.8)

    assert customer.orders() == [order1, order2, order3]
    assert set(customer.coffees()) == {coffee1, coffee2}  # Ensure unique coffees
