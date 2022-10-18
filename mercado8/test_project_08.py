from classes import BankManager, Account
import unittest

# tests to check the methods' functionality
class TestBankManager(unittest.TestCase): 
    
    # 3 test cases for parseChange method
    def test_parseChange(self):
        # Arrange
        program = BankManager()
        # Act
        coins = "XXXXWWWWWWWWWW"
        # Assert
        # will check if the return from the parsechange method is correct
        # answer should be equal to the amount of valid coins
        self.assertEqual(program.parseChange(coins), 10.00)
    
    def test_parseChangeWithLower(self):
        # Arrange
        program = BankManager()
        # Act
        coins = "qxqxqxqxhhhh"
        # Assert
        # will check if the return from the parsechange method is correct
        # answer should be equal to the amount of valid coins
        self.assertEqual(program.parseChange(coins), 3.00)
    
    def test_parseChangeWithInvalids(self):
        # Arrange
        program = BankManager()
        # Act
        coins = "lllAaTi"
        # Assert
        # will check if the return from the parsechange method is correct
        # answer should be equal to the amount of valid coins
        self.assertEqual(program.parseChange(coins), 0)
       
        
    # 2 unit tests for EACH: deposit, withdraw, isvalidpin in Account
    def test_depositValid(self):
        # Arrange
        program = BankManager()
        account = Account("123456789", "nelly", "merc", "098765432", "6767")
        # Act
        deposit_amt = 500
        # Assert
        # will check if the return from the deposit method is correct
        # answer should be equal to the amount of deposit_amt
        self.assertEqual(account.deposit(deposit_amt), 500.00)
    
    def test_depositInvalid(self):
        # Arrange
        program = BankManager()
        account = Account("123456789", "nelly", "merc", "098765432", "6767")
        # Act
        deposit_amt = -5
        # Assert
        # will check if the return from the deposit method is correct
        # answer should be equal to the amount of deposit_amt
        self.assertEqual(account.deposit(deposit_amt), False)
        

    def test_withdrawValid(self):
        # Arrange
        program = BankManager()
        account = Account("123456789", "nelly", "merc", "098765432", "6767")
        account.setOwnerBalance = 500
        # Act
        withdraw_amt = 100
        # Assert
        # will check if the return from the withdraw method is correct
        # answer should be equal to the amount of the account balance minus the withdraw amount
        self.assertEqual(account.withdraw(withdraw_amt), 400)
    
    def test_withdrawInvalid(self):
        # Arrange
        program = BankManager()
        account = Account("123456789", "nelly", "merc", "098765432", "6767")
        account.setOwnerBalance = 500
        # Act
        withdraw_amt = 1000
        # Assert
        # will check if the return from the withdraw method is correct
        # answer should be equal to the amount of the account balance minus the withdraw amount
        self.assertEqual(account.withdraw(withdraw_amt), "Not enough funds available")
    
    def test_isValidPinValid(self):
       # Arrange
        program = BankManager()
        account = Account("123456789", "nelly", "merc", "098765432", "6767")
        account.setOwnerBalance = 500
        # Act
        pin = 6767
        # Assert
        # will check if the return from the isValidPin method is correct
        # answer should be equal to the pin variable
        self.assertEqual(account.isValidPIN(pin), True)
    
    def test_isValidPinInvalid(self):
        # Arrange
        program = BankManager()
        account = Account("123456789", "nelly", "merc", "098765432", "6767")
        account.setOwnerBalance = 500
        # Act
        pin = 6760
        # Assert
        # will check if the return from the isValidPin method is correct
        # answer should be equal to the pin variable
        self.assertEqual(account.isValidPIN(pin), False)
    
        
    # 2 unit tests for EACH: addAccounToBank, removeAccountFromBank, findAccount, addMonthly interest in Bank
    def test_addAccounToBankValid(self):
        # Arrange
        program = BankManager()
        account = Account("987654321", "nelly", "merc", "098765432", "6767")
        # Act
        # Assert
        # will check if the return from the addAccounttobank method is correct
        # answer should be equal True if valid and False if not
        self.assertEqual(program.addAccountToBank(account), True)
    
    def test_addAccounToBankInvalid(self):
        # Arrange
        program = BankManager()
        account = Account("123456787", "nelly", "merc", "098765432", "6767")
        
        for i in range(100):
            program.mercado_bank.allbank_accounts.append(account)
        # Act
        # Assert
        # will check if the return from the addAccounttobank method is correct
        # answer should be equal True if valid and False if not
        self.assertEqual(program.addAccountToBank(account), False)
        
    def test_removeAccountFromBankValid(self):
        # Arrange
        program = BankManager()
        account = Account("123456787", "nelly", "merc", "098765432", "6767")
        
        program.mercado_bank.allbank_accounts.append(account)
        # Act
        # Assert
        # will check if the return from the removeAccountFromBank method is correct
        # answer should be equal True if valid and False if not
        self.assertEqual(program.removeAccountFromBank(account), True)
    
    def test_removeAccountFromBankInvalid(self):
        # Arrange
        program = BankManager()
        account = Account("124848487", "Mark", "Zurc", "0983465432", "6967")
        
        program.allbank_accounts.append(account)
        account2 = Account("123348487", "Mae", "Zoo", "098423423432", "6067")
        # Act
        # Assert
        # will check if the return from the removeAccountFromBank method is correct
        # answer should be equal True if valid and False if not
        self.assertEqual(program.removeAccountFromBank(account2), False)
    
    # def test_findAccountValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_findAccountInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_addMonthlyInterestValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_addMonthlyInterestInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    
     # 2 unit tests for EACH: aisNumeric, convertFromDollarsToCents, generateRandomInteger in BankUtility
    # def test_isNumericValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     deposit = 500
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.deposit(500), 500.00)
    
    # def test_isNumericInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     deposit = "SFSDF"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.deposit(deposit), "Deposit amount must be a positive number")
    
    # def test_rconvertFromDollarsToCentsValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     program.deposit(500)
    #     withdraw_amt = 400
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.withdraw(withdraw_amt), 100)
    
    # def test_convertFromDollarsToCentsInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_generateRandomIntegerValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_generateRandomIntegerInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    
if __name__ == '__main__':
    unittest.main()