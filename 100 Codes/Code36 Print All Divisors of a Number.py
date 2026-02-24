n = int(input("Enter a number: "))

print("Divisors are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        Enter a number: 3
# Divisors are:
# 1 3