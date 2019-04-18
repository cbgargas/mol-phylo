#! /usr/bin/python

import argparse
import csv

# create a column of taxa names in csv file by matching taxa names 
#in renamed tree file to taxa names in csv file of characters



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
