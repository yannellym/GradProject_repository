from art import logo
from classes import Account, BankUtility, Bank
import random

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
mercado_bank = Bank()
#executes the main functions for the program
def main():
    # print(logo)
    menu_redirect()
    
        
    

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
   
def menu_redirect():
    options()
    user_choice = int(input("Please input choice number: "))
    choices = [1,2,3,4,5,6,7,8,9,10]
    while user_choice:
        if user_choice == 11:
            break
        elif user_choice not in choices:
            print("invalid choice, please try again.")
            options()
        else:
            match user_choice:
                case 1:
                    openAccount()
                    print("Account creation successful!") 
                case 2:
                    getAccountInfoAndBalance()
                case 3:
                    changePin()
                case 4:
                    return .01
                case 5:
                    return .01
                case 6:
                    return .01
                case 7:
                    return .01
                case 8:
                    return .01
                case 9:
                    return .01
                case 10:
                    print(mercado_bank.allbank_accounts)
        menu_redirect()
    
def openAccount():
    user_fname = input("Enter Account owner's first name:\n")
    user_lname = input("Enter Account owner's last name: \n")
    user_ssn = input("Enter Account owner's SSN (9 DIGITS): \n")
    # calls the randomNums function to generate 9 random numbers
    account_num = randomNums(9)
    # if the account number is already in the bank's account list
    # generate another account number
    if account_num in mercado_bank.allbank_accounts:
        account_num = randomNums(9)
    # calls the randomNums function to generate 4 random numbers
    pin = randomNums(4)
    # creates a new account object and passes in the users inputs
    new_account = Account(account_num,user_fname, user_lname, user_ssn, pin)
    # Adds this account number to the bank's account list
    mercado_bank.allbank_accounts.append(new_account)
    print(mercado_bank.allbank_accounts)
    # returns the account information for the user
    return new_account.__repr__()

def getAccountInfoAndBalance():
    account_number = int(input("Please enter your account number: \n"))
    account_pin = int(input("Please enter your account pin: \n"))
    
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                print("Looking for account...")
                print(account.__repr__())
            else:
                print("Invalid PIN number")
        else:
            print("Invalid account number")
    
def changePin():   
    account_number = int(input("Please enter your account number: \n"))
    account_pin = int(input("Please enter your account pin: \n"))
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    # ask the user to input a new pin number and confirm that number again
    # if the confirmed pin equals the new pin given by the user:
    # change the account's pin number to the new pin number
    # else, print that it is an invalid pin number or an invalid account number
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                new_pin = input("Enter new PIN: \n")
                confirmed_pin = input("Enter new PIN again to confirm: \n")
                if new_pin == confirmed_pin:
                    account.pin_num = int(new_pin)
                    print("PIN updated")
                    print(account.pin_num)
                    print(mercado_bank.allbank_accounts)
                else:
                    print("Invalid PIN, Try again")
                    menu_redirect()
            else:
                print("Invalid PIN number")
        else:
            print("Invalid account number")
    
    
def randomNums(num):
    # loops num amount of times
    # each time, it will call the method generaterandominterger from the bank Utility class
    # it will pass in two numbers, 0 and num
    # it will append the number to a res array
    # returns the array as a joined number
    res = []
    for i in range(num):
        res.append(BankUtility.generateRandomInteger(0,num))
    return int("".join(map(str, res)))
# calls the function main   
main()