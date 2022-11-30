def main():
    # 1) a) Write python code for a recursive algorithm that will calculate the number of digits in the 
    # binary expansion/representation of a positive integer n. The logic of the recursive algorithm 
    # should be something like:
    # if n = 1, the answer is 1; 
    # if n > 1, the answer is 1 more than the number of digits in the binary representation of 
    # n/2.  
    # You might want to use the python function math.floor() in your code. 
    # Your function should have only one input parameter – a positive integer n. It should return the 
    # number of digits using a return statement. There should be no print statements in the function. 
    # Note: Your function is determining the number of digits in the binary expansion of n. It is not 
    # creating the binary expansion of n. 
    # Be sure to include comments identifying the input and output for this algorithm, as well as 
    # comments explaining what is accomplished by the key steps of the algorithm.   
    def getbinary(number):
        '''
        Function: calculates the number of digits in the binary expansion/representation of a positive integer n.
        Input: A positive integer number.
        Output: A digit representing the number of digits in the binary expansion of n.
        '''
        # Base case for the function
        if number == 0:   # if the number is 0, returns 0
            return 0
        # Recursive call
        # this will add 1 everytime the function is called
        # it serves as a counter for the function
        return getbinary(number // 2) + 1  
    
    # 2) a) Write python code for a recursive algorithm that will calculate the sum of the squares of the
    # positive integers 12 + 22 + 32 + ... + 𝑛𝑛2 when supplied with a positive integer n.
    # The logic of the recursive algorithm should be something like: 
    # if n = 1, the answer is 1; 
    # if n > 1, the answer is (the sum of the squares of the integers from 1 to n-1) + 𝑛𝑛2.  
    # Do not find a closed form formula for the summation; make your algorithm do all the arithmetic. 
    # Your function should have only one input parameter – a positive integer n. It should return the 
    # sum of the sqaures using a return statement. There should be no print statements in the function. 
   
    def getSum_squares(digit):
        '''
        Function: calculates the sum of the squares of the positive integers 12 + 22 + 32 + ... + 𝑛𝑛2 when supplied with a positive integer n.
        Input: A positive integer number.
        Output: A number representing the sum of the squares of the positive integers
        '''
        # Base case for the function
        if digit == 0:   # if the number is 0, returns 0
            return 0
        # this goes through each time and does the following:
        # f(x) = 1^2 + 2^2 + 3^2 + 4^2 + 5^2  ... (n-1)^2 + n^2
        # f(n) = f(n-1) + n^2
        return getSum_squares(digit - 1) + digit * digit
   
    # functions to be executed
    
    # 1) b) 
        # decimal 1 = 1
        # decimal = 131 binary = 10000011
        # decimal = 206 binary = 11001110
        # decimal = 192 binary = 11000000
        # Example 1:
            # decimal = 203 binary = 11001011
            # if n > 1, the answer is 1 more than the number of digits in the binary representation of n/2. 
            # - > 206 /2 = 103
            # decimal = 103 binary  = 1100111
            # 11001011 len = 8  and 1100111 len = 7
        # Example 2:
            # decimal = 341 binary = 101010101
            # if n > 1, the answer is 1 more than the number of digits in the binary representation of n/2. 
            # - > 341 // 2 = 170
            # decimal = 170 binary  = 10101010
            # 101010101 len = 9  and 10101010 len = 8
        # Example 3:
            # decimal = 75 binary = 1001011
            # if n > 1, the answer is 1 more than the number of digits in the binary representation of n/2. 
            # - > 75 // 2 = 37
            # decimal = 37 binary  = 100101
            # 1001011 len = 7  and 100101 len = 6          
    # decimal_number = 75
    # print(getbinary(decimal_number))
    # decimal_number = 32
    # print(getbinary(decimal_number))
    
    # 1) c) 
    # T(n) = 1 + T(n / 2) + 1              n = 6
    #      = 1 + [1 + T(n / 2)] + 1        count = 1
    #      = 2 + [1 + T(n / 4)] + 1        count = 2
    #      = 3 + [1 + T(n / 6)] + 1        count = 3
    #      = k + T(n / 2) + 1
    #      = n + T(0)
    #      = n + O
    #      O(n)
    
    # 1) d)
    # T(n) = 1 + T(n / 2) + 1     n = 4
    # T(n) = 1 + T(n / 2) + n^0
    # a =  1, b = 3 , d = 0
    # 1 = 3^0 = 1
    # case 2: a = b^d  then T(n) = 0(n^d * lg(n))
    # Big Oh ->  O(n^d * lg(n))
    
    # 2) b) 
    # Example 1:
      # n = 5
      # 1^2 + 2^2 + 3^2 + 4^2 + 5^2  = 55
    # Example 2:
      # n = 10
      # 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 + 9^2 + 10^2 = 385
    n = 1
    print(getSum_squares(n))
    n = 10
    print(getSum_squares(n))
    
    # 2) c)
    # T(n) = 2 + T(n - 1) + n * n      
    #      
    
    # 2) d) 
    # back substitution method 
    # T(n) = 2 + T(n - 1) + n * n 
    #      = 2[1 (n-1)] + T(n-2)]   
    #      = 2[1 (n-1) + [T(n-2) +  (n-3)]  
    #      = 2[1 (n-1) + (n-2) + (n-3)
    #      = 2 * n(n +1) / 2
    #      =  O(n)^2

main()