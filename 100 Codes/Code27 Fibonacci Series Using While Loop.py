n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

# Enter number of terms: 2
# 0 1 