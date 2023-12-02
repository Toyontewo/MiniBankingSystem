try:
    import string
    import time
    import random
    import itertools
    import threading
    import sys
    from animation import loading_animation

    from tqdm import tqdm

    # LOADING ANIMATION

        # long process here
    # LOADING ANIMATION

    bank_on = True

    while bank_on:

        print("Welcome to Trust Bank Money App")

        user = int(input("1.New User \n2.Existing User \n"))

        if user == 1:
            f_name = str(input("Enter Your First Name: "))
            l_name = str(input("Enter Your Last Name: "))
            email = input("Enter Your Email: ")
            password = input("Enter your Password: ")
            password2 = input("Re-Enter your Password: ")
            if password == password2:
                username = f"{f_name}{l_name}".lower()

                # Getting the first word in the name

                # def get_first_word(name):
                #     words = name.split()
                #     if words:
                #         return words[0]
                #     else:
                #         return None
                #
                # first_name = get_first_word(name)
                # for i in tqdm(range(int(9e6))):
                #     pass

                # Assigning user information to a"1/Bank System/User Information"" txt

                with open(f"../Bank System/User Information/{f_name}_data.txt", "w") as user_data:
                    user_data.write(f"First Name: {f_name} \nLast Name: {l_name} \nUsername: {username} \nPassword: {password} "
                                    f"\nEmail: {email} ")

                # Continuation
                loading_animation()
                print(f"Hi, {f_name}, You account has successfully been created")
                account_number = random.randint(100000000, 999999999)
                print(f"Your account number is {account_number}")
                print()
                deposit_amt = int(input("How much do you want to Deposit into your account?: $"))
                loading_animation()
                # for i in tqdm(range(int(9e6))):
                #     pass

                if deposit_amt <= 100:
                    # loading_animation()
                    print("Amount must be greater than $100")
                    bank_on = False

                else:
                    # loading_animation()
                    print(f"You have successfully deposited ${deposit_amt} into your wallet "
                          f"\n Thank you for using Trust Bank.")
                    bank_on = False
            else:
                print("Password must be the same")
                bank_on = False

        elif user == 2:
            account_balance = random.randint(100000, 10000000)
            usr_name = input("Enter your Username: ")
            usr_password = input("Enter your password: ")
            loading_animation()
            # for i in tqdm(range(int(9e6))):
            #     pass

            print(f"Hi {usr_name}, Your Balance is ${account_balance}")
            print("What can we do for you today?")
            what_to_do = int(input("1. Transfer \n2. Deposit\n"))

            if what_to_do == 1:
                ben_account_type = int(input("1. Trust Bank \n2. Other Bank\n"))
                loading_animation()
                if ben_account_type == 1:
                    ben_account_number = int(input("Enter Beneficiaries account number: "))
                    transfer_amt = int(input("Amount: $"))
                    transfer_pin = int(input("Enter Transfer pin: "))
                    loading_animation()
                    # for i in tqdm(range(int(9e6))):
                    #     pass
                    print(f"You have successfully transferred ${transfer_amt} to your Beneficiary.")
                    print()
                    transfer_balance = account_balance - transfer_amt
                    loading_animation()
                    # for i in tqdm(range(int(9e6))):
                    #     pass
                    print(f"Your Current balance is ${transfer_balance}")
                    bank_on = False

                elif ben_account_type == 2:
                    ben_account_number = int(input("Enter Beneficiaries account number: "))
                    ben_bank_name = input("Enter bank name: ")
                    transfer_amt = int(input("Amount: $"))
                    transfer_pin = int(input("Enter Transfer pin: "))
                    loading_animation()
                    # for i in tqdm(range(int(9e6))):
                    #     pass
                    print(f"You have successfully transferred ${transfer_amt} to your Beneficiary.")
                    print()
                    transfer_balance = account_balance - transfer_amt
                    loading_animation()
                    # for i in tqdm(range(int(9e6))):
                    #     pass
                    print(f"Your Current balance is ${transfer_balance}")
                    bank_on = False
                else:
                    print("Invalid Value")
                    bank_on = False

            elif what_to_do == 2:
                deposit_amt = int(input("How much do you want to deposit?: $"))
                if deposit_amt >= 200:
                    deposit_balance = account_balance + deposit_amt
                    # for i in tqdm(range(int(9e6))):
                    #     pass
                    loading_animation()
                    print(f"You have successfully deposited ${deposit_amt} into your account.")
                    print()
                    print(f"Your current balance is ${deposit_balance}")
                    bank_on = False
                else:
                    # for i in tqdm(range(int(9e6))):
                    #     pass
                    # loading_animation()
                    print("Amount must be greater than $200")
                    bank_on = False
            else:
                print("Invalid Value")
                bank_on = False

        else:
            print("Invalid Value")
            bank_on = False

except ValueError:
    print("Invalid Value")