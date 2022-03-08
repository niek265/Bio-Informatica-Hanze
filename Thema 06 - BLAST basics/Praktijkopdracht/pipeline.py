#!/usr/bin/python3

"""
Functions as a main script for calling all modules.
Modules are located in /lib
"""

__author__ = 'Niek Scholten, Carlo van Buiten'
__version__ = 1.0


import argparse
import configparser
import glob
import sys
from math import floor
from multiprocessing import cpu_count
from os import path

from termcolor import colored

from lib.alignment import Alignment
from lib.fastqc_analysis_analysis import AnalysisFastqcOutput
from lib.identifier import identify
from lib.make_dirs import MakeDirs
from lib.preprocessing import perform_multiqc, PreProcessing
from lib.process_fasta import ProcessFasta
from lib.quality_check import RunFastqc
from lib.trimmer import TrimFiles
from lib.multiqc_analysis import AnalysingMultiqc
from lib.count_matrix import create_count_matrix


def argument_parser():
    """
    This function creates an 'argparse' parser and adds arguments
    that will be used later in the script.
        :return parser.parse_args(): - The parser arguments
    """
    # Create parser with a description and usage
    parser = argparse.ArgumentParser(
        description='This file runs the entire program with all the modules.',
        usage='python3.7 pipeline.py -d [fastq directory] '
              '-o [hg|mm|rn|mmu] -out [out directory]'
              '-p (use paired end) -c [number of threads]'
              '-t [last bp | first and last bp]'
    )

    # Add arguments:
    parser.add_argument('-d', '--fastq_dir', type=str, metavar='', required=True,
                        help='Directory to the fq.gz/fastq.gz files. (required)')
    parser.add_argument('-o', '--organism', type=str, metavar='', required=True,
                        help='Define the two letter id for the organism '
                             'for the alignment: '
                             'Human=hs '
                             'Mouse=mm '
                             'Macaque=mmu '
                             'Rat=rn (required)')
    parser.add_argument('-out', '--output_dir', type=str, metavar='', required=True,
                        help='Pathways to new or existing output directory. (required)')
    parser.add_argument('-p', '--paired_end', action='store_true',
                        help='Switches on paired end sequencing. '
                             'Please ensure that the input consists of 2 files when '
                             'using this option. (optional)')
    parser.add_argument('-t', '--trim', type=str, metavar='', required=False, default=None,
                        help='Define the last bp or begin and end bp\'s to keep for trimming. '
                             '(optional)')
    parser.add_argument('-c', '--cores', type=str, metavar='', required=False, default=cpu_count(),
                        help='Amount of cores you want to use while '
                             'running the several tools in the pipeline.'
                             'if no value is given, this value will default '
                             'to total amount of cores available'
                             'on your system. (optional)')

    return parser.parse_args()


def config_parser():
    """
    Reads config.ini and assigns variables to their values.
    :return: Paths of the used tools.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    default = config['DEFAULT']

    return default


def list_files(directory, filetype):
    """
    Return a list of files in a specified directory.
    :param directory: Directory to search.
    :param filetype: Type of file to search for.
    :return: A list of files that were found.
    """
    files = []
    for file in filetype:
        files += glob.glob(f"{directory}/*{file}", recursive=True)
    return files


def check_path_or_file(fastq_dir):
    """
    This method simply checks whether the input was a directory or a file.
        :return 0 or 1: It returns 0 when it's a directory and 1 when it's a file.
    """
    if path.isdir(fastq_dir):
        # If the path is a directory
        # Print feedback:
        print(colored('Input is a directory', 'green'))
        return list_files(fastq_dir, ['.fastq.gz'])

    if path.isfile(fastq_dir):
        # If the path is a file
        # Print feedback:
        print(colored('Input is a file', 'green'))
        files = [fastq_dir]
        return files

    # Else, the path is non-existent:
    print(colored('Path or file doesn\'t exist', 'red'))
    # Terminate program:
    sys.exit(1)


def get_threads(process_count, cores):
    """
    This function gives back the amount of threads the a command may use
    :param process_count: The amount of processes
    :param cores: The maximum amount of threads
    :return treads: The calculated amount of usable threads per process
    """

    # Divide all the threads evenly across each process:
    threads = floor(int(cores) / process_count)
    if threads < 1:
        # If there is less than 1 thread available per process, default to 1:
        threads = 1
    # Return the value:
    return threads


def main(args, config):
    """
    Main function for calling all modules.
    :param config:
    :param args: Arguments from argparse.
    :return: Exitcode.
    """
    # Check the existence and type of the input:
    files = check_path_or_file(args.fastq_dir)

    # Set the output directory
    location = MakeDirs(args.output_dir)
    location.build_output_dir()
    location.create_all_dirs()

    # Run FastQC
    fastq = RunFastqc(f'{location.output_dir}/Results/fastQC')
    fastq.multi_run(files)

    # Get all fastqc zip output files:
    fastqc_files = [file for file in glob.glob(f"{location.output_dir}/Results/fastQC/*.zip",
                                               recursive=True)]
    # Analyse FastQC output
    analysis = AnalysisFastqcOutput(fastqc_files, f'{location.output_dir}'
                                                  f'/Results/ToolAnalysisFastqc')
    analysis.run_analysis()

    # Make sure that the fasta file of the right organism is chosen
    genome_hisat2, gtf_file, genome_fasta = identify(args.organism)
    if genome_hisat2 is None or gtf_file is None or genome_fasta is None:
        sys.exit(1)
    # Process Fasta
    ProcessFasta(genome_fasta, config['picard'], location.output_dir)

    # Trim the files
    trimmer = TrimFiles(args.output_dir,
                        args.trim,
                        config['trim_galore'])
    trimmer.multi_run(files)

    # Create alignment object and perform alignment
    trimmed_files = [path.basename(w).replace('.fastq.gz', '_trimmed.fq.gz') for w in files]
    trim_dir = f'{location.output_dir}/Preprocessing/trimmed'
    align_files = list_files(trim_dir, trimmed_files)
    aligner = Alignment(genome_hisat2, location.output_dir, get_threads(len(files), args.cores))
    if args.paired_end:
        aligner.paired_end(align_files[0], align_files[1])
    else:
        aligner.multi_run_single_end(align_files)

    # Perform preprocessing
    PreProcessing(location.output_dir)

    # Create a count matrix
    create_count_matrix(config['feature_counts'], gtf_file,
                        location.output_dir)

    # Run multiqc
    perform_multiqc(location.output_dir)

    # Analyse multiqc
    multiqc_analyser = AnalysingMultiqc(f'{location.output_dir}'
                                        f'/Results/multiQC/multiqc_data/multiqc_fastqc.txt',
                                        f'{location.output_dir}/Results/MultiqcAnalysis')
    multiqc_analyser.parse_multiqc()


if __name__ == "__main__":
    main(argument_parser(), config_parser())
