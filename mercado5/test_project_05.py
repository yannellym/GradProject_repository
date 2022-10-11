
from classess import Student, Medical, Engineer
import unittest

# tests to check the functions' functionality
class TestStudent(unittest.TestCase): 
    
    def test_StudentDisplay(self):
        # Arrange
        # Act
        # references the Student class and passes in the corresponding string parameters
        general_student = Student("Maria", "16")
        # Assert
        # will check if the return from the display method is correct
        # answer should equal the object's name and age.
        self.assertEqual(general_student.display(),"The name is Maria and age is 16.")
        
    def test_EngineerDisplay(self):
        # Arrange
        # Act
        # references the Engineer class and passes in the corresponding string parameters
        engineer = Engineer("Bob", "30", "Data structures and algorithms")
        # Assert
        # will check if the return from the displayEngineer method is correct
        # answer should equal the object's name, age, and course/s.
        self.assertEqual(engineer.displayEngineer(), "The name is Bob and age is 30. The course is Data structures and algorithms.")
        
    def test_MedicalDisplay(self):
        #Arrange
        #Act
        # references the Engineer class and passes in the corresponding string parameters
        medical = Medical("Krishna", "21", "Medical City")
        #Assert
        # will check if the return from the displayEngineer method is correct
        # answer should equal the object's name, age, and course/s.
        self.assertEqual(medical.displayDoctor(), "The name is Krishna and age is 21. The hospital is Medical City.")

if __name__ == '__main__':
    unittest.main()