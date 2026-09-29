

def check_balance(i,account_balance):

    print(f"\nYour account balance is {account_balance[i]}. ")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def withdrawal(i,account_balance,account_number):

    withdraw_amount = int(input("Enter the amount you want to withdraw :"))

    if withdraw_amount > account_balance[i] :
        print("\nInsufficent balance!!")

    elif withdraw_amount<0:
        print("\nWithdrawal amount can't be negative.")

    else:
        print("\nWithdrawal Done!")
        account_balance[i] -=  withdraw_amount   
        print(f"\n{withdraw_amount} is debited from Your account \"{account_number[i]}\" and new balance is {account_balance[i]}.") 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
def deposit(i,account_balance,account_number):

    deposit_amount = int(input("Enter Amount to deposit :"))
    if deposit_amount <=0 :
        print("deposit amount must be positive.")
    else:    
        account_balance[i] += deposit_amount
        print(f"\n{deposit_amount} is credited to your bank account {account_number[i]} and balance is {account_balance[i]}.")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def account_details(i,account_number,usernames,account_balance):

    print(f"\nYour Account Number is {account_number[i]}.\nYour username is {usernames[i]}\nYour account balance is {account_balance[i]}.")



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def create_new_acc(account_number,usernames,passwords,account_balance):

    print("\nDetails required to create a new account-- \n1.New account number (10 alphanumeric characters) \n2.New Username  \n3.New password (4 numerical digits)")               
    new_account_number= input("\nEnter a unique account number of your choice: ")

    if new_account_number in account_number:

        print("\nPlease try a unique account number.")
        
    else:
        account_number.append(new_account_number)

       

        new_account_username =input("\nEnter new user name :")
        usernames.append(new_account_username)
        

        new_account_password = input("\nCreate 4 digit Password :")
        passwords.append(new_account_password)

        account_balance.append(0)

        print("\nCongratulations !  Account Sucessfully created. ")
        print(f"\nYour accout details:--\nYour account Number:{new_account_number}\nYour username:--{new_account_username}\nYour password :--{new_account_password}")
                

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def edu_loan(i,account_balance,account_number):

    print("\nYou Chose Education loan.\n\nIn education loan we provide loan of amount 1 lakh to  20 lakhs with an interest of 10% p.a")
    print("\nEnter you want to proceed :\n1.YES\n2.NO")
    print("\nEnter your decicion:")
    edu_loan_choice = int(input())
    if edu_loan_choice == 2:
        print(f"\nThank you for showing interest.")
    elif edu_loan_choice == 1 :
        print("\nHow much amount you want in digits:")    
        edu_loan_amount = int(input())

        if 100000<=edu_loan_amount and edu_loan_amount<=2000000:
            print("\nfor how many years :")
            
            while True:
                edu_loan_year = int(input("Enter year which  should be greater than or equal to 1 :"))
                if edu_loan_year >=1:
                    break
                else:
                    print("invalideyear!year cannot ne negative or zero.")
            total_amount_edu_loan = edu_loan_amount*(1+(10/100))**edu_loan_year
            ci_edu_loan = total_amount_edu_loan - edu_loan_amount
            print("Education Loan Granted!")
            print(f"\nFor your amount {edu_loan_amount}.\n\nYour Total amount is {total_amount_edu_loan} and Interest is {ci_edu_loan} to pay back.")
            account_balance[i]+=edu_loan_amount
            print(f"\n{edu_loan_amount} is credited to your account {account_number[i]} and balance is {account_balance[i]}.")
            print("\nthanks for visit..\n")
        else:
            print(f"\nyour amount {edu_loan_amount} is not in  range! \nWe can't provide you loan.\nThank you for visit.")  
    else:
            print("\nPlease enter only 1 or 2. ")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def home_loan(i,account_balance,account_number):
    print("\nYou Chose Home Loan.\nIn home loan we provide loan of amount 1 lakh to 1 cr with an interest of 12% p.a") 
    print("\nEnter you want to proceed :\n1.YES\n2.NO")
    print("Enter your decicion:")
    home_loan_choice = int(input())
    if home_loan_choice == 2:
        print(f"\nThank you for enquiry.")
    elif home_loan_choice == 1:
        print("\nHow much amount you want in digits:") 
        home_loan_amount = int(input())

        if 100000<=home_loan_amount<=10000000:
            print("\nfor how many years :")
            #
            while True:
                home_loan_year = int(input("Enter year which  should be greater than or equal to 1 :"))
                if home_loan_year >=1:
                    break
                else:
                    print("invalideyear!year cannot ne negative or zero.")
            total_amount_home_loan = home_loan_amount*(1+(12/100))**home_loan_year
            ci_home_loan = total_amount_home_loan - home_loan_amount
            print("Home Loan Granted!")
            print(f"\nfor your amount {home_loan_amount}\n Your Total amount is {total_amount_home_loan} and interest is {ci_home_loan} to pay back")
            account_balance[i]+=home_loan_amount
            print(f"\n{home_loan_amount} is credited to your account {account_number[i]} and balance is {account_balance[i]}.")
            print("\nthanks for visit..\n")
        else:
            print(f"\nyour amount {home_loan_amount} is not in range!\nWe can't provide you loan.\nThank you for visit.")    
    else:
        print("\nPlease enter only 1 or 2. ")      



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def gold_loan(i,account_balance,account_number):
    print("\nYou Chose Gold loan.\nIn Gold loan  we provide loan of amount 10k to 10 lakhs with an interst of 8% p.a")
    print("\nEnter you want to proceed :\n1.YES\n2.NO")
    print("Enter your decision:")
    gold_loan_choice = int(input())
    if gold_loan_choice == 2:
        print("\nThank for enquiry.")
    elif gold_loan_choice == 1:    
        print("\nhow much amount you want in digits:")
        gold_loan_amount = int(input())  
        
        
        if 10000<=gold_loan_amount<=1000000:
            print("\nfor how many years :")
           
            while True:
                gold_loan_year = int(input("Enter year which  should be greater than or equal to 1 :"))
                if gold_loan_year >=1:
                    break
                else:
                    print("invalid year!year cannot ne negative or zero.")
            total_amount_gold_loan =  gold_loan_amount*(1+(8/100))**gold_loan_year
            ci_gold_loan = total_amount_gold_loan - gold_loan_amount
            print("Gold Loan Granted!")
            print(f"\nfor your amount{gold_loan_amount} \nYour Total amount is {total_amount_gold_loan} and interest is {ci_gold_loan} to pay back.")
            account_balance[i]+=gold_loan_amount
            print(f"\n{gold_loan_amount} is credited to your account {account_number[i]} and balance is {account_balance[i]}.")
            print("\nthanks for visit..")
        else:
            print(f"\nyour amount {gold_loan_amount} is not in range!\nWe can't provide you loan.\nThank you for visit.")    

    else:
     print("\nPlease enter only 1 or 2. ")           




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def loan(i,loan_choice,account_balance,account_number):

    if loan_choice == 1 :

        edu_loan(i,account_balance,account_number)
            
    elif loan_choice == 2:
        home_loan(i,account_balance,account_number)


    elif loan_choice == 3:
        gold_loan(i,account_balance,account_number)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



