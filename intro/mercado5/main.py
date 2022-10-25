from classess import Student, Engineer, Medical

#Project 5
# There is a generic Student class. Create two types of students -- a child class Engineer and a child class Medical.

# Create a Python class Student with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Student class.
# Create children's classes Engineer and Doctor which inherit from the student class. An engineer also has a courses attribute and doctor has a hospital attribute.
# Create methods displayEngineer() and displayDoctor that displays the name, age, and courses or hospital of an object created via the children classes.
# Create an engineer and doctor objects via an instantiation on the engineer and doctor classes and then test the displayEngineer and displayDoctor methods.

'''
    File name: project_05.py
    Author: Yannelly Mercado
    Date created: 9/24/2022
    Date last modified: 9/24/2022
    Python Version: 2.7.18
'''

def main():
    # generic is created using an instantiation of the Student class
    generic = Student("Jose", "18")
    # this displays the generic's name, and age.
    print(generic.display())
    
    # medical is created using an instantiation of the of the Medical class who inherits from the Student class.
    medical = Medical("Pablo", "22", "Children's Hospital")
    # this displays the medical's name, age, and hospital.
    print(medical.displayDoctor())

    # engineer is created using an instantiation of the of the Engineer class who inherits from the Student class.
    engineer = Engineer("Yannelly", "27", "Intro to programming" )
    # this displays the engineer's name, age, and courses.
    print(engineer.displayEngineer())

# calls the function main   
main()