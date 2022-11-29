import math

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
        # Base case for the function
        if number == 0:
            return 0
        # Recursive call
        # bin_num is where we will save the results
        bin_num = getbinary(number // 2)
        
        final = (number % 2 + 10 * bin_num)
        print(len(str(final)))
        return final
        # return len(str(final))
   
    # functions to be executed
    
    # problem 1
        # decimal 1 = 1
        # decimal = 131 binary = 10000011
        # decimal = 206 binary = 11001110
        # decimal = 192 binary = 11000000
    decimal_number = 203
    print(getbinary(decimal_number))

main()