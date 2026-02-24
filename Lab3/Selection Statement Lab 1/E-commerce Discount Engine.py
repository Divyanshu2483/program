# E-commerce Discount Engine

cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discount = 0

# Membership Discount
if membership == "Silver":
    discount = 5
elif membership == "Gold":
    discount = 10
elif membership == "Platinum":
    discount = 15

# Festival Discount
if festival == "yes":
    if discount < 20:
        discount = 20

# Cart value discount
if cart_value > 50000:
    if discount < 25:
        discount = 25

final_amount = cart_value - (cart_value * discount / 100)

print("Highest Discount Applied =", discount, "%")
print("Final Payable Amount =", final_amount)
