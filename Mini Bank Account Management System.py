"""CREATING A BANK ACCOUNT MANAGEMENT SYSTEM IN WHICH USER CAN USE SERVICES OR CREATE NEW ACCOUNT."""

from bank_module import *

print("VIT BANK")

to_continue = "continue"       #For initialising the while loop condition

account_number = ["26BCE11282","26BCE10776","26BCE11098","26BCE11492"]  
usernames = ["Rohit","Satyam","Aman","Diptanshu"]
passwords = ["0604","0710","1706","0103"]
account_balance = [10000,8000,6000,7000]

while to_continue == "continue" or to_continue == "CONTINUE" or to_continue == "Continue":
    
    print("\n1. Services.\n2. Create New Account.")  # display choices 
    choice_new = int(input("\nEnter Your Choice :")) 

    if choice_new == 1 :

        account_number_input = input("\nEnter your account Number:")
        i = list(account_number).index(account_number_input)
        password_input = input("\nEnter your four digit password :")

        if account_number_input not in account_number or password_input != passwords[i]:  # 

            print("\nAccount Number or Password is Incorrect. ")
            break

        else:

            print("\nAccess Granted")
            print(f"\nWelcome ,{usernames[i]}!!!")

            print(f"\nServices:\n\n1. Account Balance\n2. Withdraw\n3. Deposit\n4. Account Details\n5. Loan Enquiry\n6. Exit")
            choice = int(input("\nEnter your Choice :"))

            if choice == 1 :
                
                check_balance(i,account_balance)
                
            elif choice == 2:

                withdrawal(i,account_balance,account_number) 

            elif choice == 3 :
               

                deposit(i,account_balance,account_number)

            elif choice == 4 :

                account_details(i,account_number,usernames,account_balance)

            elif choice == 5 :

                print(f"\nWelcome,{usernames[i]} to Loan Enquiry.")
                print("\n\nType of loan options available: \n1. Education Loan \n2. Home Loan\n3. Gold Loan \n") 
                loan_choice = int(input("Enter which loan option you are choosing: "))
                loan(i,loan_choice,account_balance,account_number)
                
            elif choice == 6:

                print("\nThank your for using our services. ")    
                break

            to_continue = input("\nEnter CONTINUE if you want to use other services : ")

    elif choice_new == 2:

        create_new_acc(account_number,usernames,passwords,account_balance)
        to_continue = input("\nEnter CONTINUE if you want to use other services : ")
        
    else:

        print("\nPlease enter only 1 or 2. ")


