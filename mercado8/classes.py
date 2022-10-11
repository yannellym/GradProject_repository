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
       
      def deposit(self, amount):
            # adds the amount to the account balance and returns
            # the new account balance
            self.balance += amount
            return self.balance
      
      def withdraw(self, amount):
            # subtracts the amount from the account balance and returns
            # the new account balance
            # if not enough funds available, returns a string 
            if self.balance > 0:
                  self.balance -= amount
                  return self.balance
            else:
                  return "not enough funds available"
      
      def isValidPIN(pin):
            
            
            # implement isValidPIN here
            
            return False  # be sure to change this
      
      
      # all objects have a toString method - this indicates you are providing
      # your own version
      def __repr__(self):
            return "" # change this as needed

class Bank():
      def addAccountToBank(account):
            
        # implement addAccountToBank here
        
        return False; # be sure to change this as needed
      def removeAccountFromBank(account):
            # implement removeAccountFromBank here
            
            return False; # be sure to change this as needed
      
      def findAccount(accountNumber):
            
            return  # be sure to change this as needed
      
      def addMonthlyInterest(percent):
            pass
        # EXTRA CREDIT


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
