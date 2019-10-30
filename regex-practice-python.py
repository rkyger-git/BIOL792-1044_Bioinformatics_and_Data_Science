#!/usr/bin/python3 

#regex-practice-python.py 

import re

InFileName = "regex.practice1.fasta"
InFile = open(InFileName, "r")

regex = r">(\d+_\d:\S+).+"

rep_regex = r"Homo_sapiens:\1"


#for line in InFile:
#    line = str(line)
#    line = line.strip('\n')
#    line = re.sub(regex, rep_regex, InFile)
#    print(line)

new_fasta = re.sub(regex, rep_regex, InFile)

print(new_fasta)

#close file 
InFile.close()

