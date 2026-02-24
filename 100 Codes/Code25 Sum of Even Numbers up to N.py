n = int(input("Enter a number: "))

i = 1
sum_even = 0

while i <= n:
    if i % 2 == 0:
        sum_even += i
    i += 1

print("Sum of even numbers =", sum_even)

# Enter a number: 23
# Sum of even numbers = 132