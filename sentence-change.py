#!/usr/bin/python3

# file: sentence-change.py
# This program takes a sentence from user input, turns letters to lower case, removes the space, and counts the length.

#give user instructions and convert input into string
sentence = string(input("Please input a sentence: "))
	
#convert to lower case
sentence = sentence.lower()

#replace spaces with nothing
sentence = sentence.replace(“ “, “”)

#print new sentence
print("The new sentence is: ", sentence)

#print sentence length
print("The length of the sentence is: ", len(sentence))

