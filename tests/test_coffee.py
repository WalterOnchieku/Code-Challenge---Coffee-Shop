import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee(name="")  # Name is too short
    with pytest.raises(ValueError):
        Coffee(name="Co")  # Name is too short

    coffee = Coffee(name="Espresso")
    assert coffee.name == "Espresso"

def test_coffee_orders_and_customers():
    coffee = Coffee(name="Latte")
    customer1 = Customer(name="Alice")
    customer2 = Customer(name="Bob")

    order1 = Order(customer=customer1, coffee=coffee, price=3.5)
    order2 = Order(customer=customer2, coffee=coffee, price=4.0)

    assert coffee.orders() == [order1, order2]
    assert set(coffee.customers()) == {customer1, customer2}

def test_num_orders():
    coffee = Coffee(name="Latte")
    customer1 = Customer(name="Alice")

    order1 = Order(customer=customer1, coffee=coffee, price=3.5)
    order2 = Order(customer=customer1, coffee=coffee, price=4.0)

    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee(name="Latte")
    customer1 = Customer(name="Alice")

    assert coffee.average_price() == 0  # No orders yet

    Order(customer=customer1, coffee=coffee, price=3.5)
    Order(customer=customer1, coffee=coffee, price=4.0)

    assert coffee.average_price() == (3.5 + 4.0) / 2
