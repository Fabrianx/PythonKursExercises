#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: malaria.py
Date: 2020-10-11
Author: Fabricio Romero García

Description:
    This progam annotate partially a nucleotide .fna file with the protein
    description contained in a .tab blastx results generated file. By inserting the
    information contained in the column 'hitDescription' from the blastx results
    .tab file to the right end of the id-lines, separated by a tab space, in
    the .fna sequences file. It generates an output.txt file with the results.
    
List of functions:
    get_annots(annot)
    add_annots(annot, seq, out)
    
List of modules used that are not explained in the course material:
    ---
    
Procedure:
    1.- The program gets the list of annotations associating it with the file
    object f1. It skips the header line in the file when looking at the lines.
    2.- It creates an empty instance. The first and tenth coulmns from the list
    of annotations are extracted and inserted in the empty instance both
    separated by a tab space.
    3.- Then, the program gets the fasta file associating it with the file
    object f2. Additionally, it creates the an output empty file.
    4.- Iteration: The program looks for all the lines beginning with ">" in
    the fasta file. The line is splitted after the last string of text.
    5.- Each line of the annotations extracted are appended at the end of each
    id-header anteceded by a tab space. The lines are appended in the exact
    same order they are in the annotation's file.
    *.- (Here is missing the matching of the query Name in the blastx file with
    the id in the fasta file, which I could not manage. Therefore, the
    hitDescription annotated in the output file is not accurate).
    6.- Output file is generated.
    
    *.- Got inspired by: "https://stackoverflow.com/questions/29930050/adding-each-item-in-list-to-end-of-specific-lines-in-fasta-file"
    
Usage:
    python malaria.py malaria.blastx.tab malaria.fna output.txt
"""
#!/usr/bin/python3
import sys

# gets list of annotations
def get_annots(infile):
    with open(infile, 'r') as f1:  # makes sure the file is closed properly
        next(f1) # skips the header line
        annots = [] # an empty instance is created
        for line in f1:
            annots.append( line.split('\t')[0] + '\t' + line.split('\t')[9]+'\n') # extraction of 1st and 10th columns separated by a tab space

    return annots

# appends the annotation
def add_annots(infile1, infile2, outfile):
    annots = get_annots(infile1) # contains list of annotations extracted previoulsy
    with open(infile2, 'r') as f2, open(outfile, 'w') as output: # makes sure the file is closed properly
        for line in f2:
            if line.startswith('>'): # which indicates the id-headers in fasta file
                line_split = list(line.split()[:4]) # split line after last string
                line_split.append(annots.pop(0)) # append data of interest to current id line
                output.write( '\t'.join(line_split) ) # join and write to file
            else:
                output.write(line)

annot = sys.argv[1]
seq = sys.argv[2]
out = sys.argv[3]

add_annots(annot, seq, out)
get_annots(annot)
