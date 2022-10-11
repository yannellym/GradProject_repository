class Rectangle: # Parent class 
      def __init__(self, length, width):
            self.length = length
            self.width = width
      
      def perimeter(self): # perimeter = 2 * (L* /W)
            perim =  2 * (self.length + self.width)
            return perim
      
      def area(self): # area =  L * W
            calc_area = self.length * self.width
            return calc_area
      
      def display(self): # this method will dispaly the L, W, perimeter, and area of the object.
            return f"The length is {self.length}, the width is {self.width}, the perimeter is {self.perimeter()}, and the area is {self.area()}."
            
class Parallelepiped(Rectangle): # Child class inherits the parent rectangle class. 
      def __init__(self, length, width, height):
            super().__init__(length, width)
            self.height = height
            
      def volume(self):   # volume = H * W * L
            return self.height * self.width * self.length
            