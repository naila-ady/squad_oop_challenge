from product import Product

# ---------------------- PRODUCT SUBCLASS Electronic----------------------
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        return (f"[Electronics] {self._name} (ID: {self._product_id}) - "
                f"Brand: {self.brand}, Warranty: {self.warranty_years} yrs, "
                f"Price: ${self._price}, In Stock: {self._quantity_in_stock}")
def to_dict(self):
        return {
            "type": "Electronics",  # important for identifying type when loading
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity_in_stock,
            "warranty_years": self.warranty_years,
            "brand": self.brand
        }

@classmethod
def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["price"],
            data["quantity"],
            data["warranty_years"],
            data["brand"]
        )
