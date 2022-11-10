class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

class Tree:
    def __init__(self, d=None):
        # if no data, root will be None
        if (d == None): 
            self.root = None
        # else, create a new node with data = d and assign it to the root
        else:
            self.root = Node(d)
            
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.data > d):   # if no node left insert here
                if (n.left == None):
                    n.left = Node(d)
                else:          # or try left child
                    __insertHere__(n.left, d)
            elif (n.data < d): # if no node right insert here
                if (n.right == None):
                    n.right = Node(d)
                else:          # or try right child
                    __insertHere__(n.right, d)
        if (self.root == None): # it was an empty tree
            self.root = Node(d)
        else:
            if (self.root.data > d):          # try left child
                if (self.root.left == None):  # if empty insert here
                    self.root.left = Node(d)
                else:                         # try left subtree
                    __insertHere__(self.root.left, d)
            elif (self.root.data < d):        # try right child
                if (self.root.right == None): # if empty insert here
                    self.root.right = Node(d)
                else:                         # try right subtree
                    __insertHere__(self.root.right, d)
    
    # def check(self, d):
    #     # checks if the value is in a node of the tree
    #     # if none, itll return False
    #     # if equal, itll return True
    #     # if the current's node data is greater than the number given
    #      # itll check the node to the left side.
    #     # if the current's node data is less than the number given
    #      # itll check the node to the right side.
    #     def __check__(n, d):
    #         if (n == None):
    #             return False
    #         elif (n.data == d):
    #             return True
    #         elif (n.data > d):
    #             return __check__(n.left, d)
    #         elif (n.data < d):
    #             return __check__(n.right, d)
    #     return __check__(self.root, d)
    
    # # visit first child, then node, then next child
    # def printInorder(self):
    #     def __visit__(n):
    #         if (n != None):
    #             __visit__(n.left)
    #             print(n.data, end=" ")
    #             __visit__(n.right)
    #     print("\n--------")
    #     __visit__(self.root)
    #     print("\n--------")
    
    # def printPreorder(self):
    #     def __visit__(n, h):
    #         if (n != None):
    #             print("---"*h, n.data)
    #             __visit__(n.left, h+1)
    #             __visit__(n.right, h+1)
    #     print("^^^^^^^^^^")
    #     __visit__(self.root, 1)
    #     print("^^^^^^^^^^")
    
    # def printPostorder(self):
    #     def __visit__(n, h):
    #         if (n != None):
    #             __visit__(n.left, h+1)
    #             __visit__(n.right, h+1)
    #             print("---"*h, n.data)
    #     print("==========")
    #     __visit__(self.root, 1)
    #     print("==========")
    
    def getArr(self):
        '''goes through the tree, preoder, and adds all values of the tree to the array.
        return this array of values'''
        arr = []
        def __visit__(n, h):
            if (n != None):
                arr.append(n.data)
                __visit__(n.left, h+1)
                __visit__(n.right, h+1)
                
        __visit__(self.root, 1)
        return arr
      
    def extractValues(self, tree_arr, matrix):
        def __visit__(n, h):
            if (n != None):
                # row of matrix to insert
                i = tree_arr.index(n.data)
                # deal with the left child 
                if n.left != None:
                    j = tree_arr.index(n.left.data)
                    matrix[i][j] = abs(n.data - n.left.data)
                # then deal with the right child
                if n.right != None:
                    k = tree_arr.index(n.right.data)
                    matrix[i][k] = abs(n.data - n.right.data)
                __visit__(n.left, h+1)
                __visit__(n.right, h+1)
        __visit__(self.root, 1)
            
    def createMatrix(self):
        '''Takes the length of the tree array and the size(level) of the tree.
        Creates a matrix that is nth wide and nth tall. Where n represents the tree height'''
        tree_arr = self.getArr()
        tree_size = len(tree_arr)
                
        matrix = [[0] * tree_size for i in range(tree_size)]
        return matrix
    
    def printMatrix(self, matrix):
        #prints matrix row by row
        for row in matrix:
            print(row)
            print('\n')