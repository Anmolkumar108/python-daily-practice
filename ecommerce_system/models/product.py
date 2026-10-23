class Product:
    def __init__(self, product_id, name, price, stock):

        if not product_id or not str(product_id).strip():
            raise ValueError("Product ID empty nahi honi chahiye.")
        self._product_id = product_id

        if not name or not str(name).strip():
            raise ValueError("Name empty nahi hona chahiye.")
        self._name = name

        self.price = price
        self.stock = stock

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price zero ya negative nahi ho sakti.")
        self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock negative nahi ho sakta.")
        self._stock = value

    def __str__(self):
        return f"Product ID: {self._product_id}\nName: {self._name}\nPrice: ₹{self._price}\nStock: {self._stock}"