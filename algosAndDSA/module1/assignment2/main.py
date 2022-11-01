from classes import LinkedList

'''
Create a program that reads a list of Integer numbers from a file named data.txt (create your own file with about 16 numbers - no repetitions and one number per line)
Store those numbers into an array a and sort it - a.sort()
Use the linked list and node classes seen in class to store the ordered elements of a into a LinkedList structure L
Ask the user a Integer value x
Look for the position to insert x in L
If the value x is already in L, remove it
If it is not, insert x in the appropriated position so L remains sorted
Go to IDLE and try to program it
Save your program in a .py file and submit 
'''
                                         
def main():
    # list to store contents of data.txt
    store = []
    # looks through file and adds contents to store
    lookThroughFile(store)
    # Makes sure that the last entry in the store is None
    store.append(None)
    
    # references the linked list class
    print("Creating link list...")
    L = LinkedList()
    
    # sets and connects the nodes in the linked list
    print("Adding array elements to list...")
    for i in range(len(store)-1):
        L.insertNode(store, i)
        
    # prints out a visual of the linked list L
    print(L.visualizeList())
        
    # asks users to input a number and sets this as the target
    target = input("please input number to check in the linked list: \n")
    
    # prompts the user to enter a numeric value if the target is a word or a decimal
    if not target.isdigit():
       target = input("please input a numeric character to check in the linked list: \n")
    # removes or inserts the target node in the linked list
    print(L.removeOrInsert(int(target)))
    

# Helper functions for main
def lookThroughFile(store): 
    # reads a list of Integer numbers from a file named data.txt
    with open('algosAndDSA/module1/assignment2/data.txt', 'r') as f:
        # for each line in  data.txt, append it to the store list as an integer without any trailing spaces
        for line in f:
            store.append(int(line.strip()))
        print("adding file contents to the array...")
        # sort the store list
        print("sorting array...")
        store.sort()
        
main()