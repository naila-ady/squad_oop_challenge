# ---------------------- EXCEPTION CLASSES ----------------------
class DuplicateProductIdError(Exception):
    pass

class InvalidProductDataError(Exception):
    pass

class InventoryError(Exception):
    pass

class OutOfStockError(InventoryError):
    pass
