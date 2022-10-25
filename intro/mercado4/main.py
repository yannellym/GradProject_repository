from classess import Rectangle, Parallelepiped
import pydoc
pydoc.help()
#Project 4
#Write a Rectangle class in Python language, allowing you to build a rectangle wi4th length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.
# Create a method display() that displays the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

'''
    File name: project_04.py
    Author: Yannelly Mercado
    Date created: 9/11/2022
    Date last modified: 9/18/2022
    Python Version: 2.7.18
'''

def main():
    # user will be prompted to enter a length and a width attribute.
    user_length = input("Please input a length: ")
    user_width = input("Please input a width: ")
    
    if not user_length.isnumeric() or not user_width.isnumeric():
        print("Please only input numeric values.")
        main()
    #shape_1 is created using an instantiation of the Rectangle class.
    shape_1 = Rectangle(int(user_length), int(user_width))
    # displays the information about the Rectangle class.
    print(shape_1.display())

    # shape_2 is created using an instantiation of the Parallelepiped 
    # class who has inherited from the parent Rectangle class.
    user_height = eval(input("Please input a height: "))
    shape_2 = Parallelepiped(int(user_length), int(user_width), int(user_height))
    # calculates the volume of the Parallelepiped. 
    print(f"the volume is: {shape_2.volume()}")
    
main()