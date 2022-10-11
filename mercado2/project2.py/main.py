#1.2.11
#compose a program that in a function, asks for two positive integers and returns True if either evenly divides the other. 
# The function should keep asking for entries if the wrong ones are entered. The result (boolean) should be displayed in the calling function.
# 
'''
    File name: project_02.py
    Author: Yannelly Mercado
    Date created: 9/05/2022
    Date last modified: 9/05/2022
    Python Version: 2.7.18
'''

print("Welcome, let's figure out if, with two positive integers, either integer evenly divides the other. ") 

def ask():
    num_one = int(input("Please type the first number: "))
    num_two = int(input("Please type the second number: "))
    
    if num_one <1 or num_two <1:
        print("Please ONLY input positive integers.")
        ask()
    evenly_divides(num_one, num_two) #calls the func to check if the numbers are evenly divisible.

def evenly_divides(num_one, num_two):
    if num_one % num_two == 0 or num_two % num_one == 0: # if they're evenly divisible by each other. We use the modulo operator.
      print("True")
      ask_again = input("Do you want to check new numbers? type 'y' for yes or 'n' for no: ").lower()  # Included in case the user wants to use the function again to check for new numbers.
      if ask_again == 'y': #if yes, run function again
        ask()
      else: # if no, thank the user and dont run the while loop again
        print("Thank you for using this tool. Goodbye!")
    else: 
      print(f"{num_one} and {num_two} do not evenly divide each other. Try again.")
      ask() # if numbers don't divided each other evenly, the user will be prompted to try again.

ask()