class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def setList(self, store):
        '''Looks through each item in the store and assigns it to a node in the linked list.'''
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
        
        '''assigns first node to the head of the list.'''
        self.head = first_node
        
        '''assigns rest of the nodes to connect to each other.'''
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
        
    def visualizeList(self):
        '''Prints out the current list of nodes to help visualize it.'''
        node = self.head
        nodes = ""
        while node is not None:
            nodes += str(node.data)
            nodes += '->'
            node = node.next
        nodes+= "None"
        print(nodes)
    
    def replaceHead(self, current):
        '''Replaces the head of the list if the head equals the target.'''
        next = current.next
        current.next = None
        self.head = next
        return self.head

    def addNode(self, current):
        '''Adds a new node to the list.'''
        current = current.next
                
    def removeNode(self, current):
        '''Remove the node if it is already in the list.'''
        current.next = current.next.next
        print("Node was removed from the list")
      
    
    def removeOrInsert(self, target):
        '''Removes the node if it is already in the list or add it if it is not in the list.'''
        current = self.head
        
        # handles the edge case where the target node would be the first node
        if current is None or current.data == target:
            self.replaceHead(current) 
            print("** Replaced head **")
            self.visualizeList()
            return 
        # handles the edge case where the target node is less than the first node
        if target < current.data:
            self.head = Node(target)
            self.head.next = current
            current = current.next
            print("** Replaced head **")
            self.visualizeList()
            return
        
        while current:       
            if current.next:
                # if the next node is less than the target node, 
                # make the current node equal the next node
                while current.next.data < target:
                    current = current.next
                    
                # if the current node equals the target node, remove it
                print("values", current.next.data, target)   
                if current.next.data == target: 
                    current.next = current.next.next
                    self.removeNode(current)
                    # print the current linked list
                    self.visualizeList()
                    return
                # add a new node with the target value,
                # make the new node's next equal to the current's next
                # make the current's next equal to the new node 
                # print and visual the linked list
                newNode = Node(target)
                newNode.next = current.next
                current.next = newNode
                print("New node was added to the list")
                self.visualizeList()
                return self.head       
            
            
    
            
        
        