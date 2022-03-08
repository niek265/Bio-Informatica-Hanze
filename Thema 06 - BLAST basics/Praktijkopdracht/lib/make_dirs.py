#!/usr/bin/python3.7

"""
This script has functions that can be used to create certain directories,
that may be needed during the pipeline process.
If run on its own, the script creates all directories.
    Usage: python3.8 make_dirs.py
Note: In the example above python3.8 is used, but python version
3.7 should suffice as well.
"""

__author__ = 'Tim Swarts'
__version__ = '0.0.1'


import os
import sys
import shutil
from subprocess import run as sub_run
from termcolor import colored


class MakeDirs:
    """
    This class has methods that make directories during processing
    """
    def __init__(self, output_dir):
        """
        This sets global variables within the class
            :param output_dir: This is the base directory were all
                               new directories will be made.
        """
        directory = str(output_dir)
        if directory.endswith('/'):
            directory = directory.rstrip('/')
        if not len(os.listdir(output_dir)) == 0:
            print("Output directory is not empty, do you want to delete all files and continue?"
                  "(Y/N)")
            yes_no = input().lower()[0]
            if yes_no == 'y':
                sub_run(["rm", "-rf", f"{directory}/*"])
                print(f"directory {colored(directory, 'green')} emptied\n")
            else:
                sys.exit("output directory is not empty, please make sure"
                         "that the directory is empty, exiting now...")
        self.output_dir = directory

    def __str__(self):
        """
        String representation of the object, returns a printable message showing
        the instance variables.
        """
        return f"Output Direcotry: { self.output_dir }"

    def build_output_dir(self):
        """
        Check if the output directory already exists, otherwise create it.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def extend_output_dir(self):
        """
        Check if the preprocessing folder already exists, if this is not the
        case. Create this directory with the other folders.
        """
        if not os.path.exists(f"{ self.output_dir }/Preprocessing/"):
            os.makedirs(f"{ self.output_dir }/Preprocessing/")
            os.makedirs(f"{ self.output_dir }/Preprocessing/trimmed")
            os.makedirs(f"{ self.output_dir }/Preprocessing/aligned")
            os.makedirs(f"{ self.output_dir }/Preprocessing/sortedBam")
            os.makedirs(f"{ self.output_dir }/Preprocessing/addOrReplace")
            os.makedirs(f"{ self.output_dir }/Preprocessing/mergeSam")
            os.makedirs(f"{ self.output_dir }/Preprocessing/markDuplicates")

    def create_result_dir(self):
        """
        Check if the results directory exists, otherwise create it.
        """
        if not os.path.exists(f"{ self.output_dir }/Results/"):
            os.makedirs(f"{ self.output_dir }/Results/")
            os.makedirs(f"{ self.output_dir }/Results/alignment")
            os.makedirs(f"{ self.output_dir }/Results/fastQC")
            os.makedirs(f"{ self.output_dir }/Results/multiQC")
            os.makedirs(f"{ self.output_dir }/Results/ToolAnalysisFastqc")
            os.makedirs(f"{ self.output_dir }/Results/MultiqcAnalysis")

    def create_code_dir(self):
        """
        Check if the code directory exists, otherwise create it.
        """
        if not os.path.exists(f"{ self.output_dir }/Code/"):
            os.makedirs(f"{ self.output_dir }/Code/")
            os.makedirs(f"{ self.output_dir }/Code/aligningPipeline")
            os.makedirs(f"{ self.output_dir }/Code/analysis")

    def create_raw_data_dir(self):
        """
        Check if the code directory exists, otherwise create it.
        """
        if not os.path.exists(f"{ self.output_dir }/RawData/"):
            os.makedirs(f"{ self.output_dir }/RawData/")
            os.makedirs(f"{ self.output_dir }/RawData/fastqFiles")
            os.makedirs(f"{ self.output_dir }/RawData/counts")

    def remove_dirs(self):
        """
        Remove preprocessing directory
        """
        if os.path.exists(self.output_dir + "/Preprocessing/"):
            shutil.rmtree(self.output_dir + "/Preprocessing/")

    def create_all_dirs(self):
        """
        This function runs all above functions
        """
        self.build_output_dir()
        self.extend_output_dir()
        self.create_result_dir()
        self.create_code_dir()
        self.create_raw_data_dir()


def main():
    """
    This is the main function, which is run if the script isn't imported,
    but run on its own. It defines an output directory and calls the
    create_all_dirs function.
    """
    directory = "test_dir/"
    create = MakeDirs(directory)
    create.create_all_dirs()
    return 0


if __name__ == "__main__":
    EXITCODE = main()
    sys.exit(EXITCODE)
