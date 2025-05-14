   
# ---------------------- IMPORTS ----------------------
from abc import ABC, abstractmethod
from datetime import date
import json

# ---------------------- EXCEPTION CLASSES ----------------------
class DuplicateProductIdError(Exception):
    pass

class InvalidProductDataError(Exception):
    pass

# ---------------------- ABSTRACT PRODUCT BASE CLASS ----------------------
class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock to sell.")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

# ---------------------- PRODUCT SUBCLASSES ----------------------
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        return (f"[Electronics] {self._name} (ID: {self._product_id}) - "
                f"Brand: {self.brand}, Warranty: {self.warranty_years} yrs, "
                f"Price: ${self._price}, In Stock: {self._quantity_in_stock}")

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.expiry_date = expiry_date

    def is_expired(self):
        return date.today() > self.expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return (f"[Grocery] {self._name} (ID: {self._product_id}) - "
                f"Expires on: {self.expiry_date}, Status: {status}, "
                f"Price: ${self._price}, In Stock: {self._quantity_in_stock}")

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def __str__(self):
        return (f"[Clothing] {self._name} (ID: {self._product_id}) - "
                f"Size: {self.size}, Material: {self.material}, "
                f"Price: ${self._price}, In Stock: {self._quantity_in_stock}")

# ---------------------- INVENTORY CLASS ----------------------
class Inventory:
    def __init__(self):
        self._products = {}  # Dictionary to store products by ID

    def add_product(self, product):
        if product._product_id in self._products:
            raise DuplicateProductIdError(f"Product ID {product._product_id} already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            self._products.pop(product_id)
        else:
            raise ValueError(f"Product ID {product_id} not found.")

    def search_by_name(self, name):
        result = []
        for product in self._products.values():
            if name.lower() in product._name.lower():
                result.append(product)
        return result

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if isinstance(p, product_type)]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id not in self._products:
            raise KeyError("Product not found.")
        self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id not in self._products:
            raise KeyError("Product not found.")
        self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        total = 0
        for product in self._products.values():
            total += product.get_total_value()
        return total

    def remove_expired_products(self):
        removed_list = []
        for product_id, product in self._products.items():
            if isinstance(product, Grocery) and product.is_expired():
                removed_list.append(product_id)

        for product_id in removed_list:
            del self._products[product_id]
inventory =Inventory()
e1 = Electronics("E101", "Smartphone", 50000, 10, 2, "Samsung")
g1 = Grocery("G101", "Milk", 150, 20, date(2024, 12, 31))
c1 = Clothing("C101", "T-Shirt", 1200, 50, "M", "Cotton")
inventory.add_product(e1)
inventory.add_product(g1)
inventory.add_product(c1)
results = inventory.search_by_name("milk")
for p in results:
    print(p)
