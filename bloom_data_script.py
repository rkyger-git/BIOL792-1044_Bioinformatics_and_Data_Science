#!/usr/bin/python3 

#log_body_size.py

#This script reads through "Bloom_etal_2018_Reduced_Dataset.csv" and prints out the taxon name, the diadromous status, and the total log body size. 
#define the file of interest
InFileName = "Bloom_etal_2018_Reduced_Dataset.csv"

#open and read "Bloom_etal_2018_Reduced_Dataset.csv"
InFile = open(InFileName, 'r')

#initialize LineNumber at zero
LineNumber = 0

#create empty list of body sizes
BodySizeList = []

#loop through each line in the file
for line in InFile:

    #select the non-header lines
    if LineNumber > 0:

        #remove line endings from current line
        line = line.strip('\n')

        #make a list from current line
        List = line.split(',')

        #print the taxon name and diadromous status separated by a tab
        print(List[0] + "\t" + List[3])
        
        #convert log body size from current line to a float and append it to BodySizeList
        BodySizeList.append(float(List[1]))
    
    #increment LineNumber by 1 as each new line is read
    LineNumber = LineNumber + 1

#get total log body size by summing all items in the BodySizeList
TotalLogBodySize = sum(BodySizeList)

#print total log body size
print("\nThe total log body size is", round(TotalLogBodySize, 2))

#close file 
InFile.close()

