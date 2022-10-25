class Deque:
      # constructor. Will receive the user_input and save this as the line
      def __init__(self, user_input):
            self.items = user_input
      
      # will return an f string displaying the current status of the line   
      def display(self):
            return self.items
      
      # will add a new person to the back of the line
      # will return the status of the line
      def addToBack(self, item):
            self.items.append(item)
            return self.items
      
      # will add a new person to the front of the line
      # will return the status of the line
      def addToFront(self, item):
            self.items.insert(0, item)
            return self.items
            

