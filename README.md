WK 3 CODE CHALLENGE - COFFEE SHOP

In this code challenge, I create a Python application from scratch to model a Coffee Shop domain using object-oriented programming principles to test my ability to design classes, implement methods, establish relationships between objects, and handle data appropriately.


The model consists of three main entities: `Customer`, `Coffee`, and `Order`. The relationships are as follows:

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

There are three Python files in the coffee shop directory with a class defined corresponding to the file name :
     - `customer.py`
     - `coffee.py`
     - `order.py`

Comments have been added to describe the following:
- Initializers and Properties
- Object Relationship Methods and Properties 
- Aggregate and Association Methods
- Handling Exceptions and Validating Inputs


TESTING

 -  A `tests` directory is included in the coffee_shop directory with test files (`test_customer.py`, `test_coffee.py`, `test_order.py`) to test each class and method.
 
