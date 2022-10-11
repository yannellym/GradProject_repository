'''
    File name: project_01.py
    Author: Yannelly Mercado
    Date created: 9/02/2022
    Date last modified: 9/02/2022
    Python Version: 2.7.18
'''

pie_num = 3.14159 # set this as a variable as it will be used continuously throughout the program.

def calc_circum(user_answer, pie_num): 
    circum = round(2 *(pie_num * user_answer), 5)  # multiply pie by the user's answer. Then multiply this result by two.Lastly, round to 5 decimal places.
    print(f"The circumference of a circle with a radius of {user_answer} is {circum}") 
    print("\n" * 2) # add 2 spaces below the answer.
    
def calc_area(user_answer, pie_num): 
    area = round(pie_num * (user_answer ** 2),5) # user's answer to the power of 2. Then multiply this result by pie. Lastly, round to 5 decimal places.
    print(f"The area of a circle with a radius of {user_answer} is {area}") 
    print("\n" * 2)  # add 2 spaces below the answer.

def calc_sph_volume(user_answer, pie_num): 
    volume = round(4/3 * (pie_num *(user_answer ** 3)), 5) # take the user's answer and raise it to the 3rd power. Multiple this result by pie. Then multiply this result by 4/3. Lastly, round to 5 decimal places.
    print(f"The volume of a sphere with a radius of {user_answer} is {volume}")
    print("\n" * 2)    # add 2 spaces below the answer.
    
    
user_answer = float(input("Please enter a radius of a circle/sphere: \n")) # Ask the user for the radius of a circle/sphere. Save the answer in a variable
calc_circum(user_answer, pie_num) # call the calc_circum function and pass in the user's answer and pie_num variable.
calc_area(user_answer, pie_num) # call the calc_area function and pass in the user's answer and pie_num variable.
calc_sph_volume(user_answer, pie_num) # call the calc_sph_volume function and pass in the user's answer and pie_num variable.

