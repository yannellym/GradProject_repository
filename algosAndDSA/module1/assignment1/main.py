"""
Part 1: Variables, Decisions, and I/O

1. Write a program that will be called "Is It Cold In Canada Today?"
2. Ask a Canadian what is the threshold for cold - Receive the threshold in C0 (input)
3. See the current temperature in Fahrenheit - Receive the today's temperature in F0 (input)
4. Making the necessary conversions, decide - Print if is it cold for a Canadian (output)

Part 2: Functions and Parameters

Create a function zigzag that gets three values as input parameters, let's call then a, b, and c

The program will return True if they are a zigzag, and False otherwise, these numbers are a
zigzag if, and only if a < b > c or a > b < c

For example:

If a = 3 b = 8 c = 5 then they are a zigzag
If a = 3 b = 8 c = 9 then they are not a zigzag
If a = 6 b = 3 c = 6 then they are a zigzag
If a = 3 b = 5 c = 5 then they are not a zigzag

Part 3: Loops

1. Create a program that swaps elements in a created vector
2. Ask the user an even integer between 9 and 21
3. Create a vector sized by this inputted integer
4. [0, 1, 2, ... ]
5. Swap the first with the second element,
6. Swap the third with the fourth, ... and so on
7. Prints out the resulting vector
"""
 
def main():   
    print("Program 1:")
    coldInCanada()

    print("Program 2: Inputs 3,5,5")
    zigzag(a = 3, b = 5, c = 5)

    print("Program 3:")
    swappingInVector()
    
# Helper functions for main
# Part 1 function    
def coldInCanada():
    '''
    Variables:
        celsius_threshold: will ask the user for an input that must be in celsius. Then it will evaluate that answer to figure out the data type of the input.
        current_f_temp: variable set to the current temperature. 
        cels_to_faren: takes the celsius_threshold variable and multiplies it by the result of 9/5. Then adds the previous to 32. This will represent the celcius
        temperate in Farenheit.
    '''
    celsius_threshold = input("What is the threshold for cold? Please input the temperature in celsius: \n")
    current_f_temp = input("What is the current temperature? (in Farenheit) \n")
    
    ''' 
    if the celsius_threshold is not of type float, call the ColdInCanada function again to let the user input a new temperature.
    Else, multiply the user temp  by the result of 9/5. Then add this result to 32. The answer will be the celsius temp converted to farenheit.
    If the current temperature is less than the cold threshold, print "it is cold for a Canadian". Else, print "it is not cold for a Canadian".
    '''
    try:
        user_temp = float(celsius_threshold)
        current_f_temp = float(current_f_temp) 
    except ValueError:
        print("Please only type numeric characters.")
        coldInCanada()
    else:
        cels_to_faren = (user_temp * 9/5) + 32
        print(f"Current Temperature: {current_f_temp} degrees farenheit")
        print(f"Canadian Threshold: {cels_to_faren} degrees farenheit")
        if float(current_f_temp) < float(cels_to_faren): 
            print("It is cold right now for a Canadian.")
        else:
            print("It is not cold right now for a Canadian.")
            
# Part 2 function    
def zigzag(a,b,c):
    '''
    Parameters:
        a: Type INT
        b: Type INT
        c: Type INT
    
    if a is less than b and b is greater than c or a is greater than b and b is less than c,
    return True. Else, return False
    '''
    if a < b > c or a > b < c:
        print("True")
        return True
    else:
        print("False")
        return False
    
# Part 3 function    
def swappingInVector():
    '''
    if a is less than b and b is greater than c or a is greater than b and b is less than c,
    return True. Else, return False
    '''
    valid_ints = [10, 12, 14, 16, 18, 20]
    user_res = input("Please input an even integer between 9 and 21: \n")
    
    '''
    if the user's input is not of type int, it will raise an error, print a message, and call the swappingInVector() func again.
    if the user's input is of type int, create a vector. Append the numbers from 0 to the even integer the user inputted.
    For the length of the vector (minus 1 so it doesn't go out of bounds), swap the ith number in the vector with the ith number + 1.
    Do this for every 2nd element of the vector.
    Last, print the updatee vector.
    '''
    try:
        even_int = int(user_res)
    except ValueError:
        print("**Input must be numeric**")
        swappingInVector()
    else:
        if even_int in valid_ints:
            vector = []
            for i in range(even_int):
                vector.append(i)
            
            for i in range(0, len(vector) - 1, 2):
                vector[i], vector[i + 1] =  vector[i + 1], vector[i]
            print(vector)
        else:
            print("**Input must be an even integer between 9 and 21**")
            swappingInVector() 

main()