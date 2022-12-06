def main():
    A1, n1 = [12,  23,  37,  45,  63,  82,  47,  75,  91,  88,  102], 11    # 60.45454545454545 -> rounded 2 decimal points = 60.46
    A2, n2 = [-1.7,  6.5,  8.2,  0.0,  4.7,  6.3,  9.5,  12.2,  37.9,  53.2], 10
    
    
    
# 1) A “decrease-by-a constant amount” algorithm - Mean of an array  
    # Your function should have two parameters – the array of numbers and an integer indicating how 
    # many of the array values should be included in the calculations (note this is not the subscript of 
    # the last element of the array) – and should return the calculated value of the mean using a return 
    # statement.     
    
    def mean(A, n):
        if n == 1:
            return A[n-1]
        else:
            return  ((mean(A, n-1) * (n-1) + A[n-1])  / n)
        
    
    print(mean(A1, n1))
    
    
    
    
    
    
    
    
    
    
main()