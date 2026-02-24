num = int(input("Enter number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if lower <= num <= upper:
    print("Number is within range")
else:
    print("Number is outside range")

# Enter number: 2
# Enter lower limit: 0
# Enter upper limit: 1
# Number is outside range