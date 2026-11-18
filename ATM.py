correct_pin = "1234"
balance = 5000
history = []

pin = input("Enter your ATM PIN: ")

if pin == correct_pin:

    print("WELCOME TO PYTHON ATM")

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("Your Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                history.append(f"Deposited: {amount}")
                print("Deposit Successful!")
            else:
                print("Invalid Amount")

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                history.append(f"Withdrawn: {amount}")
                print("Please collect your cash")
            else:
                print("Invalid Amount or Insufficient Balance")

        elif choice == "4":
            new_pin = input("Enter new PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                correct_pin = new_pin
                print("PIN Changed Successfully!")
            else:
                print("PIN must contain 4 digits")

        elif choice == "5":
            print("Transaction History:")
            for transaction in history:
                print(transaction)

        elif choice == "6":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")
