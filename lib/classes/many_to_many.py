class Coffee:
    def __init__(self, name):
        self._name = name
        self.orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if hasattr(self, "_name") and self._name is not None:
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value

    def _orders(self):
        return self.orders
    
    def customers(self):
        return list(set(order.customer for order in self.orders))
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders) if self.orders else 0

class Customer:
    def __init__(self, name):
        self._name = name
        self.orders = []

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1<= len(value) <= 15):
            raise ValueError("Name must be betwen 1 and 15 characters")
        self._name = value   

    def _orders(self):
        return self.orders
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders))
    
    def create_order(self, coffee, price):
        order = Order(self, coffee)
        coffee.orders.append(order)
        self.orders.append(order)
        order.price = price
        return order
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    
    @property
    def _price(self):
        return self.price
    
    @_price.setter
    def _price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, "_price") and self._price is not None:
            raise AttributeError("Price cannot be changed after instantiation")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of the Customer class")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of the Coffee class")
        self._coffee = value