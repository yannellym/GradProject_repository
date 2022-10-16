import random, math
from art import logo

class Bank:
      def __init__ (self):
            # stores all the accounts in the bank
            # has a set number of accounts that it can support
            self.allbank_accounts = []
            self.numaccounts_supported = 10
            
            
      def addAccountToBank(self, account): # 2 unit tests need to be implemented
            # parameter received of type: OBJECT
            # adds the account to the allbank_accounts list only if:
            # the list length is less than the number of accounts supported
            # returns True if the account is added to the allbank_accounts list
            # print a message if the account is not added and returns False
            if len(self.allbank_accounts) < self.numaccounts_supported:
                  self.allbank_accounts += account
                  return True
            print("No more accounts available")
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
      
      def addMonthlyInterest(self, percent): # 2 unit tests need to be implemented
            # parameter received of type: FLOAT
            # iterates through all the accounts in the list
            # deposits a monthly interest payment into every account
            # monthly interest is the current balance of the account nultiplied by the monthly interest rate
            for stored_account in self.allbank_accounts:
                  monthly_interest =  stored_account.balance * (percent / 12)
                  stored_account.balance += monthly_interest

class Account:
      def __init__ (self, account_number, owner_fname, owner_lname, ssn, pin):
            self.account_num = account_number
            self.owner_firstname = owner_fname
            self.owner_lastname = owner_lname
            self._social = ssn
            self.pin_num = pin
            self.balance = 0.00
            
      # add methods as getters and setters for attributes  
      # ONLY THROUGH FUNCTIONS ACCESS    
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
            self.balance += balance
      
    
      def deposit(self, amount): # 2 unit tests need to be implemented
            # adds the amount to the account balance and returns
            # the new account balance
            self.setOwnerBalance(amount)
            return self.getOwnerBalance
      
      def withdraw(self, amount): # 2 unit tests need to be implemented
            # subtracts the amount from the account balance and returns
            # the new account balance
            # if not enough funds available, returns a string 
            if self.getOwnerBalance() > 0:
                  new_balance = self.getOwnerBalance - amount
                  self.setOwnerBalance(new_balance)
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
            coin_list = [*coins]
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
      
class BankManager(Bank, Account, CoinCollector): 
      mercado_bank = Bank()
      collector = CoinCollector()
      
      def __init__(self): 
            super().__init__()
            
       # This is where you will implement your  method and start 
       # the program from.  The BankManager class should create 
       # an instance 
       # of a Bank object when the program runs and use that instance to 
       # manage the Accounts in the bank 
            
      # @staticmethod     
      # promptForAccountNumberAndPIN(bank):
            
      #       # implement promptForAccountNumberAndPIN here 
      #       # takes one parameter, a Bank object that represents the bank. 
      #       # The method should prompt the user to enter an account number 
      #       # and then try to find a matching account with that accountnumber 
      #       # in the bank. 
      #       return # be sure to change this as needed 
      def run_main(self):
            print(logo)
            self.menu_redirect()
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
            self.options()
            user_choice = int(input("Please input choice number: "))
            choices = [1,2,3,4,5,6,7,8,9,10,11]
            
            if user_choice not in choices:
                  print("invalid choice, please try again.")
                  self.options()  
            else:
                  if user_choice == 11:
                        print("*** Thank you for using MercadoBank. Have a nice day! ***")
                  else:
                        match user_choice:
                              case 1:
                                    print(self.openAccount())
                                    print("Account creation successful!") 
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
                  
      
      def openAccount(self):
            user_fname = input("Enter Account owner's first name:\n")
            user_lname = input("Enter Account owner's last name: \n")
            user_ssn = input("Enter Account owner's SSN (9 DIGITS): \n")
            # calls the randomNums function to generate 9 random numbers
            account_num = self.randomNums(9)
            # if the account number is already in the bank's account list
            # generate another account number
            if account_num in self.mercado_bank.allbank_accounts:
                  account_num = self.randomNums(9)
            # calls the randomNums function to generate 4 random numbers
            pin = self.randomNums(4)
            # creates a new account object and passes in the users inputs
            new_account = Account(account_num,user_fname, user_lname, user_ssn, pin)
            # Adds this account number to the bank's account list
            self.mercado_bank.allbank_accounts.append(new_account)
            # print(mercado_bank.allbank_accounts)
            # returns the account information for the user
            return new_account.__repr__()

      def getAccountInfoAndBalance(self):
            account_number, account_pin = self.askAccountNumAndPin()
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            # return the account's information
            # else, print "invalid account number" or "invalid pin number"
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              print("Looking for account...")
                              return account.__repr__()
                        else:
                              print("Invalid PIN number")
            
            print("Account not found for account number: %d" % account_number)
      
      def changePin(self):   
            account_number, account_pin = self.askAccountNumAndPin()
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            # ask the user to input a new pin number and confirm that number again
            # if the confirmed pin equals the new pin given by the user:
            # change the account's pin number to the new pin number
            # else, print that it is an invalid pin number or an invalid account number
            for account in self.mercado_bank.allbank_accounts:
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
                                    self.menu_redirect()
                        else:
                              print("Invalid PIN number")
                  else:
                        print("Invalid account number")

      def depositMoneyToAccount(self): # REFACTOR
            account_number, account_pin = self.askAccountNumAndPin()
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            # ask the user to input a deposit amount. Save it as a float in a avariable
            # if the deposit amount is < or equal to zero, print a message for user to try again
            # else, call the deposit amount, and deposit the money in the account
            # print the account's information
            # if any account information doesn't match, redirect user to menu again
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              self.deposit_amount = float(input("Please enter an amount to deposit: \n"))
                        if self.deposit_amount <= 0:
                              print("Amount cannot be negative. Try again.")
                        else:
                              account.deposit(self.deposit_amount)
                              print(f"New balance: ${account.balance}")
            self.menu_redirect()

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
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              print("**Account to transfer to**:")
                              t_account_number, t_account_pin = self.askAccountNumAndPin()
                              for t_account in self.mercado_bank.allbank_accounts:
                                    if t_account.account_num == t_account_number:
                                          if t_account.pin_num == t_account_pin:
                                                deposit_amount = float(input("Please enter an amount to deposit in dollars and cents (Ex, 5.99): \n"))
                                                if account.balance <= 0:
                                                      print("Amount cannot be negative. Try again.")
                                                elif account.balance < deposit_amount:
                                                      print("Not enough funds to transfer. Try again.")
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
            self.menu_redirect()

      def withdrawFromAccount(self): # REFACTOR
            # search through the bank's list of accounts
            # if the account number equals the account number given by the user
            # if the account's pin number equals the pin number given by the user
            account_number, account_pin = self.askAccountNumAndPin()
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              withdraw_amount = float(input("Please enter an amount to withdraw in dollars and cents (Ex, 5.99): \n"))
                              if withdraw_amount <= 0:
                                    print("Amount cannot be negative. Try again.")
                              elif account.balance < withdraw_amount:
                                    print("Not enough funds to withdraw. Try again.")
                              else:
                                    account.withdraw(withdraw_amount)
                                    print(f"New balance: ${account.balance}")
            self.menu_redirect()

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
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              self.withdraw_amount = int(input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1,000): \n"))
                        if self.withdraw_amount < 5 or self.withdraw_amount > 1000 or self.withdraw_amount %5 != 0:
                              print("Invalid amount. Try again.")
                        elif account.balance < self.withdraw_amount:
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
                              account.withdraw(self.withdraw_amount)
                              print(f"New balance: ${account.balance}")

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
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              coins = input("Deposit coins (P: penny, N: nickel, D: dime, Q: Quarter, H: half-dollar, W: whole-dollar) Ex(QPDNNDHW): \n").upper()
                        
                              deposit_amt = self.collector.parseChange(coins)
                              account.deposit(deposit_amt)
                              print("deposit amt:" ,deposit_amt)
                              print("account balance:", account.balance)
                              print(f"New balance: ${account.balance}")
                        else:
                              print("Wrong account PIN. Try again.")
                  else:
                        print("Wrong account number. Try again.")
            self.menu_redirect()

      def closeAccount(self):
      # set a list with the valid coin letters
      # call the askAccountNumAndPin function to get the user's input
      # search through the bank's list of accounts
      # if the account number equals the account number given by the user
      # if the account's pin number equals the pin number given by the user
            account_number, account_pin = self.askAccountNumAndPin()
            for account in self.mercado_bank.allbank_accounts:
                  if account.account_num == account_number:
                        if account.pin_num == account_pin:
                              self.mercado_bank.allbank_accounts.remove(account)
                              print(f'Account {account.account_num} has been closed')
                        else:
                              print("Wrong account PIN. Try again.")
                  else:
                        print("Wrong account number. Try again.")
            self.menu_redirect()

      def addMonthlyInterest(self):
      # look through all of the account in the bank's account list
      # calculate the monthly rate by multiplying the account balance times the annual rate
      # then, divide that by twelve
      # then, turn that into an integer (two digits) and divide it by 100 to give you a value
      # save the above value into a variable named monthly rate
      # add this amount to the account's balance
      # display the account balance as a string
            annual_rate = float(input("Enter annual rate percentage (e.g 2.75 for 2.75%): \n"))
            for account in self.mercado_bank.allbank_accounts:
                  monthly_rate = int(((annual_rate  * account.balance) / 12)) / 100
                  account.balance += monthly_rate
                  print(f"Deposited interest: {monthly_rate} into account number: {account.account_num}, new balance: ${account.balance}")
                              
                  
      def askAccountNumAndPin(self):
      # this is a helper function that will ask for the account number and pin
      # it will return both values which will be saved in separate variables
            account_number = int(input("Please enter the account number: \n"))
            account_pin = int(input("Please enter the account pin: \n"))
            return account_number, account_pin
            
      def randomNums(self,num):
      # loops num amount of times
      # each time, it will call the method generaterandominterger from the bank Utility class
      # it will pass in two numbers, 0 and num
      # it will append the number to a res array
      # returns the array as a joined number
            res = []
            for i in range(num):
                  res.append(BankUtility.generateRandomInteger(0,num))
            return int("".join(map(str, res)))
      

class BankUtility:
      def __init__ (self):
            pass
      def promptUserForString(self, prompt):
            # parameter received of type: STRING
            # string prompt will print on the screen and ask the user to input information
            # method will return the user's response as a string
            user_response = prompt
            return user_response
      
      def promptUserForPositiveNumber(self, prompt):
            # parameter received of type: STRING
            # prompts use to enter a positive number
            # if the number is less than or equal to zero
            # will print a message and loop again
            # if number is positive, will return the number
            user_response = eval(prompt)
            if user_response <= 0:
                  print("Amount cannot be negative. Try again")
                  self.promptUserForPositiveNumber(prompt)
            else:
                  return user_response
                  
      
      def generateRandomInteger(min, max): # needs 2 unit tests
            # parameters received of type: INT
            # takes in the min and max value and generates a random integer between these two numbers (both inclusive)
            # returns the random integer 
            ran_num = random.randint(min, max + 1)
            return ran_num
      
      def convertFromDollarsToCents(amount):        # needs 2 unit tests
            # parameter received of type: FLOAT  
            # takes in a float and converts it to string
            # will remove the dots in the string
            # return the string as a number 
            new_amount = str(amount).replace(".", "")
            return int(new_amount)
      
      def isNumeric(numberToCheck): # needs 2 unit tests
            try:
                  if numberToCheck.isdigit():
                        return True
                  else:
                        return False
            except ValueError:
                  return False
