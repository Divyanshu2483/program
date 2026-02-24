num = int(input("Enter a number: "))

count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits =", count)

# Enter a number: 12345
# Number of digits = 5