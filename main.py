import BankAccount


def main():
    while True:
        try:
            name = input("Enter Name: ")
            balance = input("Enter Balance: ")
            bank_class = BankAccount.BankAccount(name, balance)
            break
        except ValueError as e:
            print(e)
            print("Try Again")

    while True:
        try:
            action = int(input("Choose an action:\n1- deposit\n2- withdraw\n3- quit\n"))
            if action == 1:
                deposit_amount = int(input("How much would you like to deposit: "))
                bank_class.deposit(deposit_amount)
                bank_class.displayDetails()
                next_action = input("Would you like to make another transaction? (y/n): ")
                while True:
                    if next_action.lower() == "n":
                        exit()
                    elif next_action.lower() == "y":
                        break
                    else:
                        print("Invalid answer. Returning to home")
                        break
            elif action == 2:
                withdraw_amount = int(input("How much would you like to withdraw: "))
                bank_class.withdraw(withdraw_amount)
                bank_class.displayDetails()
                next_action = input("Would you like to make another transaction? (y/n): ")
                while True:
                    if next_action.lower() == "n":
                        exit()
                    elif next_action.lower() == "y":
                        break
                    else:
                        print("Invalid answer. Returning to home")
                        break
            elif action == 3:
                quit()

            else:
                print("invalid input. Pick again")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
