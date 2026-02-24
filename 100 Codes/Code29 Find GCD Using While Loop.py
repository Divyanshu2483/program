a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)

# Enter first number: 12
# Enter second number: 2
# GCD = 2