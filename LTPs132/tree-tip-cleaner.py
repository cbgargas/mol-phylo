#! /usr/bin/python

import os
import argparse

with open('LTPs132_SSU_tree-to-mess-with.nexus', 'r') as in_tree:
    with open('temp1.txt', 'w') as temp1:
        for line in in_tree:
            if line.find(','):
                temp1.write(line.replace("'", ''))
            else:
                continue
        with open('temp1.txt', 'r') as temp2:
            with open('temp2.txt', 'w') as temp3:
                for line in temp2:
                    if line.find(','):
                        temp3.write(line.replace(' ', '_'))
                    else:
                        continue
                
os.remove('temp1.txt')
os.remove('temp2.txt')