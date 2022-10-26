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
    setList(L, store)
    # asks users to input a number and sets this as the target
    target = int(input("please input number to check in the linked list: \n"))
    # removes or inserts the target node in the linked list
    removeOrInsert(L, target)
    

# Helper functions for main
def lookThroughFile(store): 
    # reads a list of Integer numbers from a file named data.txt
    with open('algosAndDSA/module1/assignment2/data.txt', 'r') as f:
        # for each line in  data.txt, append it to the store list as an integer without any trailing spaces
        for line in f:
            store.append(int(line.strip()))
        # sort the store list
        store.sort()
    
def setList(l_list, store):
    # Looks through each item in the store and assigns it to a node in the linked list
    first_node = Node(store[0])
    second_node = Node(store[1])
    third_node = Node(store[2])
    fourth_node = Node(store[3])
    fifth_node = Node(store[4])
    sixth_node = Node(store[5])
    seventh_node = Node(store[6])
    eigth_node = Node(store[7])
    nineth_node = Node(store[8])
    tenth_node = Node(store[9])
    eleventh_node = Node(store[10])
    twelve_node = Node(store[11])
    thirteen_node = Node(store[12])
    fourteen_node = Node(store[13])
    fifteen_node = Node(store[14])
    sixteen_node = Node(store[15])
    # assigns first node to the head of the list
    l_list.head = first_node
    #assigns rest of the nodes to connect to each other
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node 
    fifth_node.next = sixth_node
    sixth_node.next = seventh_node 
    seventh_node.next = eigth_node
    eigth_node.next = nineth_node 
    nineth_node.next = tenth_node
    tenth_node.next = eleventh_node     
    eleventh_node.next = twelve_node
    twelve_node.next = thirteen_node 
    thirteen_node.next = fourteen_node
    fourteen_node.next = fifteen_node 
    fifteen_node.next = sixteen_node
    sixteen_node.next = None 

def removeOrInsert(l_list, target):
    # remove node if already in linked list
    prev = None
    current = l_list.head
    while current:
        if current.data == target:
            prev.next = current.next
            print("Node was removed from the list")
            break
        prev = current
        current = current.next
    for node in l_list:
        print(node.data)  
        
    current = l_list.head
    
    # handles the edge case where the target node would be the first node
    if current is None or current.data >= target:
        newNode = Node(target)
        newNode.next = l_list.head
        head = newNode
        return head
    
    while current.next and current.next.data < target:
        current = current.next
    newNode = Node(target)
    newNode.next = current.next
    current.next = newNode
    print("New node was added to the list")
    for node in l_list:
        print(node.data)

main()