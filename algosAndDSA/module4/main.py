'''Module 4: Programming Assignment
1) Find the number of entries in an array of integers that are divisible by a given integer. Your function should have two input parameters 
– an array of integers and a positive integer – and should return an integer indicating the count using a return statement.
Run your algorithm on the problem instances:
a) [20, 21, 25, 28, 33, 34, 35, 36, 41, 42] number of entries that are divisible by 7
and
b) [18, 54, 76, 81, 36, 48, 99] number of entries that are divisible by 9   

2) Given an array of real numbers, without sorting the array, find the smallest gap between all pairs of elements 
(for an array A, the absolute value of the difference between elements 𝐴𝑖 and 𝐴𝑗). Your function should have one input parameter 
– an array of numbers – and should return a non-negative number indicating the smallest gap using a return statement.
Run your algorithm on the problem instances:
a) <50, 120, 250, 100, 20, 300, 200>
b) <12.4, 45.9, 8.1, 79.8, -13.64, 5.09>

3) Given an integer n>=2 and two nxn matrices A and B of real numbers, find the product AB of the matrices.
Your function should have three input parameters – a positive integer n and two nxn matrices of numbers– 
and should return the nxn product matrix using a return statement.
'''

def main():
    # problem 1
    arr_store = [[20, 21, 25, 28, 33, 34, 35, 36, 41, 42],[18, 54, 76, 81, 36, 48, 99]]
    nums = [7, 9]
    # Runs a loop ith times. With i being the length of the arr_store.
    for i in range(len(arr_store)):
        # passes the arr in position i of the arr_store and the number in position i of nums
        # prints the return statement from the divisible_by function
        print("**Problem 1 answer:")
        print(divisible_by(arr_store[i], nums[i]))
        
    # problem 2
    num_arr = [[50, 120, 250, 100, 20, 300, 200],[12.4, 45.9, 8.1, 79.8, -13.64, 5.09]]
    # Runs a loop ith times. With i being the length of the num_arr
    for i in range(len(num_arr)):
        # passes the arr in position i of the num_arr 
        # prints the return statement from the smallest_gap function
        print("**Problem 2 answer:")
        print(smallest_gap(num_arr[i]))
        
    # problem 3
    matrix_nums = [2,3]
    matrix_1_arrs = [[[2,7],[3,5]], [[1,0,2],[3,-2,5],[6,2,-3]]]
    matrix_2_arrs = [[[8, -4], [6,6]] , [[.3, .25, .1],[.4, .8, 0],[-.5, .75, .6]]]
    
    # Runs a loop ith times. With i being the length of the matrix_nums
    for i in range(len(matrix_nums)):
        # passes the matrix in position i of the matrix_1_arrs and the the matrix in position i of the matrix_2_arrs
        # prints the matrix built by multiplying the columns and rows of the matrices
        print("**Problem 3 answer:")
        result = matrix_product(matrix_nums[i], matrix_1_arrs[i], matrix_2_arrs[i])
        for r in result:
           print(r) 
    

def divisible_by(arr, n):
    '''
    Parameters:
    - arr: an array of numbers type INT
    - n: the number the digits must be divisible by, type INT
    
    Function will look through each number in the array and figure out if it is divisible by n.
    If the number is divisible by n, it will increase the count. 
    
    Return:
    - count: the counto of how many digits are divisible by n. 
    '''
    count = 0
    for digit in arr:
        if digit % n == 0:
            count += 1
    return count   

def smallest_gap(num_arr):
    '''
    Parameters:
    - num_arr: an array of numbers type INT, and FLOAT
    
    Variables:
    i , j : INT will be used to loop through the array and compare numbers to each other.
    gap : a variable set to positive infinity. 
    
    Function will look through each number in the array and comparate the ith element with the jth element. 
    It will subtract j - i and set it to its absolute value. Then, if the value is less than the variable "gap",
    it will set gap to equal that new value.
    
    Return:
    - gap: the smallest gap  
    '''
    i = 0
    j = 1
    gap = float('inf')
    
    for j in range(1,len(num_arr)):
        gap = min(gap, abs(num_arr[j] - num_arr[i]))
        i += 1
    return gap
     
def matrix_product(n, matrix1, matrix2):
    '''
    Parameters:
    - n:
    - matrix1:
    - matrix2:
    
    Variables:
    result : will store the final matrix that is obtained by multiplying the colum and rows of matrix1 with matrix
    
    Function will look through each row in matrix 1 and multiply its numbers by each number in matrix2 column.
    Then, it will save the result in the result variable.
    At the end, it will print each row in the results variable.
    
    Return:
    - result : the variable with the final matrix that is obtained by multiplying the colum and rows of matrix1 and matrix2
    '''
    
    # gets all the rows in in matrix1 and all the columns in matrix2
    # zips together matrix1 and matrix2
    # takes each digit in matrix1 and matrix2 and multiplies them
    # rounds the multiplication result by the num of columns
    result = [[ round(sum(a*b for a,b in zip(matrix1_row, matrix2_col)), n) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
    return result    
          
          
main()


