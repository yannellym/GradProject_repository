class Stack:
    def __init__(self):
        # list to list contents of people.csv
        self.list = []
     
    def popItem(self, chosen_num):
        '''Will receive an amount of users to pop from the list
        Parameters:
        - number_chosen: INT number of users to pop from the list
        Return:
        False: if the stack is empty, returns false
        True: if the stack is not empty, returns True
        '''
        if chosen_num > len(self.list):
            print(f"Current stack length is {len(self.list)}. Please choose a different number to remove")
            
        elif chosen_num == len(self.list):
            self.list = []
            print(f"Stack is now empty: {self.list}, length is {len(self.list)}")
            # returns false in order to quit the program
            return False
        else: 
            if chosen_num < len(self.list):
                for i in range(chosen_num):
                    self.list.pop()
            print(f"New stack is: {self.list} ")
        return True
                    
    def askUser(self):
        '''
        Ask the user for to enter a number between 1 and 4. If The user doesn't enter an 
        integer, or the integer is not between 1-4, keep asking the user for a valid input
        Return:
        - The number inputted by the user as an INT
        '''
        number_chosen = input("Please choose a number between 1 and 4: \n")
        # if it is not an instance of INT, ask user again for a number.
        if not number_chosen.isdigit():
            print("Number must be an integer")
            self.takeAction()
            
        elif int(number_chosen) > 4 or int(number_chosen) < 1:
            print("Number must be between 1 and 4.")
            self.takeAction()
        return int(number_chosen)
    
    def takeAction(self):
        '''asks user for a number and sets it in a variable called chosen_number'''
        chosen_num = self.askUser()
        continue_pop = self.popItem(chosen_num)
        # while continue_pop is true (this means the stack is not empty and the user wants to pop more items)
        # continue asking the user for a number and popping from the stack
        # once continue_pop is set to false or null, the program will quit
        if continue_pop:
            continue_pop = self.takeAction()

class Person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age  = age
    def getName(self):
        return self.name
    def getFullName(self):
        return self.name+" "+self.famN
    def getFamilyName(self):
        return self.famN
    def getAge(self):
        return self.age
    
    def __str__(self):
        print(self.__dict__)


