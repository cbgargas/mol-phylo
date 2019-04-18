#! /usr/bin/python

import argparse
import csv
from collections import defaultdict

def get_args():

    #create and argumentparser object('parser') that will hold all info to parse the cmd line
    parser = argparse.ArgumentParser(description = 'This script removes false frequency-code pairs from telemetry data')

    #positional arguments
    #number argument to input
    parser.add_argument('csv', help='csv input file')
    parser.add_argument('tree_file', help='input tree file')

    #parse the cmd line arguments
    return parser.parse_args()

def parse_csv():
    # names dictionary: key = frequency, value = list of real names
    names = defaultdict(dict)

    # opening and reading tags file
    with open(args.csv, 'r') as chars:   
        #create a csv reader object
        reader = csv.reader(chars, delimiter=',')

        #skip the header line
        header = next(reader)

        # read in file line by line
        for line in reader:

            #skip blank lines
            if not line:
                continue
            
            else:
                # need to ask if key exists already
                if line[0] in names:
                    # same as appending to a regular list
                    names[line[0]].append(line[1])
                else:
                    names[line[0]] = []
                    names[line[0]].append(line[1])

        #check our work
        for name,value in names.items():
            print(name, value)
        
    return names

def parse_tree(names_dict):

    i=1
    # open, read, and parse the telemetry data file
    with open(args.tree_file, 'r') as tree:
        for line in tree:

            #skip the header, could make the value an optional input
            if '#NEXUS' in line:
                print(line, end=' ')
                continue
            elif 'Begin' in line:
                print(line, end=' ')
                continue
            elif 'Translate' in line:
                print(line, end=' ')
                continue
            else:
                for value,name in names_dict.items():
                    if str(name) in line:
                            print(name+',')
                    else:
                        continue


def main():
    names_dict = parse_csv()
    parse_tree(names_dict)

#get the arguments before calling main
args = get_args()

#execute the program by calling main. __ __allow you to call these functions in other scripts and not just through this one
if __name__ == '__main__':
    main() 


