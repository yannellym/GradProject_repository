from classes import Stack, Person
'''
Create a program that reads a list of people (use the class Person seem in class) from a file named people.csv (create your own file with about 15 fictional people).
Store those people in a stack (use any stack implementation you want among the ones presented in class). Ask repeatedly the user integer numbers from 1 to 4, and according to the user informed number pop this amount of people, printing the name of the one remaining in the top of the stack. For example, if the user enters 2, removes two people from the stack and print the "third" remaining in the stack
The program stops as the stack becomes empty.
'''

def main():
    store = Stack()
    fileName = input("Enter the file name with people info: ")
    everyone = readPeople(fileName)
    printPeople(everyone)
    # looks through file and adds contents to store
    lookThroughFile(everyone, store)
    store.takeAction()
        
# Helper functions for main
def lookThroughFile(everyone, store): 
    '''
    looks through the everyone object and obtains its keys values. 
    Then, append it to the store that will now be a our stack.
    Prints the stack
    
    parameters: 
    everyone: object. An object containing People
    store: stack. An instanc of the stack class.
    '''
    for name in everyone.keys():
        store.list.append(name)
    print("adding file contents to the stack...")
    print(f"New stack: {store.list}")

    
def readPeople(fileName):
    '''
    Looks through the file given, reads it, and return the people's information
    
    Parameters:
    fileName: string. Name of file given by the user
    
    returns: an object containing the peopple's information
    '''
    infile = open(fileName, "r")
    people = {}
    for line in infile:
        info = line.split(",")
        people.update({info[0]:Person(info[1], info[2], int(info[3]))})
    return people

def printPeople(people):
    '''Prints the nickname and names of the people coming from the file'''
    print("==========================")
    print(" Nickname  Name           ")
    print("==========================")
    for k in people.keys():
        print("{0:>9}  {1:<15}".format(k,people[k].getFullName()))

    
main()