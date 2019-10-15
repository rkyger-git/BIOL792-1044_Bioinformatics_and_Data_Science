#!/usr/bin/bash

# file: add-one.py

# description: This script loops through a list of numbers, adds 1 to each number, and prints the numbers.  

# create list of numbers
num_list =  [1,2,3,4,5,6]

# loop through each number in the list
for num in num_list:
    # add one to each number
    num = num + 1
    # print new numbers 
    print(num)


#Notes: Orginallly, I was overthinking this problem.

#Solution 1:
#num_list = [1,2,3,4,5,6]
#new_list = []

#for num in num_list:
    #num = num + 1
    #new_list.append(num)

#print(new_list)

#Solution 2:
# This would be much easier with a list comprehension. 
# num_list = [1,2,3,4,5,6]
# new_num_list = [num+1 for num in num_list]
# print(new_num_list)

