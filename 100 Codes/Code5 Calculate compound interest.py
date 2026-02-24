p = float(input("Enter Principal: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time in Month: "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)
#Input
    # Enter Principle : 2000
    # Enter Rate of interest: 3
    # Enter Time in Month: 2
# Output
    # Compound Interest = 121.79999999999973