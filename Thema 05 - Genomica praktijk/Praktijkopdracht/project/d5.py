#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for filtering VCF data.

Usage: 'd5.py -I [VCF file] -O [output file] -F [frequency]'
Or: 'main.py', by using this command the program will use default
settings for the run.
"""

import argparse
import sys

__author__ = "Niek Scholten, Rienk Heins"
__status__ = "development"
__version__ = "1.0.0"
__email__ = "n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl"


def parse_vcf_file(file, frequency, output):
    """
    Parses the vcf file and writes back the headers and the lines
    with a frequency higher than the given minimum frequency.
    :param file: Given vcf file for parsing.
    :param frequency: Minimum frequency required to write the line to the output file.
    :param output: Name of the file with output that will be created.
    """
    output_file = open(output, "a")
    # Creates the output file where the lines will be written to
    for line in open(file):
        if line.startswith("#"):
            # Checks if the line is a header
            output_file.write(line)
        elif line.startswith("chr"):
            content = line.split()
            # Splits the line to get the right content
            data = content[9].split(":")
            # Splits the Sample1 to get the FREQ value
            if float(data[6][:-1]) > frequency:
                # FREQ is the 7th value, if it's higher than the frequency the line is written
                output_file.write(line)
    output_file.close()


def main():
    """
    Main function for calling the needed functions.
    :return: Exitcode.
    """
    parser = argparse.ArgumentParser(description="Creates a filtered vcf file")
    parser.add_argument("-I", "--input_file", type=str, help="VCF file for parsing")
    parser.add_argument("-O", "--output_file", type=str, help="Name of the parsed VCF output file")
    parser.add_argument("-F", "--frequency", type=int, help="Minimum frequency to be parsed on")
    # Gets the arguments from the command line
    args = parser.parse_args()
    vcf_file = args.input_file
    out_vcf = args.output_file
    frequency = args.frequency
    if vcf_file is None:
        raise Exception("No vcf file given")
    if out_vcf is None:
        print("No output name given, default name 'd5_output.vcf' is used")
        out_vcf = 'd5_output.vcf'
    if frequency is None:
        print("No frequency given, default frequency of 30% is used")
        frequency = 30
    # Check if arguments are given, if not default values are used
    parse_vcf_file(vcf_file, frequency, out_vcf)
    print("Program is done!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
