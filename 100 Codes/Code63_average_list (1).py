# Problem 63: Find average of list elements
numbers = list(map(int, input("Enter list elements: ").split()))
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average of list elements:", average)