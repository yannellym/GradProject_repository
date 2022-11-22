# 1) a) Write Python code for the selection sort algorithm to sort an array into ascending order. 
# Modify the code in the class notes (using the same parameters and return) to do three things:
    # i) After k iterations through the outer loop, the k LARGEST elements should be sorted 
    # rather than the k SMALLEST elements.
    # ii) After each iteration through the outer loop, print the array. After the kth iteration, 
    # you should see that the k largest elements have been placed into the last k slots of the 
    # array.
    # iii) Throughout the run, count the number of times two array elements are compared. Be 
    # sure to count the number of comparisons not just the number of comparisons that evaluate 
    # to True. When the algorithm concludes, use a print statement to display the total number 
    # of comparisons of array elements required to sort the array.
    
# 2) Check your algorithm on the problem instances:
# A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
# A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
# A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

def main():
    selectionSort([33,77,55,22,11,44])






# Helper functions for main

# Problem 1 functions    
def Swap(A, i, j): 
    temp = A[i] 
    A[i] = A[j] 
    A[j] = temp 
    # after each iteration, print the array
    # K largest elements will be placed into the last k slots of the array
    print(f"Iteration #{len(A) - i}: ")
    print(A) # after each iteration, print the array

# Input: An array A of integers. 
# Output: Array A sorted in increasing order.
def selectionSort(A): 
    comparisons = 0
    print(f"Initial array {A}")
    for i in range(len(A)-1, -1, -1): 
        m = i 
        for j in range(i-1, -1, -1): 
            comparisons += 1
            if A[j] > A[m]:  # after k iterations, the K largest element should be sorted
                m = j
        Swap(A, i, m) 
    print(f"Number of comparisons required to sort the array: {comparisons}")
    
        

main()
 
