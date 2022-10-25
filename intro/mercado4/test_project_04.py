
from classess import Rectangle, Parallelepiped
import unittest

# tests to check the functions' functionality
class TestShip(unittest.TestCase): 
    
    def test_rectangle_perim(self):
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        rectangle = Rectangle(10,20)
        #Assert
        # will check if the perimiter for the rectangle was calculated correctly
        # perimeter should equal the user's length input plus the user's height input multiplied by 2
        self.assertEqual(rectangle.perimeter(),60)
        
    def test_rectangle_area(self):
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        rectangle = Rectangle(10,20)
        #Assert
        # area should equal the user's length input multiplied by the user's height
        self.assertEqual(rectangle.area(),200)
        
    def test_rectangle_display(self):
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        rectangle = Rectangle(10,20)
        #Assert
        # display should show the rectangle's length, width, perimter, and area. 
        self.assertEqual(rectangle.display(), f"The length is {rectangle.length}, the width is {rectangle.width}, the perimeter is {rectangle.perimeter()}, and the area is {rectangle.area()}.")

    def test_parallelepid_perim(self):
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        parallelepid = Parallelepiped(7,5,6)
        #Assert
        # perimeter should equal the user's length input plus the user's height input multiplied by 2
        self.assertEqual(parallelepid.perimeter(), 24)
            
    def test_parallelepid_area(self):
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        parallelepid = Parallelepiped(8,10,9)
        #Assert
        self.assertEqual(parallelepid.area(), 80)

    def test_parallelepid_display(self):
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        parallelepid = Parallelepiped(10,20 ,15)
        #Assert
        self.assertEqual(parallelepid.display(), f"The length is {parallelepid.length}, the width is {parallelepid.width}, the perimeter is {parallelepid.perimeter()}, and the area is {parallelepid.area()}.")

    def test_parallelepid_volume(self): 
        #Arrange
        #Act
        #references the rectangle class and passes in the user's inputs
        parallelepid = Parallelepiped(14,6,7)
        #Assert
        self.assertEqual(parallelepid.volume(), parallelepid.height * 14 * 6)

if __name__ == '__main__':
    unittest.main()