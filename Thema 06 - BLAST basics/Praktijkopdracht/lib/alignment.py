#!/usr/bin/python3

"""
This is the alignment script that performs the actual alignment using the hisat2 tool
"""
__author__ = 'Tim Swarts'
__version__ = 0.01

from sys import exit as sys_exit
from subprocess import run as sub_run
from multiprocessing import Process
from termcolor import colored


def get_fastq_file_name(path):
    """
    This is a very small function that simply retrieves the file name and extension
    from a longer path
    :param path: The path
    :return file_name: The retrieved file name
    :return ext: the retrieved extension
    """
    # Split the path on the /'s
    name = path.split("/")
    # Get the file name and extension by splitting the last element in the list
    return name[-1].split(".")[0]


def align(command, output_dir, fastq_name):
    """
    This method contains the actual alignment execution, to prevent duplicated code
    :param command: The alignment command that will be run
    :param fastq_name: The name of the file, without its extension,
                       this name is used to create a log file of the alignment
    :param output_dir: The directory where to the output will be stored
    """

    # Make a list  out of the command, so it's safe to use with subprocess:
    input_command = command.split()

    # Set a directory for the error log:
    log_file = f'{output_dir}/Results/alignment/{fastq_name.replace("_trimmed", "")}.log'

    # Execute command with subprocess:
    with open(log_file, 'a+') as err:
        alignment = sub_run(input_command, capture_output=True, text=True, check=False)
        # Print the error to the log file
        print(alignment.stderr, file=err)

    # Use samtools to create bam file:
    # Write samtools command:
    samtools_command = f'samtools view -Sbo {output_dir}/Preprocessing/aligned/' \
                       f'{fastq_name.replace("_trimmed", ".bam")} -'
    # Run samtools command using the the output of the alignment as input:
    sam = sub_run(samtools_command.split(), capture_output=True, text=True, input=alignment.stdout,
                  check=False)


class Alignment:
    """This class has methods that are used for single and paired end alignment"""
    def __init__(self, genome_hisat2, output_dir, threads):
        """
        This method is for setting instance variables
        :param threads: This is the amount of threads that each hisat process will use
        :param genome_hisat2: This is the path to the files of the correct reference genome.
        """
        # Save genome path:
        self.genome_hisat2 = genome_hisat2
        # Save threads:
        self.threads = threads
        self.output_dir = output_dir

    def multi_run_single_end(self, files_list):
        """
        This method is for executing single end alignment on all files in a given directory.
        The directory used is output_dir, which in the pipeline, was last changed by trim_files.py.
        """
        print('Performing Alignment...')
        # Define processes list:
        processes = [Process(target=self.single_end,
                             args=(get_fastq_file_name(file), file),) for file in files_list]

        for process in processes:
            process.start()

        for process in processes:
            # Starts the processes
            process.join()

    def single_end(self, fastq_name, file):
        """
        This method performs single end alignment on a given file
        :param fastq_name: The name of the file, without its extension,
                            this name is used to create a log file of the alignment
        :param file: The full path to the file
        """
        fastq_name_colored = colored(fastq_name, 'green')
        print(f"\t>now performing alignment for: {fastq_name_colored}")
        # Write alignment command:
        full_command = f'hisat2 -x ./{self.genome_hisat2} -U {file} -p {str(self.threads)}'

        # Perform alignment:
        align(full_command, self.output_dir, fastq_name)

    def paired_end(self, file1, file2):
        """
        This method performs paired end alignment on two given files
        :param file1: The full path to the first file
        :param file2: The full path to the second file
        """
        print('Performing Alignment...')
        fastq_name = get_fastq_file_name(file1)
        # Write alignment command:
        alignment_command = f'hisat2 -x {self.genome_hisat2} -1 {file1} -2{file2} ' \
                            f'-p {str(self.threads * 2)}'
        # Perform alignment:
        align(alignment_command, self.output_dir, fastq_name)


def main():
    """
    This is the main function, this function will run when
    the script is run on its own during testing.
    """
    # I do not currently have the correct data to test the program
    return 0


if __name__ == '__main__':
    EXITCODE = main()
    sys_exit(EXITCODE)
