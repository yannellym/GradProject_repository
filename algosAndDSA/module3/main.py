from classes import Tree


def main():
    tree = Tree()
    fileName = input("Please enter the file path: ")
    # object containing the information extract from the chosen file
    numbers = readNumbers(fileName)
    for digit in numbers:
        tree.insert(digit)
        
    tree.printInorder()
    tree.printPreorder()
    
    print("66 is in the tree:", tree.check(66))
    print("99 is in the tree:", tree.check(99))
    print("8 is in the tree:", tree.check(8))
    print("72 is in the tree:", tree.check(72))
    tree.printPostorder()


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
    print(nums)
    return nums
    
    
main()