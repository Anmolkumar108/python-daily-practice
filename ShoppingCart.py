class ShoppingCart:
    def __init__(self, product_names, prices):
        self.product_names = list(product_names)
        self.prices = list(prices)

    def __str__(self):
        return f"Cart has {len(self.product_names)} items."

    def __repr__(self):
        return f"ShoppingCart({self.product_names!r}, {self.prices!r})"

    def __len__(self):
        return len(self.product_names)

    def __getitem__(self, index):
        return {
            "product": self.product_names[index],
            "price": self.prices[index]
        }

    def __setitem__(self, index, value):
        self.product_names[index] = value[0]
        self.prices[index] = value[1]

    def __contains__(self, item):
        return item in self.product_names

    def __iter__(self):
        return iter(zip(self.product_names, self.prices))

    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            new_names = self.product_names + other.product_names
            new_prices = self.prices + other.prices
            return ShoppingCart(new_names, new_prices)
        return NotImplemented


# Do alag alag carts banate hain
cart1 = ShoppingCart(["Apple", "Milk"], [120, 60])
cart2 = ShoppingCart(["Bread"], [45])

# 1. __str__ aur __len__ check karein
print(cart1)         
print(len(cart1))   
# 2. __getitem__ (index se item nikalna)
print(cart1[0])      

# 3. __setitem__ (index change num)
cart1[0] = ("Mango", 150) 
print(cart1[0])

# 4. __contains__ ('in' operator)
print("Milk" in cart1) 

# 4. __iter__ (looping se index Print Karwana)
for Cart in cart1 :
    print(Cart)


# 4. __add__ (Carts ko jodna)
combined_cart = cart1 + cart2
print(combined_cart.product_names) 
print(combined_cart.prices)  
