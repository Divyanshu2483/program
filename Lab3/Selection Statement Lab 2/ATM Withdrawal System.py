# ATM Withdrawal System

balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))
atm_cash = int(input("Enter ATM available cash: "))

if withdraw > balance:
    print("Insufficient Balance")

elif withdraw > 50000:
    print("Daily limit exceeded")

elif withdraw > atm_cash:
    print("ATM does not have enough cash")

else:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
