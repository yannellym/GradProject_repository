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

# list to store contents of data.txt
store = []
    
# reads a list of Integer numbers from a file named data.txt
with open('algosAndDSA/module1/assignment2/data.txt', 'r') as f:
    # for each line in  data.txt, append it to the store list as an integer without any trailing spaces
    for line in f:
        store.append(int(line.strip()))
    # sort the store list
    store.sort()


class LinkedList:
    def __init__(self):
        self.head = None
    
    def visualize(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        print(" -> ".join(nodes))
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None             
        
        
def main():
   
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

    l_list = LinkedList()

    l_list.head = first_node
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
            
    # for node in l_list:
    #     print(node.data)

    target = int(input("please input num "))
    
    
    # remove node if already in linked list
    prev = None
    current = l_list.head
    while current:
        if current.data == target:
            prev.next = current.next
            break
        prev = current
        current = current.next
        
    for node in l_list:
        print(node.data)
    
    target2 = int(input("please input num ")) 
    current = l_list.head
    if current is None or current.data >= target2:
        newNode = Node(target2)
        newNode.next = l_list.head
        head = newNode
        return head
 
    # Locate the node before the poof insertion
   
    while current.next and current.next.data < target2:
        current = current.next
    newNode = Node(target2)
    newNode.next = current.next
    current.next = newNode
    for node in l_list:
        print(node.data)

main()