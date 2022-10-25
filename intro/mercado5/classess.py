class Student: # Parent class 
      def __init__(self, name, age):
            self.name = name
            self.age = age
      
      def display(self): # this method will dispaly name and age of an object created by this class
            return f"The name is {self.name} and age is {self.age}."
            
class Engineer(Student): # Child class inherits the parent Student class. 
      def __init__(self, name, age, courses):
            super().__init__(name, age)
            self.courses = courses
            
      def displayEngineer(self): # this method will display name, age, and course/s of an object created by this class
            return f"The name is {self.name} and age is {self.age}. The course is {self.courses}."
      
class Medical(Student): # Child class inherits the parent Student class. 
      def __init__(self, name, age, hospital):
            super().__init__(name, age)
            self.hospital = hospital
            
      def displayDoctor(self): # this method will display name, age, and hospital of an object created by this class
            return f"The name is {self.name} and age is {self.age}. The hospital is {self.hospital}."