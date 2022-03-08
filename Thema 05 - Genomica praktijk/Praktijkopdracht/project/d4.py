#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for converting Pile-up data to CSV

Usage: 'd4.py.py [bed file] [pileup file] [name for csv file] [processors]'
Or: 'd4.py', by using this command the program will use default
settings for the run.
"""

import sys
import csv
import warnings
import multiprocessing as mp
from os import path
from multiprocessing import Manager, Queue
from tqdm import tqdm

__author__ = 'Niek Scholten, Rienk Heins'
__version__ = '1.1.0'
__email__ = 'n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl'
__status__ = 'Finished'


def loadfile(arg):
    """
    Asks for filenames if they are not given.
    :return: The names of the BED, Pile-up & CSV file and the amount of processors.
    """
    files = []
    # Checks if the user gives the right input
    if len(arg) == 5:
        files = arg[1:5]
    elif len(arg) == 1:
        files.append(input('Please enter the file name of the bed file: '))
        files.append(input('Please enter the file name of the pile-up file: '))
        files.append(input('Please enter the file name of the csv file to write to: '))
        # Checks if the user has a system capable of multiprocessing
        if mp.cpu_count() > 1:
            print(f"It appears your system has {mp.cpu_count()} processors.")
            files.append(input('How many would you like to use?\n'))
        else:
            files.append(1)
    else:
        raise Exception("File should be used with commandline 'main.py'"
                        " or 'main.py [BED file] [Pileup file] [name csv file] [Processors]',"
                        " program will end now")

    # Checks the BED input for any problems
    if not files[0].lower().endswith('.bed'):
        warnings.warn('Given BED file does not have a ".bed" extension.', Warning)
    if files[0] is None:
        raise Exception('No BED-data read.')

    # Checks the Pileup input for any problems
    if not files[1].lower().endswith('.pileup'):
        warnings.warn('Given pileup file does not have a ".pileup" extension.', Warning)
    if files[1] is None:
        raise Exception('No Pileup-data read.')

    # Checks the CSV input for any problems
    if not files[2].lower().endswith('.csv'):
        warnings.warn('Given pileup file does not have a ".csv" extension.', Warning)
    if files[2] is None:
        raise Exception('No CSV data to write to.')

    # Checks if amount of cores is an integer
    if not isinstance(files[3], int):
        try:
            files[3] = int(files[3])
        except ValueError:
            raise Exception("Amount of processors is not a number.")

    return files


def process_wrapper(chunk_start, chunk_size, bed, file):
    """
    The process each worker starts to go through the file.
    :param chunk_start: Start location of the line that needs to be read.
    :param chunk_size: The size of the chunk that needs to be read.
    :param bed: The dictionary containing the information from the bed file.
    :param file: The Pileup file.
    """
    with open(file) as data:
        # Searches the file for the start of the chunk
        data.seek(chunk_start)
        # Splits the chunk in lines
        lines = data.read(chunk_size).splitlines()
        local_dict = {}
        for line in lines:
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
    # Add the results to the queue
    QUEUE.put(local_dict)


def split_file(filename, cores):
    """
    Splits the file into 'chunks' so they can be processed individually.
    :param filename: The name of the Pileup file.
    :param cores: Amount of cores to be used.
    :return:
    """
    # Set the file end to the file size
    file_end = int(path.getsize(filename))
    # Set the chunk size based on the amount of processors
    size = round(file_end/cores/8)
    # Open the file as binary read
    with open(filename, 'rb') as file:
        # Set the chunk end to the current cursor position
        chunk_end = file.tell()
        while True:
            chunk_start = chunk_end
            # Add the chunk size to the current position
            file.seek(size, 1)
            # Read to the end of the line
            file.readline()
            # Get the end of the chunk
            chunk_end = file.tell()
            # Return the start of the chunk and size, while maintaining the cursor position
            yield chunk_start, chunk_end - chunk_start
            # If the end of the chunk is outside of the file, break the loop
            if chunk_end > file_end:
                break


def read_bed(bed):
    """
    Reads the BED file and returns a dictionary with lists and tuples containing location info.
    :param bed: The bed file loaded from loadfile().
    :return: Dictionary containing chromosome locations.
    """
    bed_dict = {}
    print(f"Reading BED data from {bed}")
    line_count = 0
    for line in open(bed):
        line_count += 1
        # Split and pop to get the line ready for the dictionary
        contents = line.split()
        chromosome = contents.pop(0)
        # If the key does not exist, create it
        if chromosome not in bed_dict.keys():
            bed_dict[chromosome] = []
        # Write the contents to the corresponding key
        bed_dict[chromosome].append(tuple(contents))
    print(f"\t > A total of {line_count} lines have been read.\n")

    return bed_dict


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


def main(filenames):
    """
    Creates all the necessary variables and sets up each function.
    :param filenames: List containing the filenames and amount of cores to be used.
    :return: Exitcode.
    """
    print('Parsing BED data...')
    # Parse the bed file name to read_bed
    bed_sorted = read_bed(filenames[0])
    print(f"\t> A total of {len(bed_sorted.keys())} chromosomes have been stored.\n")

    cores = filenames[3]
    # Opens the processing pool with the amount cores given
    pool = mp.Pool(cores)
    jobs = []
    # Create a dictionary that will be shared with all the processes
    managed_dict = MANAGER.dict()
    print('Parsing and filtering pileup-data...')
    # Parse the file to the function that creates the chunks
    for start, size in split_file(filenames[1], cores):
        # Add the jobs to a list, apply to the pool without an order
        jobs.append(pool.apply_async(process_wrapper,
                                     (start, size, bed_sorted,
                                      filenames[1])))
    # Create the progress bar
    pbar = tqdm(total=(len(jobs)))

    # Run all jobs in the list
    for job in jobs:
        job.get()
        pbar.update()

    # After all the jobs are done, get the results from the queue and add them to the dictionary
    for i in range(len(jobs)):
        managed_dict.update(QUEUE.get())

    # Close the progress bar and the processing pool
    pbar.close()
    pool.close()

    print(f"\t> Coverage of {len(managed_dict.keys())} genes have been stored.\n")
    print("Calculating coverage statistics...")
    coverage_stats = mapping_coverage(managed_dict)
    print(f"\t> Statistics for {len(coverage_stats)} genes have been calculated.\n")

    print(f"Writing the coverage statistics to {filenames[2]}")
    create_csv(coverage_stats, filenames[2])
    print("\t> CSV file created, program finished.")
    # Return the exit code
    return 0


if __name__ == '__main__':
    if sys.version_info[0] == 3 and sys.version_info[1] < 6 or sys.version_info[0] < 3:
        raise Exception("Must be using Python 3.6 or newer.")
    ARGS = loadfile(sys.argv)
    MANAGER = Manager()
    QUEUE = Queue()
    EXITCODE = main(ARGS)
    sys.exit(EXITCODE)
