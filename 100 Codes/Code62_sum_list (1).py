# Problem 62: Find sum of list elements
numbers = list(map(int, input("Enter list elements: ").split()))
total = 0
for num in numbers:
    total += num
print("Sum of list elements:", total)