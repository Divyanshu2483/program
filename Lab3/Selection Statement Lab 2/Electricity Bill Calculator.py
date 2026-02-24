# Electricity Bill Calculator

units = int(input("Enter electricity units: "))
senior = input("Are you a senior citizen? (yes/no): ")

# Bill calculation
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

# Discount
if senior == "yes":
    discount = bill * 0.10
    bill = bill - discount

print("Total Bill =", bill)
