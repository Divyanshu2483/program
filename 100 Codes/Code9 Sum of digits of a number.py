num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits =", sum_digits)

# Input: Enter a number: 2345
# Output: Sum of digits = 14