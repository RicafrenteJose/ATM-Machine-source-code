#Ricafrente Jose Urbanito III, S.

# sample account details
account_number = "1234"
pin = "0000"
balance = 1000.00

# Step 1: Ask for account number and PIN
user_account = input("Enter your account number: ")
user_pin = input("Enter your PIN: ")

# Step 2: Check if account and PIN are correct
if user_account == account_number and user_pin == pin:
    print("Login successful!\n")

    # Step 3: Display options and ask for user's choice
    while True:
        print("Choose an option:")
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Cancel Transaction")
        
        choices = input("Enter option (1/2/3): ")

        # Step 4: Balance Inquiry
        if choices == "1":
            print(f"Your current balance is: ${balance:.2f}")

        # Step 5: Withdraw Cash
        elif choices == "2":
            amount_input = input("Enter amount to withdraw: ")

            # Check if the entered amount is a valid number
            if amount_input.isdigit():
                amount = float(amount_input)

                if amount <= balance:
                    # Proceed with withdrawal
                    balance = balance - amount
                    print("Processing...")
                    print("\n=== Receipt ===")
                    print(f"Withdrawn Amount: ${amount:.2f}")
                    print(f"New Balance: ${balance:.2f}")
                    continue # we need to add a "continue" to skip the current iteration
                else:
                    print("Insufficient balance. Please try again or cancel the transaction.")
                    # Ask again for withdrawal amount

            else:
                print("Invalid amount. Please enter a valid number.")

        # Step 6: Cancel Transaction
        elif choices == "3":
            print("Transaction canceled. Thank you for using the ATM.")
            break  # Exit the program

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

        # Step 7: Ask if user wants another transaction
        another = input("Do you want another transaction? (yes/no): ")
        if another.lower() != "yes":# i put lower() to become error free becuase it has case sensitive
            print("Thankyou for using this ATM machine!")
            break  # Exit the program

else:
    print("Incorrect account number or PIN.")
