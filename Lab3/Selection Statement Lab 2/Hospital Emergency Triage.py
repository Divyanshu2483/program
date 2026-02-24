# Hospital Emergency Triage

age = int(input("Enter age: "))
heart_rate = int(input("Enter heart rate: "))
injury = input("Severe injury? (yes/no): ")

if heart_rate < 60 or heart_rate > 100 or injury == "yes":
    print("Priority: Critical")

elif age > 65:
    print("Priority: Moderate (Upgraded for senior)")

else:
    print("Priority: Normal")
