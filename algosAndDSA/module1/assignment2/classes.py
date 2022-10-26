class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

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
        # iterates through the list as long as the node is not None
        node = self.head
        while node is not None:
            # yield is used to produce a sequence of values, unliked return
            # return only returns a specified value
            yield node
            node = node.next 