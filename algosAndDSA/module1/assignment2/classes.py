class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, store, i):
        if (self.head is None): # if list is empty
            self.head = Node(store[0])
            self.current = self.head
        else:                     # if list not empty
            self.current.next = Node(store[i])
            self.current = self.current.next
        
    def visualizeList(self):
        '''Prints out the current list of nodes to help visualize it.'''
        node = self.head
        nodes = ""
        while node is not None:
            nodes += str(node.data)
            nodes += '->'
            node = node.next
        nodes+= "None"
        return nodes
    
    def replaceHead(self, current):
        '''Replaces the head of the list if the head equals the target.'''
        next = current.next
        current.next = None
        self.head = next
        return self.head
    
    def replaceTail(self, current, target):
        '''Replaces the tail of the list if the target is less than the tail'''
        current.next = Node(target)
        current.next.next = None
        print("New node was added to the list")
        return self.visualizeList()

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
            return self.visualizeList()
        # handles the edge case where the target node is less than the first node
        if target < current.data:
            self.head = Node(target)
            self.head.next = current
            current = current.next
            print("** Replaced head **")
            return self.visualizeList()
       
        while current.next: 
            # if the next node is less than the target node, 
            # make the current node equal the next node
            while current.next.data < target:
                current = current.next
                if current.next is None:
                    current.next = Node(target)
                    current.next.next = None
                    print("New node was added to the list")
                    return self.visualizeList()
                    
                
            # if the current node equals the target node, remove it
            #print("values", current.next.data, target)   
            if current.next.data == target: 
                self.removeNode(current)
                # print the current linked list
                return self.visualizeList()
            # add a new node with the target value,
            # make the new node's next equal to the current's next
            # make the current's next equal to the new node 
            # print and visual the linked list
            newNode = Node(target)
            newNode.next = current.next
            current.next = newNode
            print("New node was added to the list")
            return self.visualizeList()
            
            