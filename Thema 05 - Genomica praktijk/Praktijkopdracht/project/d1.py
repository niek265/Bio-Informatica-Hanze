#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for converting BED data to a usable dictionary.

Usage: 'd1.py [bed file]'
"""

import sys

__author__ = 'Niek Scholten, Rienk Heins'
__version__ = '1.0.0'
__email__ = 'n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl'
__status__ = 'Finished'


def read_bed(bed):
    """
    Reads the BED file and returns a dictionary with lists and tuples containing location info.
    :param bed: The bed file loaded from loadfile().
    :return: Dictionary containing chromosome locations.
    """
    bed_dict = {}
    print(f"Reading BED data from {bed[1]}")
    line_count = 0
    for line in open(bed[1]):
        line_count += 1
        # Split and pop to get the line ready for the dictionary
        contents = line.split()
        chromosome = contents.pop(0)
        # If the key does not exist, create it
        if chromosome not in bed_dict.keys():
            bed_dict[chromosome] = []
        # Write the contents to the corresponding key
        pos = [int(contents[0]), int(contents[1]), contents[2]]
        bed_dict[chromosome].append(tuple(pos))
    print(f"\t > A total of {line_count} lines have been read.\n")

    return bed_dict


if __name__ == '__main__':
    sys.exit(read_bed(sys.argv))
