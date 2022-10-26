from classes import Node, LinkedList

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
    # references the linked list
    L = LinkedList()
    # sets and connects the nodes in the linked list
    L.setList(store)
    # asks users to input a number and sets this as the target
    target = int(input("please input number to check in the linked list: \n"))
    # removes or inserts the target node in the linked list
    L.removeOrInsert(target)
    

# Helper functions for main11
def lookThroughFile(store): 
    # reads a list of Integer numbers from a file named data.txt
    with open('algosAndDSA/module1/assignment2/data.txt', 'r') as f:
        # for each line in  data.txt, append it to the store list as an integer without any trailing spaces
        for line in f:
            store.append(int(line.strip()))
        # sort the store list
        store.sort()

main()

#   prev = None
#     current = l_list.head
#     while current:
#         if current.data == target:
#             prev.next = current.next
#             print("Node was removed from the list")
#             break
#         prev = current
#         current = current.next
#     for node in l_list:
#         print(node.data)  
        
#     current = l_list.head
    
#     # handles the edge case where the target node would be the first node
#     if current is None or current.data >= target:
#         newNode = Node(target)
#         newNode.next = l_list.head
#         head = newNode
#         return head
    
#     while current.next and current.next.data < target:
#         current = current.next
#     newNode = Node(target)
#     newNode.next = current.next
#     current.next = newNode
#     print("New node was added to the list")
#     for node in l_list:
#         print(node.data)