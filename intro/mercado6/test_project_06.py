from classes import Deque
import unittest

# tests to check the functions' functionality
class TestStudent(unittest.TestCase): 
    
    def test_Display(self):
        # Arrange
        # Act
        # references the Deque class and passes in the corresponding string parameters
        people = ["Ana" , "Bob", "Carmen", "Dylan"]
        line = Deque(people)
        # Assert
        # will check if the return from the display method is correct
        # answer should be equal to the status of the line
        self.assertEqual(line.display(), people)
        
    def test_addToBack(self):
        # Arrange
        # Act
        # references the Deque class and passes in the corresponding string parameters
        people = ["Ana" , "Bob", "Carmen", "Dylan"]
        line = Deque(people)
        # Assert
        # will check if the return from the addToBack method is correct
        # answer should be equal to the res variable. 
        # It should have elizabeth added to the back of the line
        res = ['Ana', 'Bob', 'Carmen', 'Dylan', 'Elizabeth']
        self.assertEqual(line.addToBack("Elizabeth"), res)
        
    def test_addToFront(self):
        # Arrange
        # Act
        # references the Deque class and passes in the corresponding string parameters
        people = ["Ana" , "Bob", "Carmen", "Dylan"]
        line = Deque(people)
        # Assert
        # will check if the return from the addToFront method is correct
        # answer should be equal to the res variable. 
        # It should have Aaron added to the front of the line
        res = ['Aaron','Ana', 'Bob', 'Carmen', 'Dylan']
        self.assertEqual(line.addToFront("Aaron"), res)
        
if __name__ == '__main__':
    unittest.main()