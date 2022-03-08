#!/usr/bin/env python3
"""
this module has some dna manipulation functions

"""

#   imports
import sys


__author__ = 'User Name'
__version__ = '2017.23.01'


#   functions
def normalize_dna(dna_seq):
    return dna_seq.upper()


def transcribe(dna_seq):
    return dna_seq.replace('T', 'U')


def reverse(dna_seq):
    return dna_seq[::-1]


def gc(dna_seq):
    gc_amount = dna_seq.count('G') + dna_seq.count('C')
    gc_percentage = gc_amount / len(dna_seq) * 100
    return gc_percentage


def complement_translate(dna_seq):
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp_string = ''
    for char in dna_seq:
        comp_string += comp_dict[char]
    return comp_string


def main():
    dna_seq = "ATCGAACGTTT"
    print(normalize_dna(dna_seq))
    print(transcribe(dna_seq))
    print(reverse(dna_seq))
    print(gc(dna_seq))
    print(complement_translate(dna_seq))

    return 0


if __name__ == '__main__':
    sys.exit(main())
