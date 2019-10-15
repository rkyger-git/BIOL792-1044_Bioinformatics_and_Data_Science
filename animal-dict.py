#!/usr/bin/bash

# file: animal-dict.py

# description: This script loops through a dictionary of animals and their sizes and prints "Big" if the size is bigger than 20, otherwise "Small" is printed.   

#create animal dictionary
animal_dict = {'beetle':1, 'mouse':15, 'elephant':10000}

# print keys
print(animal_dict.keys())

#loop thorugh each pair in dictionary
for animal in animal_dict:
    #print animal name and "Big" if size is >20
    if animal_dict[animal] > 20:
        print(animal, "Big") 
    #print animal name and "Small" if size is <20 
    else:
        print(animal, "Small") 

