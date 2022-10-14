from art import logo
from classes import Account, BankUtility, Bank, CoinCollector
import math

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
    Date created: 10/13/2022
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
        if user_choice not in choices:
            print("invalid choice, please try again.")
            options()
        else:
            match user_choice:
                case 1:
                    print(openAccount())
                    print("Account creation successful!") 
                case 2:
                    getAccountInfoAndBalance()
                case 3:
                    changePin()
                case 4:
                    depositMoneyToAccount()
                case 5:
                    transferBetweenAccounts()
                case 6:
                    withdrawFromAccount()
                case 7:
                    withdrawFromATM()
                case 8:
                    depositChange()
                case 9:
                    closeAccount()
                case 10:
                    addMonthlyInterest()
                case 11:
                    break
                case 12:
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
    # print(mercado_bank.allbank_accounts)
    # returns the account information for the user
    return new_account.__repr__()

def getAccountInfoAndBalance():
    account_number, account_pin = askAccountNumAndPin()
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    # return the account's information
    # else, print "invalid account number" or "invalid pin number"
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                print("Looking for account...")
                print(account.__repr__())
            else:
                print("Invalid PIN number")
        else:
            print("Account not found for account number: %d" % account_number)
    
def changePin():   
    account_number, account_pin = askAccountNumAndPin()
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
                    # print(account.pin_num)
                    # print(mercado_bank.allbank_accounts)
                else:
                    print("Invalid PIN, Try again")
                    menu_redirect()
            else:
                print("Invalid PIN number")
        else:
            print("Invalid account number")

def depositMoneyToAccount(): # REFACTOR
    account_number, account_pin = askAccountNumAndPin()
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    # ask the user to input a deposit amount. Save it as a float in a avariable
    # if the deposit amount is < or equal to zero, print a message for user to try again
    # else, call the deposit amount, and deposit the money in the account
    # print the account's information
    # if any account information doesn't match, redirect user to menu again
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                deposit_amount = float(input("Please enter an amount to deposit: \n"))
                if deposit_amount <= 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    account.deposit(deposit_amount)
                    print(f"New balance: ${account.balance}")
        menu_redirect()

def transferBetweenAccounts():
    print("Account to transfer from:")
    account_number, account_pin = askAccountNumAndPin()
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    # ask the user for the transfer account number and PIN number
    # ask the user to input a deposit amount. Save it as a float in a avariable
    # if the deposit amount is < or equal to zero, print a message for user to try again
    # else, call the deposit amount, and deposit the money in the account
    # print the account's information
    # if any account information doesn't match, Print an error message
    # redirect user to menu again if everything else fails
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                print("**Account to transfer to**:")
                t_account_number, t_account_pin = askAccountNumAndPin()
                for t_account in mercado_bank.allbank_accounts:
                    if t_account.account_num == t_account_number:
                        if t_account.pin_num == t_account_pin:
                            deposit_amount = float(input("Please enter an amount to deposit in dollars and cents (Ex, 5.99): \n"))
                            if deposit_amount <= 0:
                                print("Amount cannot be negative. Try again.")
                            else:
                                account.withdraw(deposit_amount)
                                t_account.deposit(deposit_amount)
                                print("** Transfer Complete **")
                                print(f"New balance in account:{account.account_num} is: ${account.balance}")
                                print(f"New balance in account:{t_account.account_num} is: ${t_account.balance}")
                        else:
                            print("Wrong transfer account PIN. Try again.")
                    else:
                        print("Wrong transfer account number. Try again.")
            else:
                print("Wrong account PIN. Try again.")
        else:
            print("Wrong account number. Try again.")
        menu_redirect()

def withdrawFromAccount(): # REFACTOR
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    account_number, account_pin = askAccountNumAndPin()
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                withdraw_amount = float(input("Please enter an amount to withdraw in dollars and cents (Ex, 5.99): \n"))
                if withdraw_amount <= 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    account.withdraw(withdraw_amount)
                    print(f"New balance: ${account.balance}")
    menu_redirect()

def withdrawFromATM():
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    # ask the user to input the amount they want to withdraw in multiples of 5. Save it in a variable
    # if the withdraw amount is less than 5 or greater than 1000 or is not a multiple of 5
    # print, invalid amount try again
    # else, divide the withdraw amount by 20 and round it down. Save this in a variable called twentys
    # create a new amount variable that is the original withdraw amount - the result of twentys variable times 20
    # divide the new_amount variable by 10 and round it down. Save this in a variable called tens
    # update the new_amount variable to equal the new_amount variable - the result of tens variable times 10
    # divide the new_amount variable by 5 and round it down. Save this in a variable called fives
    # print how many 20s, 20s, and 5s the user gave you by using the above variables
    # call the account withdraw method
    # print the new account balance
    account_number, account_pin = askAccountNumAndPin()
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                withdraw_amount = int(input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1,000): \n"))
                if withdraw_amount < 5 or withdraw_amount > 1000 or withdraw_amount %5 != 0:
                    print("Invalid amount. Try again.")
                else:
                    twentys = math.floor(withdraw_amount / 20)
                    new_amount = withdraw_amount - (twentys * 20)
                    tens = math.floor(new_amount / 10)
                    new_amount -= (tens * 10)
                    fives = math.floor(new_amount / 5)
                    print(f"Number of 20-dollar bills: {twentys}")
                    print(f"Number of 10-dollar bills: {tens}")
                    print(f"Number of 5-dollar bills: {fives}")
                    account.withdraw(withdraw_amount)
                    print(f"New balance: ${account.balance}")

def depositChange():
    # set a list with the valid coin letters
    # call the askAccountNumAndPin function to get the user's input
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    # prompt the user to enter a string of the coins they want to deposit. Save it in coins variable
    # set a variable called deposit amount to 0
    # search through each letter in the coins variable
    # if coin is NOT in our valid coins list, print a message with invalid coin and show the coin
    # else, call the parseChange method and add it to the total of the deposit amount variable
    # call the deposit method on the account and deposit the deposit amount
    # if the above fails, print a message with either wrong account num or wrong PIN
    # redirect to menu
    valid_coins = ["P", "N", "D", "Q", "H", "W"]
    account_number, account_pin = askAccountNumAndPin()
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                coins = input("Deposit coins (P: penny, N: nickel, D: dime, Q: Quarter, H: half-dollar, W: whole-dollar) Ex(QPDNNDHW): \n")
                deposit_amt = 0
                for coin in coins:
                    if coin not in valid_coins:
                        print(f"Invalid coin: {coin}")
                    else:
                        deposit_amt += CoinCollector.parseChange(coin)
                account.deposit(deposit_amt)
                print(f"New balance: ${account.balance}")
            else:
                print("Wrong account PIN. Try again.")
        else:
            print("Wrong account number. Try again.")
    menu_redirect()

def closeAccount():
    # set a list with the valid coin letters
    # call the askAccountNumAndPin function to get the user's input
    # search through the bank's list of accounts
    # if the account number equals the account number given by the user
    # if the account's pin number equals the pin number given by the user
    account_number, account_pin = askAccountNumAndPin()
    for account in mercado_bank.allbank_accounts:
        if account.account_num == account_number:
            if account.pin_num == account_pin:
                mercado_bank.allbank_accounts.remove(account)
                print(f'Account {account.account_number} has been closed')
                print(f'Account {account.account_num} has been closed')
            else:
                print("Wrong account PIN. Try again.")
        else:
            print("Wrong account number. Try again.")
    menu_redirect()

def addMonthlyInterest():
    # look through all of the account in the bank's account list
    # calculate the monthly rate by multiplying the account balance times the annual rate
    # then, divide that by twelve
    # then, turn that into an integer (two digits) and divide it by 100 to give you a value
    # save the above value into a variable named monthly rate
    # add this amount to the account's balance
    # display the account balance as a string
    annual_rate = int(input("Enter annual rate percentage (e.g 2.75 for 2.75%): \n"))
    for account in mercado_bank.allbank_accounts:
        monthly_rate = int(((annual_rate  * account.balance) / 12)) / 100
        account.balance += monthly_rate
        print(f"Deposited interest: {monthly_rate} into account number: {account.account_num}, new balance: ${account.balance}")
                        
                
def askAccountNumAndPin():
    # this is a helper function that will ask for the account number and pin
    # it will return both values which will be saved in separate variables
    account_number = int(input("Please enter the account number: \n"))
    account_pin = int(input("Please enter the account pin: \n"))
    return account_number, account_pin
        
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