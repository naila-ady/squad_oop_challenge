
from product import Product
from datetime import date

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = expiry_date  # 🔁 Fixed from expiry_date to _expiry_date

    def is_expired(self):
        return date.today() > self._expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return (f"[Grocery] {self._name} (ID: {self._product_id}) - "
                f"Expires on: {self._expiry_date}, Status: {status}, "
                f"Price: ${self._price}, In Stock: {self._quantity_in_stock}")

    def to_dict(self):
        return {
            "type": "Grocery",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_in_stock": self._quantity_in_stock,
            "expiry_date": self._expiry_date.isoformat()  # ✅ for JSON
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["price"],
            data["quantity_in_stock"],
            date.fromisoformat(data["expiry_date"])  # ✅ restore as date
        )
