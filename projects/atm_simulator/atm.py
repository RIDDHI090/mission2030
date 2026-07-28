print("===== ATM Simulator =====")

pin = int(input("Enter PIN: "))

if pin == 1234:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    balance = 10000

    if choice == 1:
        print("Your Balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("New Balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))

        if amount <= balance:
            balance = balance - amount
            print("New Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank you for using our ATM")
       

else:
    print("Invalid PIN")


