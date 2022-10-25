import unittest

class BankAccount:
  def __init__(self, id):
    self.id = id
    self.balance = 0

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      return True
    return False

  def deposit(self, amount):   
    self.balance += amount
    return True
  
class TestBankOperations(unittest.TestCase):
  def test_insufficient_deposit(self):
    #Arrange
    a = BankAccount(1)
    a.deposit(100)
    
    #Act
    outcome = a.withdraw(200)
    
    #Assert
    self.assertFalse(outcome)
    
  def test_negative_deposit(self):
    # Arrange
    a = BankAccount(1)
    # Act
    outcome = a.deposit(-100)
    # Assert
    self.assertFalse(outcome)    
