#!/usr/bin/env python3

"""
Creates sequence dictionaries.
"""

import sys
import subprocess
import os
import multiprocessing
from termcolor import colored


class ProcessFasta:
    def __init__(self, genome_fasta, picard, output_dir):
        """
        run fasta processing
        :param genome_fasta: genome data from identifier.py
        :param picard: path to picard tool
        """
        self.fasta = genome_fasta
        self.picard = picard
        self.output_dir = f"{output_dir}/FastaProcessing"
        self.fasta_processing()

    def fasta_processing(self):
        """
        Checks if fasta.dict and fasta.fai files exist and if not
        creates them.
        """
        print(colored('Performing Fasta Process...', 'blue'))

        # checks if the file fasta.dict exists, if not it is created
        if not os.path.isfile(self.fasta.replace("fa", "dict")):
            subprocess.run(["java", "-jar", self.picard, "CreateSequenceDictionary",
                            f"R={self.fasta}",
                            f"O={self.output_dir}/{self.fasta.replace('fa', 'dict')}"],
                           check=False)
            print("\t>done")
        # checks if fasta.fai exists, if not it will be made
        if not os.path.isfile(self.fasta + "fai"):
            subprocess.run(["samtools", "faidx", self.fasta],
                           check=False)
            print("\t>done")
        return 0


if __name__ == "__main__":
    sys.exit(ProcessFasta("/home/niek265/Downloads/grch38/genome.fa"))
