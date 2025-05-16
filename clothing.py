from product import Product
# ---------------------- PRODUCT SUBCLASS Clothing ----------------------

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material

    def __str__(self):
        return (f"[Clothing] Name:{self._name}  ID: {self._product_id} Price: ${self._price} "
                f"Size: {self._size}, Material: {self._material}, "
                f" In Stock: {self._quantity_in_stock}")
def to_dict(self):
        return {
            "type": "Clothing",  # important for identifying type when loading
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "size": self._size,
            "material": self._material
        }

@classmethod
def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["price"],
            data["quantity"],
            data["size"],
            data["material"]
        )
