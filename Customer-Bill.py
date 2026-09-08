original_price = float(input("Enter original price: ₹"))
discount_percent = float(input("Enter discount percentage: "))
gst_percent = float(input("Enter GST percentage: "))


discount_amount = original_price * discount_percent / 100

price_after_discount = original_price - discount_amount

gst_amount = price_after_discount * gst_percent / 100

final_amount = price_after_discount + gst_amount

print("\n----- Bill Summary -----")
print(f"Original Price = ₹{original_price:.2f}")
print(f"Discount Amount = ₹{discount_amount:.2f}")
print(f"Price After Discount = ₹{price_after_discount:.2f}")
print(f"GST Amount = ₹{gst_amount:.2f}")
print(f"Final Payable Amount = ₹{final_amount:.2f}")