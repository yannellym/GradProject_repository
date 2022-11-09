from classes import Tree


def main():
    tree = Tree()
    fileName = input("Please enter the file path: ")
    # object containing the information extract from the chosen file
    numbers = readNumbers(fileName)
    for digit in numbers:
        tree.insert(digit)
        
    #tree.printInorder()
    tree.printPreorder()
    
    #print("66 is in the tree:", tree.check(66))
    # print("99 is in the tree:", tree.check(99))
    # print("8 is in the tree:", tree.check(8))
    # print("72 is in the tree:", tree.check(72))
    # tree.printPostorder()
    tree_arr = tree.getArr()
    tree_size = len(tree_arr)
    # print(tree_arr)
            
    matrix = [[0] * tree_size for i in range(tree_size)]
    
    for i in range(tree_size - 1):
        if i == 0:
            matrix[i][i+1] = tree_arr[i] - tree_arr[i+1]
            matrix[i][tree_size - 1] = abs(tree_arr[-1] - tree_arr[i])
        else:
            matrix[i][i+1] = tree_arr[i] - tree_arr[i+1]
            matrix[i][tree_size - 1] = abs(tree_arr[-i + 0] - tree_arr[i])
                   
    for row in matrix:
        print(row)
        print('\n')
        
        
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

def adjacency_matrix(tree): 
    adj = [[0 for node in tree.data] for node in tree.data]
    for edge in tree.left:
        node1, node2 = edge[0], edge[1]
        
    
main()