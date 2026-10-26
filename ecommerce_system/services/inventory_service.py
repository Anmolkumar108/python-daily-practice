from exceptions import InsufficientStockError

class InventoryService:
    @staticmethod
    def check_stock(product, required_quantity):
        if product.stock < required_quantity:
            raise InsufficientStockError(
                f"Insufficient stock for {product.name}. Available stock: {product.stock}, Required: {required_quantity}"
            )
        return True
    
    @staticmethod
    def reserve_stock(product, required_quantity):
        InventoryService.check_stock(product, required_quantity)
        product.stock -= required_quantity

    @staticmethod
    def release_stock(product, released_quantity):
        product.stock += released_quantity