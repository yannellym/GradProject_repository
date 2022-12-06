import math
def main():
    A1, n1 = [12,  23,  37,  45,  63,  82,  47,  75,  91,  88,  102], 11           # 60.45454545454545 -> rounded to nearest whole num = 60
    A2, n2 = [-1.7,  6.5,  8.2,  0.0,  4.7,  6.3,  9.5,  12.2,  37.9,  53.2], 10   # 13.68 -> rounded to nearest whole num = 14
    # print(mean(A1, n1))
    # print(mean(A2, n2))
    
    A = [2, 5, 9, 12, 17, 23, 27, 31, 36, 39, 44]          # [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18]
    k1, k2 , k3, k4 = 12, 48, 33, 10
    start, end = 0, len(A)-1
    
    binarySearch(A, start, end, k1)
    





# 1) A “decrease-by-a constant amount” algorithm - Mean of an array  
# Your function should have two parameters – the array of numbers and an integer indicating how 
# many of the array values should be included in the calculations (note this is not the subscript of 
# the last element of the array) – and should return the calculated value of the mean using a return 
# statement.     
'''
Input: A(array of numbers), n(integer indicating how many of the array values should be included in the calculations)
Output: an Int, calculated value of the mean.
'''    
def mean(A, n):
    if n == 1:
        return A[n-1]
    else:
        # ( (mean(A, n - 1) * (n - 1) + A[n - 1]) /n)
        return  round( ((n-1)/n) * mean(A, n-1)  + (1/n) * A[n-1])


# 2) A “decrease-by-a constant factor” algorithm – Binary search
# a) Write a recursive algorithm to determine the location in a sorted array where a specified 
# searchkey is found. Unlike the algorithm in the class notes, this algorithm works with an array 
# that is sorted into DESCENDING order and the code should print out all the subscripts in the 
# array that were examined during the search. The sequence of elements that are examined is 
# known as the “probe sequence”. Do not print out the “active” portion of the array, just the 
# subscript of the one “middle” element that is compared to the searchkey. 
'''
Input: A(array of numbers), start(start > 0), end(end > start), k (key to search for)
Output: index i such that A[i] = k or none if no match is found
'''        
def binarySearch(A, start, end, k):

    if start > end: 
        return None
    else:
        mid = (start + end) // 2
        print(mid)
        if A[mid] == k:
            print(mid)
            return mid
        elif k > A[mid]:
            return binarySearch(A, mid + 1 , end, k)
        else:
            return binarySearch(A, start, mid - 1, k)

    
# 3) A “decrease-by-a variable amount” algorithm - Euclidean Algorithm for Greatest 
# Common Divisor (GCD) 
# Your function should have two parameters – the two integer whose GCD is being determined – 
# and should return the calculated value of the GCD using a return statement.  
 
# Before each recursive call, have your algorithm print out the two integers being passed as 
# parameters, make the call to find their GCD, and print out the result of the call. 
 
# b) Run your code on the problem instances:  
# i) GCD (2468, 1357) 
# ii) GCD (111, 378) 
# iii) GCD (123456789, 987654321)  

main()