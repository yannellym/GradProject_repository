import random
from art import logo

class BankManager:
      
      
      
      def __init__(self): 
            pass
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
   

class Account():
      def __init__ (self, account_number, owner_fname, owner_lname, ssn, pin):
            self.account_num = account_number
            self.owner_firstname = owner_fname
            self.owner_lastname = owner_lname
            self._social = ssn
            self.pin_num = pin
            self.balance = 0.00
            
      # add methods as getters and setters for attributes      

      def getOwnerFirstName(self):
            return self.owner_firstname
      
      def setOwnerFirstName(self, name):
            self.owner_firstname = name
      
      def getOwnerLastName(self):
            return self.owner_lastname
      

      def setOwnerLastName(self, name):
            self.owner_lastname = name
      
      @property
      def getOwnerSocial(self):
            return self._social
      
      @getOwnerSocial.setter
      def setOwnerSocial(self, digits):
            self._social = digits
      

      def getOwnerPin(self):
            return self.pin_num
      

      def setOwnerPin(self, new_pin):
            self.pin_num = new_pin
    
       
      def deposit(self, amount): # 2 unit tests need to be implemented
            # adds the amount to the account balance and returns
            # the new account balance
            self.balance += amount
            return self.balance
      
      def withdraw(self, amount): # 2 unit tests need to be implemented
            # subtracts the amount from the account balance and returns
            # the new account balance
            # if not enough funds available, returns a string 
            if self.balance > 0:
                  self.balance -= amount
                  return self.balance
            return "not enough funds available"
      
      def isValidPIN(self, pin): # 2 unit tests need to be implemented
            # if the pin entered matches the pin of the account
            # return true, false otherwise
            if self.pin_num == pin:
                  return True
            return False
      
      def __repr__(self):
            # returns a string of all of the information of the account class
            return f'''
                  Account_number : {self.account_num}
                  Owner First Name : {self.owner_firstname}
                  Owner Last name : {self.owner_lastname}
                  Owner SSN : XXX-XXX-{self._social[-4:]}
                  pin = {self.pin_num}
                  balance = ${self.balance}
                  '''

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
class CoinCollector:
      # constructor so you cannot instantiate this class
      def __init__(self):
            pass
      
      def parseChange(coins, change): # needs 3 unit tests
            # will look through each character in the string
            # if the character matches any of the letter below, it will return the value
            for char in change:
                  match char:
                        case "P":
                              return .01
                        case "N":
                              return .05
                        case "D":
                              return .10
                        case "Q":
                              return .25
                        case "H":
                              return .50
                        case "W":
                              return .100
                        case "":
                              return 0   
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
