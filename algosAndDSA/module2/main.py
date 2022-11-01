from classes import Stack
'''
Create a program that reads a list of people (use the class Person seem in class) from a file named people.csv (create your own file with about 15 fictional people).
Store those people in a stack (use any stack implementation you want among the ones presented in class). Ask repeatedly the user integer numbers from 1 to 4, and according to the user informed number pop this amount of people, printing the name of the one remaining in the top of the stack. For example, if the user enters 2, removes two people from the stack and print the "third" remaining in the stack
The program stops as the stack becomes empty.
'''

def main():
    store = Stack()
    # looks through file and adds contents to store
    lookThroughFile(store.list)
    store.takeAction()
        

# Helper functions for main
def lookThroughFile(store): 
    # reads a list of Integer numbers from a file named people.csv
    with open('algosAndDSA/module2/people.csv', 'r') as f:
        # for each line in  people.csv, append it to the store list without any trailing spaces
        for line in f:
            store.append(line.strip())
        print("adding file contents to the stack...")
    print(store)

    
main()