base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result *= base

print("Result =", result)

# Enter base: 2
# Enter power: 4
# Result = 16