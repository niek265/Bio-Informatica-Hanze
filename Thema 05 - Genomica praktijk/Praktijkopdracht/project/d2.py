#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for parsing Pileup data.

Usage: 'd2.py [bed file] [pileup file]'
"""

import sys

__author__ = 'Niek Scholten, Rienk Heins'
__version__ = '1.0.0'
__email__ = 'n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl'
__status__ = 'Finished'


def parse_pileup(bed, file):
    """
    Processes a pileup file into a dictionary.
    :param bed: The dictionary containing the information from the bed file.
    :param file: The Pileup file.
    """
    with open(file) as data:
        local_dict = {}
        for line in data:
            line = line.split()
            chromosome = line[0][3:]
            # Checks if the chromosome exists in the dictionary
            if chromosome in bed.keys():
                for exon in bed[chromosome]:
                    # Checks if the coordinate is inside of the exon range
                    if int(exon[0]) <= int(line[1]) <= int(exon[1]):
                        # Checks if the exon name exists in the dictionary
                        if exon[2] not in local_dict.keys():
                            # Create a list inside of the dictionary
                            local_dict[exon[2]] = []
                        # Add the coverage info to the corresponding key
                        local_dict[exon[2]].append(int(line[3]))
    # Return the results
    return local_dict


if __name__ == '__main__':
    sys.exit(parse_pileup(sys.argv[1], sys.argv[2]))
