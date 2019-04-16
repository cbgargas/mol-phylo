#! /usr/bin/python

with open('LTPs132_SSU_tree-to-mess-with.nexus', 'r') as tree:
    with open('output.txt', 'w') as out:
        for line in tree:
            if line.find(' '):
                out.write(line.replace(' ', '_'))
            else:
                continue 

