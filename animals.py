#!/usr/bin/python3 

#animals.py

InFileName = "animals.csv"
InFile = open(InFileName, 'r')

OutFileName = "new_animals.csv"
OutFile = open(OutFileName, 'w')

LineNumber = 0

for line in InFile:
    if LineNumber > 0:
        line = line.strip('\n')
        List = line.split(',')
        print(List[1] + "\t" + List[0])
        OutputString = (List[1] + "\t" + List[0])
        OutFile.write(str(OutputString))
    LineNumber = LineNumber + 1

InFile.close()
OutFile.close()

