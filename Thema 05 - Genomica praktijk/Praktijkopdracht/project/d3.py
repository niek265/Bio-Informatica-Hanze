#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for parsing Pileup data.

Usage: 'd3.py [bed file] [pileup file] [csv file]'
"""

import sys
import csv

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


def parse_pileup(bed, file):
    """
    The process each worker starts to go through the file.
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
                            # Create a managed list inside of the managed dictionary
                            local_dict[exon[2]] = []
                        # Add the coverage info to the corresponding key
                        local_dict[exon[2]].append(int(line[3]))
    # Return the results
    return local_dict


def mapping_coverage(coverage_info):
    """
    Maps out the coverage of the Pile-up file.
    :param coverage_info: Dictionary containing the coverage information.
    :return: Information about the coverage per gene.
    """
    statistics = []
    total_cov = 0
    total_low = 0
    # Loop through the dictionary
    for gene in coverage_info.keys():
        # Find the right info for the gene
        info = coverage_info[gene]
        cov_sum = 0
        low_coverage = 0
        for cov in info:
            total_cov += 1
            # Count the total coverage
            cov_sum += int(cov)
            # If the coverage is low, add it to the counter
            if int(cov) <= 30:
                low_coverage += 1
                total_low += 1
        # Calculate average coverage
        avrg = round(cov_sum/len(info), 1)
        stat = [gene, len(info), avrg, low_coverage]
        statistics.append(tuple(stat))
        # Create a list with tuples containing a gene and it's coverage info
        print(f"Gene:{gene} , average coverage: {avrg}, low coverage: {low_coverage}")
    if total_low > 0:
        percentage = round(total_low/total_cov * 100)
    else:
        # Set the percentage to 0 if no low coverages are found
        percentage = 0
    print(f"Total bases:{total_cov}, with low coverage {total_low} ({percentage}%)\n")
    return statistics


def create_csv(stats, filename):
    """
    Writes the data to the CSV file.
    :param stats: The statistics created by mapping_coverage().
    :param filename: The name of the csv file.
    :return: CSV File.
    """
    with open(filename, "w", newline='') as file:
        # Creates a csv file with the by the user given name or default name
        writer = csv.writer(file)
        for stat in stats:
            # Writes the information from the stats list to four columns in the csv file
            writer.writerow([stat[0], stat[1], stat[2], stat[3]])


def main(args):
    """
    Main function for assigning variables.
    :param args: Commandline arguments.
    :return: Exitcode.
    """
    bed = read_bed(args[1])
    cov_info = parse_pileup(bed, args[2])
    csv_file = args[3]
    create_csv(mapping_coverage(cov_info), csv_file)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
