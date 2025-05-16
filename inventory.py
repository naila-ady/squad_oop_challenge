from datetime import date
from exceptions import DuplicateProductIdError
from grocery import Grocery
from electronics import Electronics
from clothing import Clothing
from datetime import datetime
import json
# ---------------------- INVENTORY CLASS ----------------------
# class Inventory:
#     def __init__(self):
#         self._products = {}  # Dictionary to store products by ID

#     def add_product(self, product):
#         if product._product_id in self._products:
#             raise DuplicateProductIdError(f"Product ID {product._product_id} already exists.")
#         self._products[product._product_id] = product

#     def remove_product(self, product_id):
#         if product_id in self._products:
#             self._products.pop(product_id)
#         else:
#             raise ValueError(f"Product ID {product_id} not found.")

#     def search_by_name(self, name):
#         result = []  #Yahan define ki gayi hai result — ek khaali list banayi gayi hai
#         for product in self._products.values():
#             if name.lower() in product._name.lower():
#                 result.append(product)  #Matching product ko list mein daal diya
#         return result  # Yeh list return ho rahi hai


#     def search_by_type(self, product_type):
#         return [p for p in self._products.values() if isinstance(p, product_type)]

#     def list_all_products(self):
#         return list(self._products.values())

#     def sell_product(self, product_id, quantity):
#         if product_id not in self._products:
#             raise KeyError("Product not found.")
#         self._products[product_id].sell(quantity)

#     def restock_product(self, product_id, quantity):
#         if product_id not in self._products:
#             raise KeyError("Product not found.")
#         self._products[product_id].restock(quantity)

#     def total_inventory_value(self):
#         total = 0
#         for product in self._products.values():
#             total += product.get_total_value()
#         return total
    
#     def total_inventory_value1(self):
#         total1 = 0
#         for product in self._products.values():
#             total1 += product.get_total_value1()
#         return total1


#     def remove_expired_products(self):
#         removed_list = []
#         for product_id, product in self._products.items():
#             if isinstance(product, Grocery) and product.is_expired():
#                 removed_list.append(product_id)

#         for product_id in removed_list:
#             del self._products[product_id]
#     def save_to_file(self, filename):
#         data = []
#         for product in self._products.values():
#             if isinstance(product, Grocery):
#                 product_data = {
#                     "type": "Grocery",
#                     "product_id": product._product_id,
#                     "name": product._name,
#                     "price": product._price,
#                     "quantity": product._quantity_in_stock,
#                     "expiry_date": product._expiry_date.isoformat()
#                 }
#             elif isinstance(product, Electronics):
#                 product_data = {
#                     "type": "Electronics",
#                     "product_id": product._product_id,
#                     "name": product._name,
#                     "price": product._price,
#                     "quantity": product._quantity_in_stock,
#                     "warranty": product._warranty,
#                     "brand": product._brand
#                 }
#             elif isinstance(product, Clothing):
#                 product_data = {
#                     "type": "Clothing",
#                     "product_id": product._product_id,
#                     "name": product._name,
#                     "price": product._price,
#                     "quantity": product._quantity_in_stock,
#                     "size": product._size,
#                     "material": product._material
#                 }
#             else:
#                 continue
#             data.append(product_data)

#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)

#     def load_from_file(self, filename):
#         with open(filename, 'r') as f:
#             data = json.load(f)

#         self._products.clear()
#         for item in data:
#             prod_type = item["type"]
#             if prod_type == "Grocery":
#                 expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
#                 product = Grocery(item["product_id"], item["name"], item["price"], item["quantity"], expiry)
#             elif prod_type == "Electronics":
#                 product = Electronics(item["product_id"], item["name"], item["price"], item["quantity"],
#                                       item["warranty"], item["brand"])
#             elif prod_type == "Clothing":
#                 product = Clothing(item["product_id"], item["name"], item["price"], item["quantity"],
#                                    item["size"], item["material"])
#             else:
#                 continue

#             self._products[product._product_id] = product

from datetime import datetime
import json
from exceptions import DuplicateProductIdError
from grocery import Grocery
from electronics import Electronics
from clothing import Clothing

class Inventory:
    def __init__(self):
        self._products = {}  # Store products by ID

    def add_product(self, product):
        if product._product_id in self._products:
            raise DuplicateProductIdError(f"Product ID {product._product_id} already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]
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
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = []
        for product_id, product in self._products.items():
            if isinstance(product, Grocery) and product.is_expired():
                to_remove.append(product_id)
        for pid in to_remove:
            del self._products[pid]

    def save_to_file(self, filename):
        data = []
        for product in self._products.values():
            if isinstance(product, Grocery):
                product_data = {
                    "type": "Grocery",
                    "product_id": product._product_id,
                    "name": product._name,
                    "price": product._price,
                    "quantity": product._quantity_in_stock,
                    "expiry_date": product._expiry_date.isoformat()
                }
            elif isinstance(product, Electronics):
                product_data = {
                    "type": "Electronics",
                    "product_id": product._product_id,
                    "name": product._name,
                    "price": product._price,
                    "quantity": product._quantity_in_stock,
                    "warranty": product._warranty,
                    "brand": product._brand
                }
            elif isinstance(product, Clothing):
                product_data = {
                    "type": "Clothing",
                    "product_id": product._product_id,
                    "name": product._name,
                    "price": product._price,
                    "quantity": product._quantity_in_stock,
                    "size": product._size,
                    "material": product._material
                }
            else:
                continue
            data.append(product_data)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)

        self._products.clear()
        for item in data:
            prod_type = item["type"]
            if prod_type == "Grocery":
                expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
                product = Grocery(item["product_id"], item["name"], item["price"], item["quantity"], expiry)
            elif prod_type == "Electronics":
                product = Electronics(item["product_id"], item["name"], item["price"], item["quantity"],
                                      item["warranty"], item["brand"])
            elif prod_type == "Clothing":
                product = Clothing(item["product_id"], item["name"], item["price"], item["quantity"],
                                   item["size"], item["material"])
            else:
                continue
            self._products[product._product_id] = product
