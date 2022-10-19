from classes import BankManager, Account, Bank
import unittest

# tests to check the methods' functionality


class TestBankManager(unittest.TestCase):

    # 3 test cases for parseChange method
    def test_parseChange(self):
        # Arrange
        program = BankManager()
        # Act
        coins = "XXWWWWWWWWWW"
        # Assert
        # will check if the return from the parsechange method is correct
        # answer should be equal to the amount of valid coins
        self.assertEqual(program.parseChange(coins), 10.00)

    def test_parseChangeWithLower(self):
        # Arrange
        program = BankManager()
        # Act
        coins = "qxqqqxhhhh"
        # Assert
        # will check if the return from the parsechange method is correct
        # answer should be equal to the amount of valid coins
        self.assertEqual(program.parseChange(coins), 3.00)

    def test_parseChangeWithInvalids(self):
        # Arrange
        program = BankManager()
        # Act
        coins = "lAaTi"
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
        new_account = Account("987654321", "nelly",
                              "merc", "198765432", "6767")
        # Act
        # Assert
        # will check if the return from the addAccounttobank method is correct
        # answer should be equal True if valid and False if not
        self.assertEqual(program.addAccountToBank(new_account), True)

    def test_addAccounToBankInvalid(self):
        # Arrange
        new_program = BankManager()
        print("accounts", new_program.allbank_accounts)

        # will add 100 accounts to the bank's account list
        for i in range(100):
            account = Account(
                f"123456{i if i > 9 else i+10}", "nelly", "merc", "098765432", "6767")
            new_program.allbank_accounts.append(account)
        # Act
        # Assert
        # will check if we can add anothe account to the bank,
        # this should return false as there are already 100 accounts in the bank
        self.assertEqual(new_program.addAccountToBank(account), False)

    def test_removeAccountFromBankValid(self):
        # Arrange
        program = BankManager()
        account = Account("123456787", "nelly", "merc", "098765432", "6767")

        program.allbank_accounts.append(account)
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

    def test_findAccountValid(self):
        # Arrange
        program = BankManager()
        # Act
        new_account = Account("987654321", "nelly",
                              "merc", "198765432", "6767")
        program.allbank_accounts.append(new_account)
        # Assert
        # will check if the return from the findAccount method is correct
        # answer should be equal the new_account created
        self.assertEqual(program.findAccount(
            new_account.account_num), new_account)

    def test_findAccountInvalid(self):
        # Arrange
        program = BankManager()
        # Act
        new_account = Account("8787865er67", "david",
                              "luz", "15655432", "6867")
        # Assert
        # will check if the account is not in the bank
        # answer should be equal to account not found
        self.assertEqual(program.findAccount(
            new_account.account_num), "Account not found")

    def test_addMonthlyInterestValid(self):
        # Arrange
        program = BankManager()
        # Act
        rate = 1.25
        account = Account("987654321", "nelly", "merc", "198765432", "6767")
        # Assert
        # will check if the interest was added to all of the account
        # answer should be equal to True
        self.assertEqual(program.addMonthlyInterest(rate), True)

    def test_addMonthlyInterestAlsoValid(self):
       # Arrange
        program = BankManager()
        # Act
        rate = 1.25
        account = Account("147654329", "Verma", "Zoe", "198465432", "6767")
        program.allbank_accounts.append(account)
        # Assert
        # will check if the interest was added to all of the account
        # answer should be equal to true
        self.assertEqual(program.addMonthlyInterest(rate), True)

     # 2 unit tests for EACH: isNumeric, convertFromDollarsToCents, generateRandomInteger in BankUtility

    def test_isNumericValid(self):
        # Arrange
        program = BankManager()
        # Act
        numberToCheck = '500'
        # Assert
        # will check if the string numberToCheck is a valid number
        # answer should be equal to True
        self.assertEqual(program.isNumeric(numberToCheck), True)

    def test_isNumericInvalid(self):
        # Arrange
        program = BankManager()
        # Act
        numberToCheck = 'five hundred dollars'
        # Assert
        # will check if the string numberToCheck is a valid number
        # answer should be equal to False
        self.assertEqual(program.isNumeric(numberToCheck), False)

    def test_rconvertFromDollarsToCentsValid(self):
        # Arrange
        program = BankManager()
        # Act
        amt = 500
        # Assert
        # will take in a float number presenting dollars
        # will conver it from dollars to cents
        # result should equal the amt times 100
        self.assertEqual(program.convertFromDollarsToCents(amt), 50000)

    def test_convertFromDollarsToCentsInvalid(self):
        # Arrange
        program = BankManager()
        # Act
        amt = "Five hundred"
        # Assert
        # will take in a float number presenting dollars
        # will conver it from dollars to cents
        # result should equal the amt times 100
        self.assertEqual(program.convertFromDollarsToCents(amt), False)

    def test_generateRandomIntegerValid(self):
        # Arrange
        program = BankManager()
        # Act
        min = 1
        max = 9
        # Assert
        # will check if the return from the generateRandomInteger method return 1 or 2
        # answer should be equal to either 1 or 2
        self.assertEqual(type(program.generateRandomInteger(min, max)), int)

    def test_generateRandomIntegerInvalid(self):
        # Arrange
        program = BankManager()
        # Act
        min = 1
        max = "32"
        # Assert
        # will check if the return from the generateRandomInteger method return 1 or 2
        # answer should be equal to False
        self.assertEqual(program.generateRandomInteger(min, max), False)

    def test_randomNumsAccountValid(self):
        # Arrange
        program = BankManager()
        # Act
        num = 8
        # Assert
        # will check if the return from the randomNums method if the length is 8
        # answer should be equal to 8
        self.assertEqual(len(str(program.randomNums(num))), 8)
        
    def test_randomNumsPinValid(self):
        # Arrange
        program = BankManager()
        # Act
        num = 4
        # Assert
        # will check if the return from the randomNums method if the length is 4
        # answer should be equal to 4
        self.assertEqual(len(str(program.randomNums(num))), 4)


if __name__ == '__main__':
    unittest.main()
