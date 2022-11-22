def main():
    # selectionSort([63, 44, 17, 77, 20, 6, 99, 84, 52, 39])
    # selectionSort([84, 52, 39, 6, 20, 17, 77, 99, 63, 44])
    # selectionSort([99, 84, 77, 63, 52, 44, 39, 20, 17, 6])
    # bubbleSort([44, 63, 77, 17, 20, 99, 84, 6, 39, 52])
    # bubbleSort([52, 84, 6, 39, 20, 77, 17, 99, 44, 63])
    # bubbleSort([6, 17, 20, 39, 44, 52, 63, 77, 84, 99])
    #power(9,3)
    evaluate("12.3 + 40.7𝑥 − 9.1𝑥2 + 7.7𝑥3 + 6.4𝑥4 + 8.9𝑥6", 5.4)
    pass






# Helper functions for main

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

def Swap(A, i, j): 
    temp = A[i] 
    A[i] = A[j] 
    A[j] = temp 
    # after each iteration, print the array
    # K largest elements will be placed into the last k slots of the array
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
 
   
# 2) a) Write Python code for the bubble sort algorithm to sort an array into descending order by 
# making the smallest elements “bubble up” and end up in the last entries of the array. Modify the 
# code in the class notes (using the same parameters and return) to do four things:
    # i) After k iterations through the outer loop, the k SMALLEST elements should be sorted 
    # and placed at the end of the array rather than the k LARGEST elements.
    # ii) After each iteration through the outer loop, print the array. After the kth iteration, 
    # you should see that the k smallest elements have been placed into the last k slots of the 
    # array.
    # iii-iv) Throughout the run, count the number of times two array elements are compared 
    # and the number of times two elements are swapped. When the algorithm concludes, use a 
    # print statement to display the total number of comparisons of array elements and the total 
    # number of swaps required to sort the array.
    
# b) Check your algorithm on the problem instances:
# A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52] 
# A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63] 
# A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99] 

def bubbleSort(A):
    comparisons = 0 # number of comparisons in the array
    swaps = 0  # num of swaps in the array
    print(f"Initial array: {A}")
    for i in range(len(A)-1, -1, -1):
        comparisons += 1
        for j in range(len(A)-2, -1, -1): # after k iterations, the k smallest element will be sorted at end of array.
            if A[j+1] > A[j]:
                swaps += 1
                Swap(A, j  , j+1)
    print(f"Number of comparisons: {comparisons}, number of swaps: {swaps} ")
  
    
# 3) Write a Python function (with two input parameters)
# evaluate (A, x)  
# that determines the value of f(x) for the polynomial that is represented by the corresponding 
# array A of coefficients. Return the resulting value using a return statement. 
# For each term of the polynomial, this function should make a call to the power() function that 
# you wrote in part 3a.  
# c) Run your code to evaluate the polynomial
# 𝑓𝑓(𝑥𝑥) = 12.3 + 40.7𝑥𝑥 − 9.1𝑥𝑥2 + 7.7𝑥𝑥3 + 6.4𝑥𝑥4 + 8.9𝑥𝑥6   at x = 5.4
# Use a driver/main program to initialize the corresponding array and call the function in a print.



def power(x,p):
    res = 1
    for i in range(p):
        res *= x
    print(abs(res))
        
def evaluate(A, x):
    x = str(x)
    arr = A.replace("𝑥", f"({x})")
    # arr = 12.3 + 40.7(5.4) − 9.1(5.4)2 + 7.7(5.4)3 + 6.4(5.4)4 + 8.9(5.4)6
    res = 0
    for i in range(len(arr) - 1):
        sec = ""
        expo = ""
        if arr[i] == "(":
            for j in arr[i+1:]:
                if j == ")":
                    idx = arr.index(j)
                    expo = arr[idx+1]
                    break
                sec += j
        else:
            continue
        power(float(sec), int(expo) if expo != " " else 0)
    #print(res)   #print(float(sec), int(expo) if expo != " " else 0)
            
            
    
    


main()
 
