def get_product(product_number, heading):
    print(heading)
    return {
        "Name": input(f"Enter Product {product_number} Name: "),
        "Price": float(input(f"Enter Product {product_number} Price: ")),
        "Quantity": int(input(f"Enter Product {product_number} Quantity: "))
    }


products = {
    "Product_1": [get_product(1, "___ First Product Detail ___")],
    "Product_2": [get_product(2, "___ Second Product Detail ___")],
    "Product_3": [get_product(3, "___ Third Product Detail ___")]
}


grand_total = 0

print("\n" + "=" * 35)
print("         SHOPPING BILL")
print("=" * 35)

for product_list in products.values():

    for product in product_list:

        total = product["Price"] * product["Quantity"]

        grand_total += total

        print(f"\nProduct  : {product['Name']}")
        print(f"Price    : ₹{product['Price']:.2f}")
        print(f"Quantity : {product['Quantity']}")
        print(f"Total    : ₹{total:.2f}")

print("\n" + "-" * 35)
print(f"Grand Total : ₹{grand_total:.2f}")
print("=" * 35)
