'''
Create a program that reads a list of people (use the class Person seem in class) from a file named people.csv (create your own file with about 15 fictional people).
Store those people in a stack (use any stack implementation you want among the ones presented in class). Ask repeatedly the user integer numbers from 1 to 4, and according to the user informed number pop this amount of people, printing the name of the one remaining in the top of the stack. For example, if the user enters 2, removes two people from the stack and print the "third" remaining in the stack
The program stops as the stack becomes empty.
'''
# list to store contents of people.csv
store = []

def main():
    # looks through file and adds contents to store
    lookThroughFile(store)
    removeFromStack()
    print(store)
    print("Stack is now empty.")
        




# Helper functions for main
def lookThroughFile(store): 
    # reads a list of Integer numbers from a file named people.csv
    with open('algosAndDSA/module2/people.csv', 'r') as f:
        # for each line in  people.csv, append it to the store list without any trailing spaces
        for line in f:
            store.append(line.strip())
        print("adding file contents to the array...")
    print(store)

def askUser():
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
        askUser()
    elif int(number_chosen) > 4 or int(number_chosen) < 1:
        print("Number must be between 1 and 4.")
        askUser()
    else:
        return int(number_chosen)
    
def popItem(chosen_number):
    '''Will receive an amount of users to pop from the list
    Parameters:
    - number_chosen: INT number of users to pop from the list
    Return:
    
    '''
    if chosen_number > len(store):
        print(f"Current stack length is {len(store)}. Please choose a different number to remove")
        return askUser()
    
    for i in range(chosen_number):
        store.pop()
    
    if len(store) > 0:      
        print(f"New stack is: {store} ")
        return True
    print("returning false")
    return False
        
def removeFromStack():
    
    # asks user for a number and sets it in a variabled called chosen_number
    chosen_number = askUser()
    continue_pop = popItem(chosen_number)
    while continue_pop:
        removeFromStack()
        break
    
main()