from classes import Tree

def main():
    tree = Tree()
    fileName = input("Please enter the file path: ")
    # object containing the information extract from the chosen file
    numbers = readNumbers(fileName)
    for digit in numbers:
        tree.insert(digit)
    
    # calls the getArr method which will return an array containing
    # the values of the tree in a preorder manner
    tree_arr = tree.getArr()
    # create the matrix that we will be using to input the values
    matrix = tree.createMatrix()
    
    tree.extractValues(tree_arr, matrix)  
    tree.printMatrix(matrix)
     
        
# Helper functions for main
def readNumbers(fileName):
    '''
    Looks through the file given, reads it, and return the file's information
    
    Parameters:
    fileName: string. Name of file given by the user
    
    returns: an array containing all the numbers in the file
    '''
    infile = open(fileName, "r")
    nums = []
    for line in infile:
        nums.append(int(line))
    return nums
    
main()