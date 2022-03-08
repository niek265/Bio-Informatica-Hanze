#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for checking ANNOVAR data.

Usage: 'd6.py'
"""

import sys

__author__ = 'Niek Scholten, Rienk Heins'
__version__ = '1.0.0'
__email__ = 'n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl'
__status__ = 'Finished'


def split_file(filename):
    """
    Splits the file.
    :param filename: Name of the input ANNOVAR file.
    """
    print("help")
    for line in open(filename):

        colomn = [15, 16, 27, 33, 34, 35, 53]
        content = line.split("\t")
        print("\t".join([content[x] for x in colomn]))
    filename.close()


if __name__ == "__main__":
    split_file(sys.argv[1])
