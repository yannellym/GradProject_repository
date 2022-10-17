from classes import BankManager
import unittest

# tests to check the functions' functionality
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
    # def test_depositValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     deposit = 500
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.deposit(500), 500.00)
    
    # def test_depositInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     deposit = "SFSDF"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.deposit(deposit), "Deposit amount must be a positive number")
    
    # def test_withdrawValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     program.deposit(500)
    #     withdraw_amt = 400
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.withdraw(withdraw_amt), 100)
    
    # def test_withdrawInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_isValidPinValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
    # def test_isValidPinInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
        
    # 2 unit tests for EACH: addAccounToBank, removeAccountFromBank, findAccount, addMonthly interest in Bank
    # def test_addAccounToBankValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     deposit = 500
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.deposit(500), 500.00)
    
    # def test_addAccounToBankInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     deposit = "SFSDF"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.deposit(deposit), "Deposit amount must be a positive number")
    
    # def test_removeAccountFromBankValid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     program.deposit(500)
    #     withdraw_amt = 400
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.withdraw(withdraw_amt), 100)
    
    # def test_removeAccountFromBankInvalid(self):
    #     # Arrange
    #     program = BankManager()
    #     # Act
    #     coins = "lllAaTi"
    #     # Assert
    #     # will check if the return from the parsechange method is correct
    #     # answer should be equal to the amount of valid coins
    #     self.assertEqual(program.parseChange(coins), 0)
    
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