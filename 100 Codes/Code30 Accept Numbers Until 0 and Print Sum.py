total = 0

while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Sum =", total)

# Enter number (0 to stop): 3
# Enter number (0 to stop): 32
# Enter number (0 to stop): 2
# Enter number (0 to stop): 234
# Enter number (0 to stop): 54
# Enter number (0 to stop): 0
# Sum = 325