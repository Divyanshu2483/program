a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)
  #Input
    # Enter first number: 10
    # Enter second number: 15
    # Enter third number: 13
#Output 
    # Largest = 15