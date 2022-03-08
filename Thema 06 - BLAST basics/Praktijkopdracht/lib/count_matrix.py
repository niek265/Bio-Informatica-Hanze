#!/usr/python3

"""
This script creates a count matrix using the feature counts tool
"""

__author__ = 'Tim Swarts'


from subprocess import run as sub_run
from glob import glob


def create_count_matrix(feature_counts, gtf_file, output_dir):
    """
    The last step is the creation of the count matrix file.
    This is done with the tool feature counts.
    :param feature_counts: The path to the feature counts tool
    :param gtf_file: Gene Transfer Format is a file format used to
                     hold information about gene structure
    :param output_dir: the output_directory
    """
    for bam_file in glob(f'{output_dir}/Preprocessing/markDuplicates/*_sorted.bam'):
        command = f'{feature_counts} ' \
                  f'-a {gtf_file} ' \
                  f'-o {output_dir}/RawData/counts/geneCounts.txt' \
                  f' {bam_file}'
        print(command)
        command = command.split()
        sub_run(command, check=True)
