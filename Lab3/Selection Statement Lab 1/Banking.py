# Banking – Suspicious Transaction Detection

amount = float(input("Enter transaction amount: "))
account_opened = int(input("Enter account opened in months: "))
international = input("Is transaction international? (yes/no): ")

if amount > 200000 and account_opened < 6 and international == "yes":
    print("Transaction Flagged for Manual Verification")
else:
    print("Transaction is Normal")
