a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print("Greatest number =", greatest)

# Enter first number: 24
# Enter second number: 10
# Enter third number: 35
# Enter fourth number: 23
# Greatest number = 35