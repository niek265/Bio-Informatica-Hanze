#!/usr/bin/env python3

"""
Marks duplicates and creates count files/
"""

import sys
import glob
from subprocess import run as sub_run
import multiprocessing
from termcolor import colored


def write_preprocess_to_file(output, file_name):
    """
    This function is for writing preprocessing output to output files
    :param output: The output that wil be written to a file
    :param file_name: The name of the output file
    """
    file_name_colored = colored(file_name, 'green')
    print(f"\t>now creating: {file_name_colored}")
    file = open(file_name, 'w+')
    file.close()
    file = open(file_name, 'w')
    print(output, file=file)
    file.close()


class PreProcessing:
    """
    Holds info for the picard tool.
    """

    def __init__(self, output_dir):
        """
        Initializes the object.
        :param self.output_dir: Directory to place output files.
        """
        self.output_dir = output_dir
        self.pre_processing()

    def pre_processing(self):
        """
        This function consists of the sorting, adding or replacing of
        groups, fixing of mate information, merging, marking of duplicates
        and a sorting for the creation of the count files.
        """
        print("Performing processing steps to create the count file,\n"
              "the stdout of each tool is written to a .txt file")
        # creates a new process for each file in the output directory
        processes = []
        for aligned_file in glob.glob(f'{self.output_dir}/Preprocessing/aligned/*.bam'):
            processes.append(multiprocessing.Process(target=self.file_process,
                                                     args=(aligned_file,)))
        # runs the processes
        for process in processes:
            process.start()
        for process in processes:
            process.join()

        return 0

    def file_process(self, aligned_file):
        """
        Runs all commands to create files.
        :param aligned_file: File to use with picard.
        :return: Nothing.
        """
        
        picard = "lib/Picard-2.21.6/picard.jar"
        aligned_files_sep = aligned_file.split("/")
        current_file = aligned_files_sep[-1].replace(".bam", "")

        # The follow code runs command line arguments to create the count files
        # SortSam:
        sort_sam = sub_run(["java", "-jar", picard, "SortSam",
                            f"I={self.output_dir}/Preprocessing/aligned/{current_file}.bam",
                            f"O={self.output_dir}/Preprocessing/sortedBam/{current_file}.bam",
                            "SO=queryname"], capture_output=True, text=True, check=False)
        # Write stdout to file:
        write_preprocess_to_file(sort_sam.stdout,
                                 f'{self.output_dir}/Preprocessing/{current_file}-SortSam.txt')

        # AddOrReplaceReadGroups:
        add_or_replace = sub_run(["java", "-jar", picard, "AddOrReplaceReadGroups",
                                  f"INPUT={self.output_dir}/Preprocessing/sortedBam/"
                                  f"{current_file}.bam",
                                  f"OUTPUT={self.output_dir}/Preprocessing/"
                                  f"addOrReplace/{current_file}.bam",
                                  f"LB={current_file}", f"PU={current_file}",
                                  f"SM={current_file}", "PL=illumina", "CREATE_INDEX=true"],
                                 capture_output=True, text=True, check=False)
        # Write stdout to file:
        write_preprocess_to_file(add_or_replace.stdout,
                                 f'{self.output_dir}/Preprocessing/{current_file}-'
                                 f'AddOrReplaceReadGroups.txt')

        # FixMateInformation:
        fix_mate_information = sub_run(["java", "-jar", picard, "FixMateInformation",
                                        f"INPUT={self.output_dir}/Preprocessing/"
                                        f"addOrReplace/{current_file}.bam"],
                                       capture_output=True, text=True, check=False)
        # Write stdout to file:
        write_preprocess_to_file(fix_mate_information.stdout,
                                 f'{self.output_dir}/Preprocessing/{current_file}-'
                                 f'FixMateInformation.txt')

        # MergeSamFiles:
        merge_sam_files = sub_run(["java", "-jar", picard, "MergeSamFiles",
                                   f"INPUT={self.output_dir}/Preprocessing/"
                                   f"addOrReplace/{current_file}.bam",
                                   f"OUTPUT={self.output_dir}/Preprocessing/"
                                   f"mergeSam/{current_file}.bam",
                                   "CREATE_INDEX=true", "USE_THREADING=true"],
                                  capture_output=True, text=True, check=False)
        # Write stdout to file:
        write_preprocess_to_file(merge_sam_files.stdout,
                                 f'{self.output_dir}/Preprocessing/{current_file}-'
                                 f'MergeSamFiles.txt')

        # MarkDuplicates
        mark_duplicates = sub_run(["java", "-jar", picard, "MarkDuplicates",
                                   f"INPUT={self.output_dir}/Preprocessing/"
                                   f"mergeSam/{current_file}.bam",
                                   f"OUTPUT={self.output_dir}/Preprocessing/"
                                   f"markDuplicates/{current_file}.bam",
                                   "CREATE_INDEX=true",
                                   f"METRICS_FILE={self.output_dir}/Preprocessing/"
                                   f"markDuplicates/{current_file}.metrics.log"],
                                  capture_output=True, text=True, check=False)
        # Write stdout to file:
        write_preprocess_to_file(mark_duplicates.stdout,
                                 f'{self.output_dir}/Preprocessing/{current_file}-'
                                 f'MarkDuplicates.txt')

        # SamtoolsSort:
        samtools_sort = sub_run(["samtools", "sort", "-n",
                                 f"{self.output_dir}/Preprocessing/"
                                 f"markDuplicates/{current_file}.bam",
                                 "-o", f"{self.output_dir}/Preprocessing/"
                                       f"markDuplicates/{current_file}_sorted.bam"],
                                capture_output=True, text=True, check=False)
        # Write stdout to file:
        write_preprocess_to_file(samtools_sort.stdout,
                                 f'{self.output_dir}/Preprocessing/{current_file}-SamtoolsSort.txt')


def perform_multiqc(output_dir):
    """
    Function that performs the multiqc step
    """
    print(colored('Running MultiQC...', 'blue'))
    sub_run(["multiqc", output_dir, "-o", f"{output_dir}/Results/multiQC/", '-f'],
            check=False)
    return 0


def main():
    """
    Main for calling the code.
    :return:
    """
    PreProcessing('')
    perform_multiqc('')
    return 0


if __name__ == "__main__":
    sys.exit(main())
