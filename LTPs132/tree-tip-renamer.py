#! /usr/bin/python

import argparse
import csv
from collections import defaultdict
from Bio import SeqIO 
import subprocess


def get_args():

    #create and argumentparser object('parser') that will hold all info to parse the cmd line
    parser = argparse.ArgumentParser(description = 'pulls accession numbers and taxon names from fasta files and produces a dictionary from which you can rename the tips of a nexus tree file')

    #positional arguments
    parser.add_argument('fasta_infile', help='input fasta file', type=str)
    parser.add_argument('tree_infile', help='input tree file', type=str)
    #optional arguments
    parser.add_argument('-slo','--seqlist_outfile', help='output file name data', type=str, default='tiplabels.out')
    parser.add_argument('-f1','--format1', help='format of input file', type=str, default='fasta')
    parser.add_argument('-f2','--format2', help='format for output file', type=str, default='fasta-2line')
    parser.add_argument('-fo','--fasta_outfile', help='name for your output file', type=str, default='output.fixed.fa')

    #parse the cmd line arguments
    return parser.parse_args()

# function to clean up shitty silva fasta files 
def fasta_fixer():
    #open your output file for writing
    with open('/tmp/temp1.fa', 'w') as temp1:
        #open your input fasta file
        with open(args.fasta_infile, 'r') as fasta: 
            #read in fasta file with SeqIO
            SeqIO.convert(fasta, args.format1, temp1, args.format2)
            #gives available options for an object
            #print(dir(fsa))
            with open('/tmp/temp2.fa', 'w') as temp3:
                #open your output1 file for writing
                with open('/tmp/temp1.fa', 'r') as temp2:
                #add an if/then statement for sequence headers
                    for line in temp2:
                        if line.find('>'):
                            temp3.write(line.replace('.', '-'))
                        else:
                            temp3.write(line.replace(' ', '_'))
                    with open(args.fasta_outfile, 'w') as output:   
                        with open('/tmp/temp2.fa', 'r') as temp4:
                            for line in temp4:
                                if line.find('\t'):
                                    output.write(line.replace('\t', '_'))
                                else:
                                    continue
    return

# function to output a list of fasta headers without '>' or '.' 
def seq_list(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')
    
    
# parses the fasta file and creates a dictionary of accessions (keys):taxon name (defs)
def parse_fasta():
    # acessions dictionary: key = frequency, value = list of real acessions
    accessions = defaultdict(dict)

    # opening and reading fasta file
    with open(args.seqlist_outfile, 'r') as fas:   
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
            print(accession, name)
        
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
    fasta_fixer()
    seq_list(cmd="grep '>' "+args.fasta_outfile+" | tr -d '.' | tr -d '>' > "+args.seqlist_outfile)
    fas_dict = parse_fasta()
#    parse_tree(code_dict)

#get the arguments before calling main
args = get_args()

#execute the program by calling main. __ __allow you to call these functions in other scripts and not just through this one
if __name__ == '__main__':
    main() 


