print("Geerting user to come ATM !!!")
balance = 1000
user_pin = '1234'
input_pin = input("Enter your pin: ")
atm_one = True
if user_pin != input_pin:
    atm_on = False

while atm_one:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        print("Your balance is " + str(balance))
    elif user_choice == '2':
        money_deposite = input("Enter amount to deposit: ")
        balance += float(money_deposite)
        print("Your balance is " + str(balance))

    elif user_choice == '3':
        money_withdraw = input("Enter amount to withdraw: ")
        if float(money_withdraw) > float(balance):
            print("Insufficient balance.")
        elif float(money_withdraw) <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            balance -= float(money_withdraw)
            print("Your balance is " + str(balance))
    elif user_choice == '4':
        atm_one = False
        print("Thank you for using our ATM. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
