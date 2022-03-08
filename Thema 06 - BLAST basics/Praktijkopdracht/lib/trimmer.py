#!/usr/bin/python3

"""
This script is for trimming the files.
"""

__author__ = 'Carlo van Buiten, Tim Swarts & Niek Scholten'

from multiprocessing import Process
from subprocess import run as sub_run
from termcolor import colored


class TrimFiles:
    """
    Contains all info required for the trimming process.
    """
    def __init__(self, output_dir, trim, trim_galore):
        """
        Saves parameters for later usage.
        :param output_dir: Output directory.
        :param trim: Commandline argument.
        :param trim_galore: Path to TrimGalore.
        """
        self.output_dir = output_dir
        self.trim = trim
        self.trim_galore = trim_galore

    def __str__(self):
        """
        Prints the saved items in the object.
        :return: Formatted string.
        """
        return f'Output directory:\t{self.output_dir}\nTrim:\t{self.trim}'

    def trimmer(self, file):
        """
        Wrapper for trim_galore.
        :param file: File to trim.
        :return: Nothing.
        """
        if self.trim is None:
            print("Performing trimming using trimGalore.")
            sub_run([self.trim_galore, file,
                     "-o", f"{self.output_dir}/Preprocessing/trimmed"],
                    check=False)
        else:
            print("Performing trimming using fastx trimmer.")

            sep_trim = self.trim.split("-")

            if len(sep_trim) == 1:
                sub_run([self.trim_galore, file,
                         "--clip_R1", sep_trim[0],
                         "-o", f"{self.output_dir}/Preprocessing/trimmed"],
                        check=False)

            else:
                sub_run([self.trim_galore, file,
                         "--three_prime_clip_R1", sep_trim[1],
                         "--clip_R1", sep_trim[0],
                         "-o", f"{self.output_dir}/Preprocessing/trimmed"],
                        check=False)

    def multi_run(self, file_list):
        """

        :param file_list:
        :return:
        """
        print(colored('Trimming the files...', 'blue'))
        # Define process list:
        processes = [Process(target=self.trimmer, args=(file,))
                     for file in file_list]

        for process in processes:
            process.start()

        for process in processes:
            # Starts the processes
            process.join()
