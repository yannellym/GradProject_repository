def main():
    # problem 1
    A1, n1 = [12,  23,  37,  45,  63,  82,  47,  75,  91,  88,  102], 11           # 60.45454545454545 -> rounded to nearest whole num = 60
    A2, n2 = [-1.7,  6.5,  8.2,  0.0,  4.7,  6.3,  9.5,  12.2,  37.9,  53.2], 10   # 13.68 -> rounded to nearest whole num = 
    # print(mean(A1, n1))
    # print(mean(A2, n2))
    
    # problem 2
    A = [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18] 
    k1, k2 , k3, k4 = 87, 48, 33, 10
    start, end = 0, len(A)-1
    # print("problem 2")
    # print(binarySearch(A, start, end, k1))        # => [100, 87]
    # print(binarySearch(A, start, end, k2))        # => [48]
    # print(binarySearch(A, start, end, k3))        # =>  None
    # print(binarySearch(A, start, end, k4))        # =>  None
    
    # problem 3
    l1, l2 = 2468, 1357              
    m1, m2 = 111, 378                
    n1, n2 = 123456789, 987654321 
    # print(GDC(30, 70))       # -> 10
    # print(GDC(60, 24))       # -> 12
    # print("problem 3")
    # print(GDC(l1, l2))       # -> 1
    # print(GDC(m1, m2))       # -> 3
    # print(GDC(n1, n2))       # -> 9


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
    if n == 1:         # if the length of the array is 1
        return A[n-1]  # just return the only digit in the array
    else:
        # else, return the result of n/1 times the result of calling the function again with n-1
        # then add this result to 1/n times n-1
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

    if start > end: # if the search key is not in the array, return None
        return None
    else:
        mid = (start + end) // 2  # add the start plus the end and divide it by 2. Then, round it down in case of a float value
        print(A[start:mid+1]) # print out all the subscripts in the array that were examined during the search
        if A[mid] == k:
            return (A[start:mid+1])  # subscript of the one “middle” element that is compared to the searchkey
        elif k > A[mid]:
            return binarySearch(A, start, mid - 1 , k)  # call the function again but make the end equal to mid - 1 so we shorten the sub-array we are searching in 
        else:
            return binarySearch(A,mid + 1, end,  k)    # call the function again but make the start equal to mid + 1 so we shorten the sub-array we are searching in 

    
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
'''
Input: n, m (two digits type INT)
Output: GCD of the digits after n calls
'''  
def GDC(m,n):
    print(f"integers being passed: {m}, {n}")
    if n ==0:    # if n is 0, just return m 
        return m
    else:
        return GDC(n, m % n)   # m % n produces the remainder after dividing by n 
        

main()