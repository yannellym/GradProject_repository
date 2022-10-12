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
            self.account_num = account_number,
            self.owner_firstname = owner_fname,
            self.owner_lastname = owner_lname,
            self.social = ssn,
            self.pin_num = pin,
            self.balance = 0
            
    
      # add methods as getters and setters for attributes
       
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
                  Account(account_number = 
                  {self.account_number}, owner_fname = {self.owner_fname},
                  owner_lname = {self.owner_lname}, ssn = "XXX-XXX-" + {self.ssn}, 
                  pin = {self.pin_num}, balance = {self.balance})
                  '''

class Bank():
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
            
            


class CoinCollector():
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
      
      
      
class BankUtility():
      def __init__ (self):
            pass
      def promptUserForString(prompt):
            # implement promptUserForString here
            
            return "" # be sure to change this
      def promptUserForPositiveNumber(prompt):
            
            # implement promptUserForPositiveNumber here
            
            return 0.0 # be sure to change this
      
      def generateRandomInteger(min, max):
            # implement generateRandomInteger here
            
            return 0 # be sure to change as needed
      
      def convertFromDollarsToCents(amount):        
            # implement convertFromDollarsToCents here     
            
            return 0 # be sure to change as needed
      
      '''
            Checks if a given string is a number (long)
            This does NOT handle decimals.
            
            YOU DO NOT NEED TO CHANGE THIS METHOD
            THIS IS FREE FOR YOU TO USE AS NEEDED
            
            @param numberToCheck String to check
            @return true if the String is a number, false otherwise
      '''
      def isNumeric(numberToCheck):
            try:
                  if numberToCheck.isdigit():
                        return True
                  else:
                        return False
            except ValueError:
                  return False
