import random, math
from art import logo

class Bank:
      def __init__ (self):
            # stores all the accounts in the bank
            # has a set number of accounts that it can support
            self.allbank_accounts = []
            self.numaccounts_supported = 100
            
            
      def addAccountToBank(self, account): # 2 unit tests need to be implemented
            # parameter received of type: OBJECT
            # adds the account to the allbank_accounts list only if:
            # the list length is less than the number of accounts supported
            # returns True if the account is added to the allbank_accounts list
            # print a message if the account is not added and returns False
            if len(self.mercado_bank.allbank_accounts) < self.mercado_bank.numaccounts_supported:
                  self.mercado_bank.allbank_accounts.append(account)
                  return True
            else:
                  return False

      def removeAccountFromBank(self, account): # 2 unit tests need to be implemented
            # parameter received of type: OBJECT
            # looks trough the list of account in the bank list
            # if there is an account in the list that matches the account given
            # deletes such account from the bank list
            for stored_account in self.allbank_accounts:
                  if stored_account == account:
                        self.allbank_accounts.remove(account)
      
      def findAccount(self, account_number): # 2 unit tests need to be implemented
            # parameter received of type: INT
            # looks trough the list of account in the bank list
            # if there is an account in the list that matches the account number given
            # returns the account object from the list
            # if no account matches the account number, returns "no accoutn found"
            for stored_account in self.allbank_accounts:
                  if stored_account.account_num == account_number:
                        return stored_account
                  return "Account not found"
      
      def addMonthlyInterest(self): # 2 unit tests need to be implemented
            # look through all of the account in the bank's account list
            # calculate the monthly rate by multiplying the account balance times the annual rate
            # then, divide that by twelve
            # then, turn that into an integer (two digits) and divide it by 100 to give you a value
            # save the above value into a variable named monthly rate
            # add this amount to the account's balance
            # display the account balance as a string
            annual_rate = float(input("Enter annual rate percentage (e.g 2.75 for 2.75%): \n"))
            for account in self.mercado_bank.allbank_accounts:
                  monthly_rate = int(((annual_rate  * account.getOwnerBalance) / 12)) / 100
                  account.setOwnerBalance = account.getOwnerBalance + monthly_rate
                  print(f"Deposited interest: {monthly_rate} into account number: {account.account_num}, new balance: ${round(account.getOwnerBalance, 2)}")

class Account:
      def __init__ (self, account_number, owner_fname, owner_lname, ssn, pin):
            self.account_num = account_number
            self.owner_firstname = owner_fname
            self.owner_lastname = owner_lname
            self._social = ssn
            self.pin_num = pin
            self.balance = 0.00
     
      # getters and setters for the Account object    
      @property
      def getOwnerFirstName(self):
            return self.owner_firstname
      
      @getOwnerFirstName.setter
      def setOwnerFirstName(self, name):
            self.owner_firstname = name
      
      @property
      def getOwnerLastName(self):
            return self.owner_lastname
      
      @getOwnerLastName.setter
      def setOwnerLastName(self, name):
            self.owner_lastname = name
      
      @property
      def getOwnerSocial(self):
            return self._social
      
      @getOwnerSocial.setter
      def setOwnerSocial(self, digits):
            self._social = digits
      
      @property
      def getOwnerPin(self):
            return self.pin_num
      
      @getOwnerPin.setter
      def setOwnerPin(self, new_pin):
            self.pin_num = new_pin
      
      @property
      def getOwnerBalance(self):
            return self.balance
      
      @getOwnerBalance.setter
      def setOwnerBalance(self, balance):
            self.balance = balance
      
    
      def deposit(self, amount): # 2 unit tests need to be implemented
            # adds the amount to the account balance and returns
            # the new account balance
            if amount < 1 or isinstance(amount, str):
                  print("Invalid amount.Try again")
                  return False
            else:
                  self.setOwnerBalance += amount
                  return self.getOwnerBalance
      
      def withdraw(self, amount): # 2 unit tests need to be implemented
            # subtracts the amount from the account balance and returns
            # the new account balance
            # if not enough funds available, returns a string 
            if self.getOwnerBalance > 0:
                  new_balance = self.getOwnerBalance - amount
                  self.setOwnerBalance = new_balance
                  return self.getOwnerBalance
            return "not enough funds available"
      
      def isValidPIN(self, pin): # 2 unit tests need to be implemented
            # if the pin entered matches the pin of the account
            # return true, false otherwise
            if self.getOwnerPin == pin:
                  return True
            return False
      
      def __repr__(self):
            # returns a string of all of the information of the account class
            return f'''
                  Account_number : {self.account_num}
                  Owner First Name : {self.getOwnerFirstName}
                  Owner Last name : {self.getOwnerLastName}
                  Owner SSN : XXX-XXX-{self.getOwnerSocial[-4:]}
                  pin = {self.getOwnerPin}
                  balance = ${self.getOwnerBalance}
                  '''
                  
class CoinCollector:
      # constructor so you cannot instantiate this class
      def __init__(self):
            pass
      
      def parseChange(self, coins): # needs 3 unit tests
            # saves the coins parameter into a variable called coin_list that includes all letters in the string
            # Ex, ["P", "D", "H", "Q"]
            # sets the deposit amount to zero
            # looks through each coin in the coin list and matches it with the value. Adds this value to the deposit amount
            # if coin is not a match to any value, print the message invalid coin and show the coin
            # returns the deposit amount
            coin_list = [*coins.upper()]
            print(coin_list)
            deposit_amt = 0
            for coin in coin_list:
                  match coin:
                        case "P":
                              deposit_amt +=  .01
                        case "N":
                              deposit_amt +=  .05
                        case "D":
                              deposit_amt +=  .10
                        case "Q":
                              deposit_amt +=  .25
                        case "H":
                              deposit_amt +=  .50
                        case "W":
                              deposit_amt +=  1
                        case default:
                              print(f"Invalid coin: {coin}")
            return deposit_amt
class BankUtility:
      def __init__ (self):
            pass
      def promptUserForString(self, name):
            # parameter received of type: STRING
            # string prompt will print on the screen and ask the user to input information
            # method will return the user's response as a string
            user_response =input(f"Enter Account owner's {name}:\n")
            return user_response
      
      def promptUserForPositiveNumber(self, prompt):
            # parameter received of type: STRING
            # prompts use to enter a positive number
            # if the number is less than or equal to zero
            # will print a message and loop again
            # if number is positive, will return the number
            user_response = eval(input(prompt))
            if not isinstance(user_response, int):
                  print("Deposit amount must be a positive number")
                  return False
            elif user_response <= 0:
                  print("Amount cannot be negative. Try again")    
                  return False 
            else:
                  return user_response
                  
      def generateRandomInteger(self, min, max): # needs 2 unit tests
            # parameters received of type: INT
            # takes in the min and max value and generates a random integer between these two numbers (both inclusive)
            # returns the random integer 
            ran_num = random.randint(min, max + 1)
            return ran_num
      
      def convertFromDollarsToCents(self, amount):        # needs 2 unit tests
            # parameter received of type: FLOAT  
            # takes in a float and converts it to string
            # will remove the dots in the string
            # return the string as a number 
            new_amount = str(amount).replace(".", "")
            return int(new_amount)
      
      def isNumeric(self, numberToCheck): # needs 2 unit tests
            # if the numberToCheck is a number, returns True
            # else, returns False
            try:
                  if numberToCheck.isdigit():
                        return True
                  else:
                        return False
            except ValueError:
                  return False
            
      # Helper functions for main
      def options(self):
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
      
      def menu_redirect(self):
            # displays the options of the menu
            self.options()
            user_choice = input("Please input choice number: ")
            # valid user choices
            choices = [1,2,3,4,5,6,7,8,9,10,11]
            
            # if the user choice is a number
            # and the user choice is in the valid user choices
            # print the user's choice from the menu
            # else, if the user choice is not in the valid user choices, redirect them to the menu again
            # if the user choice is not a number, redirect them to the menu again
            if self.isNumeric(user_choice):
                  user_choice = int(user_choice)
                  if user_choice not in choices:
                        print("invalid choice, please try again.")
                        self.menu_redirect()  
                  else:
                        if user_choice == 11:
                              print("*** Thank you for using MercadoBank. Have a nice day! ***")
                        else:
                              match user_choice:
                                    case 1:
                                          print(self.openAccount()) 
                                    case 2:
                                          print(self.getAccountInfoAndBalance())
                                    case 3:
                                          self.changePin()
                                    case 4:
                                          self.depositMoneyToAccount()
                                    case 5:
                                          self.transferBetweenAccounts()
                                    case 6:
                                          self.withdrawFromAccount()
                                    case 7:
                                          self.withdrawFromATM()
                                    case 8:
                                          self.depositChange()
                                    case 9:
                                          self.closeAccount()
                                    case 10:
                                          self.addMonthlyInterest()
                              self.menu_redirect()
            else:
                  print("Please enter a numeric character. Try again. ")
                  self.menu_redirect()
      
      def openAccount(self):
            print("OPEN ACCOUNT")
            # call promptUserForString to ask the user for string inputs
            user_fname = self.promptUserForString("first name")
            user_lname = self.promptUserForString("last name")
            user_ssn = self.promptUserForString("SSN (9 Digits)")
            
            # if the user didnt input a name or a last name or an SSN,
            # redirect them to the menu again.
            if user_fname == "" or user_lname == "" or user_ssn == "":
                  print("Invalid input. Try again.")
                  self.menu_redirect()
            
            # if the length of the user SSN is less than 9 or greater than 9 or
            # the user SSN is not numeric, then print a message and redirect user to menu again. 
            print(self.isNumeric(user_ssn))   
             
            if len(user_ssn) != 9 or not self.isNumeric(user_ssn):
                  print("Social Security number must be 9 digits and numeric. Try again.")
                  self.menu_redirect()

            # calls the randomNums function to generate 9 random numbers
            account_num = self.randomNums(9)
            
            # if the account number is already in the bank's account list
            # generate another account number
            if account_num in self.mercado_bank.allbank_accounts:
                  account_num = self.randomNums(9)
            
            # if the length of the account number is not 9, generate a new account number
            if len(str(account_num)) != 9:
                  account_num = self.randomNums(9)
            
            # calls the randomNums function to generate 4 random numbers
            pin = self.randomNums(4)
            
            # If the length of the pin is not 4 digits long, generate a new pin
            if len(str(pin)) != 4:
                  pin = self.randomNums(4)
            # creates a new account object and passes in the users inputs
            new_account = Account(account_num, user_fname, user_lname, user_ssn, pin)
            # Adds this account number to the bank's account list
 
            # returns the account information for the user
            # if the bank's account list is full, return "no more accounts available" 
            if self.addAccountToBank(new_account):
                  print("Account creation successful!")
                  return new_account.__repr__()
            else:
                  print("No more accounts available")

      def getAccountInfoAndBalance(self):
            account_number, account_pin = self.askAccountNumAndPin()
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            # return the account's information
            # else, print "invalid account number" or "invalid pin number"
            user_account = self.userIsConfirmed(account_number, account_pin)
            if user_account:
                  print("Looking for account...")
                  return user_account.__repr__()
      
      def changePin(self):   
            account_number, account_pin = self.askAccountNumAndPin()
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            # ask the user to input a new pin number and confirm that number again
            # if the confirmed pin equals the new pin given by the user:
            # change the account's pin number to the new pin number
            # else, print that it is an invalid pin number or an invalid account number
            user_account = self.userIsConfirmed(account_number, account_pin)
            
            if not self.verifySecondPin(user_account):       
                  self.verifySecondPin(user_account)

            
      def depositMoneyToAccount(self): 
            account_number, account_pin = self.askAccountNumAndPin()
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            # ask the user to input a deposit amount. Save it as a float in a avariable
            # if the deposit amount is < or equal to zero, print a message for user to try again
            # else, call the deposit amount, and deposit the money in the account
            # print the account's information
            # if any account information doesn't match, redirect user to menu again
            user_account = self.userIsConfirmed(account_number, account_pin)
      
            if self.verifyPositiveAmount(user_account, account_number):
                  return
                  
      def transferBetweenAccounts(self):
            print("Account to transfer from:")
            account_number, account_pin = self.askAccountNumAndPin()
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
            user_account = self.userIsConfirmed(account_number, account_pin)
            if user_account:
                  print("**Account to transfer to**:")
                  t_account_number, t_account_pin = self.askAccountNumAndPin()
                  transferingto_account = self.userIsConfirmed(t_account_number, t_account_pin)
                  if transferingto_account:
                        deposit_amount = float(input("Please enter an amount to deposit in dollars and cents (Ex, 5.99): \n"))
                        if user_account.getOwnerBalance <= 0:
                              print("Amount cannot be negative. Try again.")
                        elif user_account.getOwnerBalance < deposit_amount:
                              print(f"Insufficient funds in account {user_account.account_num}")
                        else:
                              user_account.withdraw(deposit_amount)
                              transferingto_account.deposit(deposit_amount)
                              print("** Transfer Complete **")
                              print(f"New balance in account:{user_account.account_num} is: ${user_account.getOwnerBalance}")
                              print(f"New balance in account:{transferingto_account.account_num} is: ${transferingto_account.getOwnerBalance}")
                              
      def withdrawFromAccount(self): # REFACTOR
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            account_number, account_pin = self.askAccountNumAndPin()
            user_account = self.userIsConfirmed(account_number, account_pin)
            if user_account:
                  withdraw_amount = float(input("Please enter an amount to withdraw in dollars and cents (Ex, 5.99): \n"))
                  if withdraw_amount <= 0:
                        print("Amount cannot be negative. Try again.")
                  elif user_account.getOwnerBalance < withdraw_amount:
                        print(f"Insufficient funds in account {user_account.account_num}")
                  else:
                        user_account.withdraw(withdraw_amount)
                        print(f"New balance: ${user_account.getOwnerBalance}")

      def withdrawFromATM(self):
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
            account_number, account_pin = self.askAccountNumAndPin()
            user_account = self.userIsConfirmed(account_number, account_pin)
            if user_account:
                  self.withdraw_amount = int(input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1,000): \n"))
                  if self.withdraw_amount < 5 or self.withdraw_amount > 1000 or self.withdraw_amount % 5 != 0:
                        print("Invalid amount. Try again.")
                  elif user_account.getOwnerBalance < self.withdraw_amount:
                        print("Not enough funds. Try again.")
                  else:
                        twentys = math.floor(self.withdraw_amount / 20)
                        new_amount = self.withdraw_amount - (twentys * 20)
                        tens = math.floor(new_amount / 10)
                        new_amount -= (tens * 10)
                        fives = math.floor(new_amount / 5)
                        print(f"Number of 20-dollar bills: {twentys}")
                        print(f"Number of 10-dollar bills: {tens}")
                        print(f"Number of 5-dollar bills: {fives}")
                        user_account.withdraw(self.withdraw_amount)
                        print(f"New balance: ${user_account.getOwnerBalance}")

      def depositChange(self):
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
            account_number, account_pin = self.askAccountNumAndPin()
            user_account = self.userIsConfirmed(account_number, account_pin)
            if user_account:
                  coins = input("Deposit coins (P: penny, N: nickel, D: dime, Q: Quarter, H: half-dollar, W: whole-dollar) Ex(QPDNNDHW): \n")
                        
                  deposit_amt = self.collector.parseChange(coins)
                  user_account.deposit(deposit_amt)
                  print(f"New balance: ${user_account.getOwnerBalance}")

      def closeAccount(self):
            # set a list with the valid coin letters
            # call the askAccountNumAndPin function to get the user's input
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            account_number, account_pin = self.askAccountNumAndPin()
            user_account = self.userIsConfirmed(account_number, account_pin)
            if user_account:
                  self.mercado_bank.allbank_accounts.remove(user_account)
                  print(f'Account {user_account.account_num} has been closed')

      def askAccountNumAndPin(self):
            # this is a helper function that will ask for the account number and pin
            # it will return both values which will be saved in separate variables
            account_number = input("Please enter the account number: \n")
            account_pin = input("Please enter the account pin: \n")

            # if the account number is not numeric or the pin is not numeric
            # print a message for th euser and redirect them to the menu again
            # else return the account number and pin number
            if not self.isNumeric(account_number) or not self.isNumeric(account_pin):
                  print("Input must be numeric.")
                  self.menu_redirect()
            else:
                  return int(account_number), int(account_pin)
      
      def randomNums(self,num):
            # loops num amount of times
            # each time, it will call the method generaterandominterger from the bank Utility class
            # it will pass in two numbers, 0 and num
            # it will append the number to a res array
            # returns the array as a joined number
            res = []
            for i in range(0, num):
                  res.append(self.generateRandomInteger(0,num))
            return int("".join(map(str, res)))
      
      def userIsConfirmed(self, account_number, account_pin):
            # looks through the bank's account list
            # if the account number the user inputted is in the bank's list
            # then, check if that account's pin equals the pin the user gave
            # if true, then return the account object
            # else, print the error message and return False
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.getOwnerPin == account_pin:
                              return account
                        else:
                              print("Invalid PIN number")
                  else:
                        print("Account not found for account number: %d" % account_number)    
            return False
      
      
      def verifySecondPin(self, user_account):
            # if there is a user account, ask the user to enter a pin and save it in new_pin variable
            # if the the user_pin is numeric and the length is 4, ask the user to confirm the pin again
            # if the user_pin is the same as the pin that was confirmed, set the account's pin number to the new pin
            # print a success message and return True
            # else, print the error messages, and return False
            if user_account:
                  new_pin = input("Enter new PIN: \n")
                  if self.isNumeric(new_pin):
                        if len(new_pin) == 4:
                              confirmed_pin = input("Enter new PIN again to confirm: \n")
                              if self.isNumeric(confirmed_pin):
                                    if new_pin == confirmed_pin:
                                          user_account.setOwnerPin = int(confirmed_pin)
                                          print("PIN updated")
                                          return True
                                    else:
                                          print("PINs do not match, try again.")
                              else:
                                    print(f"{confirmed_pin} is not a number.")
                        else:
                              print(f"PIN must be 4 digits, try again.")
                  else:
                        print(f"{confirmed_pin} is not a number.")
                  return False
      
      def verifyPositiveAmount(self, user_account, account_number):
            # if there is a user account, and the user account number equals the account number of the object
            # call the promptUserForPositiveNumber function to prompt the user for a positive amount
            # if the above becomes true, then go to the account and deposit the positive amount
            # display the new account balance and return True
            # else, print the error messages, and return False
            if user_account:
                  if user_account.account_num == account_number:
                        user_deposit = self.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): \n")
                        if user_deposit:
                              user_account.deposit(user_deposit)
                              print(f"New balance: ${user_account.getOwnerBalance}")
                              return True
                        else:
                              self.verifyPositiveAmount(user_account, account_number)
                  else:
                        print(f"No user account for ${account_number}")
            return False
            
      
class BankManager(Bank, Account, CoinCollector, BankUtility): 
      mercado_bank = Bank()
      collector = CoinCollector() 
      
      def __init__(self): 
            super().__init__()
            
      def initialize(self):
            print(logo)
            self.menu_redirect()
