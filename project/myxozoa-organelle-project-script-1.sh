#!/usr/bin/bash

# file: myxozoa-organelle-project-script-1.sh
# This program runs tblastn queries of organelle protein seqeunce .fasta files against myxozoan genome assembly .fasta files and outputs the results to .txt files. 

# Loop through the genome assembly .fna files for each myxozoan
for filename in *.fna;
do 
        # Loop through the organelle protein sequence .fasta files
        for protname in *.fasta;
        do
                # Tell user which tBLASTn has been initiated
                echo "Starting tBLASTn of $protname against $filename./n"
                # Run tblastn, -query is the protein seqeunce, -subject is the genome assembly, and -out is the .txt file with the results 
                tblastn -query $protname -subject $filename -out ${protname}_${filename}_tblastn.txt
        done
done

