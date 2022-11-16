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
    arr_store = [[20, 21, 25, 28, 33, 34, 35, 36, 41, 42],[18, 54, 76, 81, 36, 48, 99]]
    nums = [7, 9]
    for i in range(len(arr_store)):
        print(divisible_by(arr_store[i], nums[i]))


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

main()


