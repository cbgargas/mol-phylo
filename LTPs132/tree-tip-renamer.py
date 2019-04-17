#! /usr/bin/python

import argparse
import csv
from collections import defaultdict
import pandas as pd

def get_args():

    #create and argumentparser object('parser') that will hold all info to parse the cmd line
    parser = argparse.ArgumentParser(description = 'pulls accession numbers and taxon names from fasta files and produces a dictionary from which you can rename the tips of a nexus tree file')

    #positional arguments
    parser.add_argument('fasta_file', help='input fasta file', type=str)
    #optional arguments
    parser.add_argument('-o','--out_file', help='output file name data', type=str, default='tiplabels.out')

    #parse the cmd line arguments
    return parser.parse_args()

def parse_fasta():
    # acessions dictionary: key = frequency, value = list of real acessions
    accessions = defaultdict(dict)

    # opening and reading fasta file
    with open(args.fasta_file, 'r') as fas:   
        #create a csv reader object
        reader = csv.reader(fas, delimiter='_')
        # read in file line by line
        
        for line in reader:

            # stringify what we want to be in the new tip names
            #object that contains the accession number of a fasta seq
            access=str(line[0])
            # object that contains the names of a taxon. In this case genus, species, [subsp], [unclassified], family
            name='_'.join(line[5:])

            #skip blank lines
            if not line:
                continue
            else:
                # this searches for keys, if keys exist it appends the fasta info, if it doesn't then it creates that key for that accession # and then appends the info
                # need to ask if key exists already
                if line[0] in accessions:
                    # same as appending to a regular list
                    accessions[line[0]].append(str(access+'_'+name))
                else:
                    accessions[line[0]] = []
                    accessions[line[0]].append(str(access+'_'+name))
        #check our work
        for accession,name in accessions.items():
            print(accession, name[0])
        
    return accessions

#def parse_tree(fas_dict):
#   
#    i = 1
#    # open, read, and parse the telemetry data file
#    with open(args.data_file, 'r') as data:
#        for line in data:
#
#            # by default, .split works on white space no matter how many characters
#            row = line.split()
#
#            #skip the header, could make the value an optional input
#            if row[0] == 'Date':
#                print(line, end=' ')
#                continue
#            
#            else:
#                if row[5] in code_dict[row[4]]:
#                    print(line, end=' ')
#                else:
#                    continue
#
def main():
    fas_dict = parse_fasta()
#    parse_tree(code_dict)

#get the arguments before calling main
args = get_args()

#execute the program by calling main. __ __allow you to call these functions in other scripts and not just through this one
if __name__ == '__main__':
    main() 


