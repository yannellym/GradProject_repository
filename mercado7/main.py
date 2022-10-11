from datetime import datetime
import random

''' Project 7
Empirically, take two sorting algorithms and prove (with timestamps evidence) which one is better.

In this module, there are 5 sorting algorithms available. Write your own program to generate a large 
number of random numbers and sort them using any two algorithms. Add time stamps 
(you can use the sample program I have provided in the module contents) and prove 
that one algorithm is more efficient than the other one.

Note: Unless you generate a large amount of data, you might not be able to get differentiating data.

The grading will be based on the answers to the following questions:

Are you able to create a large number of random numbers and keep them in a list? DONE
Can you feed this list to any two sorting functions (you can/should use the ones provided)? DONE
Did you add the time stamps to determine when you are about the call the sorting function(s) and when you finish determining the time (in milliseconds) it took to sort the data? DONE
Are you able to determine which algorithm is better? DONE
Can you describe, in your own words, (in less than 3 lines!), which algorithm is more efficient?
Does your program follow the coding guidelines and is it commented appropriately?
'''

'''
    File name: project_07.py
    Author: Yannelly Mercado
    Date created: 10/4/2022
    Date last modified: 10/4/2022
    Python Version: 2.7.18
'''

#executes the main function for the program
def main():
    # generates a large array of random numbers in range 0 - 100.
    rand_num = [random.randrange(0, 100, 1) for i in range(150)]
    print("Large random list of random numbers", rand_num)
    
    # Gets the current time
    start_time_one = datetime.now()
    # Calls bubble sort to sort the random numbers
    result1 = bubble_sort(rand_num)
    # Gets the current time again
    end_time_one = datetime.now()
    # stores the results of start time - end time of bubble sort
    end_result_one = end_time_one - start_time_one
    # prints the results of bubble sort
    print("Bubble sort time:", end_result_one)
    
    
    # Getting the current date and time
    start_time_two = datetime.now()
    # Calls merge sort to sort the random numbers
    result2 = merge_sort(rand_num)
    # Gets the current time again
    end_time_two = datetime.now()
    # stores the results of start time - end time of merge sort
    end_result_two = end_time_two - start_time_two
    # prints the results of merge sort
    print("Merge sort time:", end_result_two)
    
    if end_result_one < end_result_two:
        print("bubble sort executed faster")
    else:
        print("merge sort executed faster")

    
# function for bubble sort
def bubble_sort(numbers):
    # the length of numbers - 1
    for i in range(len(numbers)-1,0,-1):
        # j will go through each number in rang of i
        for j in range(i):
            # if nums j is greater than nums j + 1
            if numbers[j]>numbers[j+1]:
                # store the numbers j in a temp variable
               temp = numbers[j]
               # make numbers j equal numbers j plus 1
               numbers[j] = numbers[j+1]
               # numbers j plus one now equals the temp
               numbers[j+1] = temp
    # return the numbers, sorted at the end
    return numbers

# function for merge sort
def merge_sort(unsorted):
    # if the length of the unsorted array is 1, return the unsorted array
    if len(unsorted) <= 1:
        return unsorted
    # take the length of the unsorted array and divide it by 2
    middle = len(unsorted) // 2
    # create a left list with all the elements to the left of the middle of the unsorted array
    l_list = unsorted[:middle]
    # create a right list with all the elements to the right of the middle of the unsorted array
    r_list = unsorted[middle:]
    # recursivelt call merge sort with the left list 
    l_list = merge_sort(l_list)
    # recursivelt call merge sort with the right list 
    r_list = merge_sort(r_list)
    # return a list of the result of calling merge on left list and right list
    return list(merge(l_list, r_list))

# helper function for merge sort
def merge(l_half,r_half):
    # stores the result 
    s = []
    # while both the lists are not empty
    while len(l_half) != 0 and len(r_half)!=0:
        # if num at position 0 of left half is less than num at position 0 of right half
        if l_half[0] < r_half[0]:
            # append the num of left half to result
            s.append(l_half[0])
            # remove num from left half
            l_half.remove(l_half[0])
        else:
            # append the num of right half to result
            s.append(r_half[0])
            # remove num from right half
            r_half.remove(r_half[0])
    # if left half is empty,
    if len(l_half) == 0:
       # add the right half to result
       s = s + r_half
    else:
        # else add the left half to result
       s = s + l_half
    return s

# calls the function main   
main()