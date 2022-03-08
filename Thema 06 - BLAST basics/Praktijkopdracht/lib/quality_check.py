#!/usr/bin/python3

"""
This module contains functions an classes for running fastqc on a file or on all
files in a directory.
"""

__author__ = 'Tim Swarts, Niek Scholten'
__version__ = 1.0

from subprocess import Popen, PIPE
from multiprocessing import Process
from termcolor import colored
import sys


def error_handling(f_err):
    """
    This method creates user friendly error messages.
        :param f_err: The standard error of the fastqc tool.
    """
    # Make a list of each line in the error output:
    f_err = f_err.split('\n')
    # Define empty list of new error messages:
    errors = []

    for i, line in enumerate(f_err):
        if line.startswith('Failed to'):
            # Get the error explanation from the next line
            error = f_err[i + 1]
            # Save everything after ':'
            error_start = error.find(':')
            error = error[error_start:-1]
            # Add the current line and the error together to create a nice message
            error_message = f'{line}{error}'
            # Add the message to the list of error messages
            errors.append(error_message)
    # Return new error messages
    return '\n'.join(errors)


class RunFastqc:
    """
    This is a class used to define objects that contain a specified in- and output directory.
    It includes methods to run a fastqc quality check on fastq files in the input directory.
    The output of this quality check is stored in the give output directory.
    Multiprocessing is used to make checking a large quantity of files a lot faster.
    """
    def __init__(self, output_dir):
        """
        This sets global variables within the class.
            :param output_dir: This is the output directory in which the fastqc ouput
                               is going to be stored.
        """
        self.output_dir = output_dir

    def __str__(self):
        """
        String representation of the object, returns a printable message showing
        the instance variables.
        """
        return f'{self.output_dir}'

    def run_fastqc(self, file):
        """
        This method runs the fastqc tool.
        """
        # Define the fastqc command:
        command = ['fastqc', file, '-o', f'{self.output_dir}']
        # Run the command using subprocces:
        fastqc = Popen(command, stderr=PIPE, stdout=PIPE, text=True)
        # Send the standard output en standard error to the following variables:
        out, err = fastqc.communicate()
        # Create user friendly error messages:
        err = error_handling(err)
        # Print the output and new error messages:
        print(out, err)

    def multi_run(self, files):
        """
        This method is for checking multiple files. It spawns a new process and runs the fastqc tool
        for each file in the directory.
        """

        print(colored('Running FastQC...', 'blue'))
        # Define process list:
        processes = [Process(target=self.run_fastqc, args=(file,)) for file in files]

        for process in processes:
            process.start()
        for process in processes:
            process.join()


def main():
    """
    This is the main function, which is run if the script isn't imported,
    but run on its own. It creates a new instance of the RunFastqc class,
    using just the default test values. Methods are called dependant on the input.
    """
    return 0


if __name__ == '__main__':
    EXITCODE = main()
    sys.exit(EXITCODE)
