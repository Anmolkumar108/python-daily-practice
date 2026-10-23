class ProductNotFoundError(Exception):
    pass
class InsufficientStockError(Exception):
    pass
class EmptyCartError(Exception):
    pass
class PaymentFailedError(Exception):
    pass
class InvalidOrderStatusError(Exception):
    pass