from classes import Deque

''' Project 6
    Implement Deque in Python, Deque or doubly ended queues are linear 
    data structures with which we can perform last in first out (LIFO) 
    operations as well as first in first out (FIFO) operations.

    The algorithm (10 points)
    The program prompts for and captures items to store in the dequeue. You can store anything you want, take your pick, and just explain what it is in the algorithm. (20 points)
    The program calls correct display method that displays all the contents of the dequeue. (20 points)
    The program has the capability to insert an element at the beginning of the queue (10 points)
    The program has the capability to insert an element at the end of the queue (10 points)
    The program has correct unit testing and proper pydocs documentation (20 points).
    The program has appropriate comments (10 points)
'''

'''
    File name: project_06.py
    Author: Yannelly Mercado
    Date created: 9/30/2022
    Date last modified: 9/30/2022
    Python Version: 2.7.18
'''

#executes the main functions for the program
def main():
    # calls the welcome function and saves the result in a variable called user_input. 
    # The result will be an arary of string
    user_input = welcome()
    #initiates the line object from the deque class and saves the result in a variable called line.
    # Also passes in the user_input variable which is an array of strings
    line = Deque(user_input)
    
    #print the line for the first time.
    print("Take a look at who is waiting in line:")
    print(line.display())
    
    # variable that determines if the loop should continue or break
    should_continue = "y"
    
    # while should_continue is "y", it will continue calling the whatToDo function
    while should_continue == "y":
        # calls the whatToDo function and passes in the line object we created
        whatToDo(line)
        # gets input from the user and saves it in a variable called should_continue
        should_continue = input("Do you want to continue adding people to the line? Type Y for yes, N for no: ").lower()
        
     

# Helper functions for main

# function welcomes the user and asks for inputs that will go in the "line". It will return the user's input.
def welcome():
    print("Welcome, with this program, you will be able to create a line and add people to it.\n"
           "However, you get to choose if they go in the front of the line or the back of the line!")
    print("Who is waiting in line?")
    # takes the user's input and removes the white spaces. It also splits it with a comma.
    user_input = input("Please enter their first names, separated by a comma: ").replace(" ", "").split(",")
    # will return the user's input as an array of strings
    return user_input

def whatToDo(line):
    # letters/inputs that are not accepted by the program
    not_accepted = "qwertyuiopasghjklzxcvnm"
    # a variable that will hold the user's input
    func = input("Type F to add someone to the front of the line, B to add to the back of the line, or D to display the line: ").lower()
    
    # if the user types d, it will display the current status of the line
    if func == "d":
        print(line.display())
    # if the user types a letter that is not accepted, it will call the 
    # whatodo function again to have them give a new input
    elif func in not_accepted:
        whatToDo(line)
    # else, it will ask for who they want to add to the line
    # based on the input, it will call the appropiate function
    else:
        user = input("Type the name of the person you want to add to the line: ")
        if func == "f":
            print(line.addToFront(user))
        elif func == "b":
            print(line.addToBack(user))
        else:
            print(line.display())

# calls the function main   
main()