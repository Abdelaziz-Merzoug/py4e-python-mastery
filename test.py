balance = 5000.0
pin = "1234"

attemps = 0

while attemps < 3:
    user_pin = input("Enter your pin: ")
    if user_pin == pin:
        print("Access granted")
        break
    else:
        print("Access denied")
        attemps += 1

if attemps == 3:
    print("Too many attempts. Access denied.")
    exit()

while True:
    print("1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is: ", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            continue
        else:
            balance += amount
            print("Your new balance is: ", balance)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            continue
        elif amount > balance:
            print("Insufficient funds. Your balance is: ", balance)
            continue
        else:
            balance -= amount
            print("Your new balance is: ", balance)
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


