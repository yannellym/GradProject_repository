from art import logo

''' Project 8: Final Project
In this project you will tie together many of the concepts that you have learned throughout the 
course into a unified banking application.  You will develop a program that performs many 
common bank transactions that a bank employee or customer might perform on one or more 
accounts.  
When executed, the program will display a menu with the following choices as follows:
============================================================
What do you want to do?
1. Open an account
2. Get account information and balance
3. Change PIN
4. Deposit money in account
5. Transfer money between accounts
6. Withdraw money from account
7. ATM withdrawal
8. Deposit change
9. Close an account
10. Add monthly interest to all accounts
11. End Program
'''

'''
    File name: project_08.py
    Author: Yannelly Mercado
    Date created: 10/07/2022
    Date last modified: 10/07/2022
    Python Version: 2.7.18
'''

#executes the main functions for the program
def main():
    print(logo)
    ask_choice()
    
   
        
     

# Helper functions for main
def options():
    # Displays the options to the user
    print(
        '''
            What do you want to do?
            1. Open an account
            2. Get account information and balance
            3. Change PIN
            4. Deposit money in account
            5. Transfer money between accounts
            6. Withdraw money from account
            7. ATM withdrawal
            8. Deposit change
            9. Close an account
            10. Add monthly interest to all accounts
            11. End Program
        ''')

def ask_choice():
    choices = [1,2,3,4,5,6,7,8,9,10]
    options()
    user_choice = int(input("Please input choice number: "))
    while user_choice:
        if user_choice == 11:
            break
        elif user_choice not in choices:
            print("invalid choice, please try again.")
            options()
        else:
            print("great choice")
            break
   


# calls the function main   
main()