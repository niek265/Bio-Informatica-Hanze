#!/usr/bin/env python3

"""
This module contains the AnalysingMultiqc class. This class can be used to parse
multiqc data files and give biological/technical feedback on it.
"""

__author__ = "Eric Hoekstra"
__version__ = "1.0"


import sys
from termcolor import colored
from lib.fastqc_function import AnalyseFunctions


class AnalysingMultiqc:
    """
    AnalysingMultiQC class will load a multiqc data file and analyse this.
    It will call an object and some of it's functions from the fastqc_function script.
    """
    def __init__(self, file_names, output_file):
        """
        Init function for AnalysingMultiqc class
        :param file_names: file name from the multiqc data
        """
        self.files = [file_names]
        self.output_file = f"{output_file}/multiqc_analysis_output.txt"

    def __str__(self):
        """
        string representation for object
        :return: string representation for object
        """
        return "File: {}".format(self.files)

    def parse_multiqc(self):
        """
        Parses the multiqc file from the toolnames, the tool status and its arguments.
        These will be passed to another function.
        """

        tool_dict = {}

        for file in self.files:
            open_file = open(file)
            for i, obj in enumerate(open_file):
                if i > 0:
                    # The info line for each file
                    info = [obj.split('\t')]
                    # Get the filenames
                    filename = info[0][1]
                    tool_status = info[0][13:22]
                    # Give the tool status and the filename to this function and
                    # the analysis will start
                    tool_dict = call_desired_functions(tool_status, filename,
                                                       tool_names, tool_dict)
                elif i == 0:
                    # Toolnames for visual representation, can be removed
                    tools = [obj.split('\t')]
                    tool_names = tools[0][11:20]

                    for count, tools in enumerate(tool_names):
                        toolname = tool_names[count].replace('_', " ")
                        if toolname not in tool_dict:
                            tool_dict[toolname] = []

        call_analyse_functions(tool_dict, self.output_file, self.files)


def call_desired_functions(tool_statuses, filename, tool_names, tool_dict):
    """
    This function will create a dictionary with the tools and the files that gave a
    warning or fail.
    :param tool_statuses: list with the status of each tool
    :param filename: filename for which fastq file was analysed
    :param tool_names: Names of the tools to call in the AnalyseFunctions class
    :param tool_dict: Dictionary with tools and the files that gave warn or fail
    """
    print(colored("\n\nAnalysing MultiQC output...", 'blue'))
    print("Analysis for file {}".format(filename))

    for i, tool_status in enumerate(tool_statuses):
        # To make sure it only analyses tools that either failed or gave a warning
        if tool_status.strip('\n') in ("warn", "fail"):
            toolname = tool_names[i].replace('_', " ")
            tool_dict[toolname].append(filename)

    return tool_dict


def call_analyse_functions(tool_dict, output_file, input_files):
    """
    Function to call the functions that analyse each tool.
    :param tool_dict: Dictionary with tools and the files that gave a warning
    :param output_file: Output file it's name
    :param input_files: Input files their names
    """

    input_files = ", ".join(input_files)
    print(f"Creating fastqc analysis output file: {colored(output_file, 'green')} for "
          f"{colored(input_files, 'green')}")

    for i in tool_dict:
        if tool_dict[i]:
            analyse = AnalyseFunctions(tool_dict[i], output_file, tool_dict)
            toolname = i
            if toolname == "per base sequence quality":
                analyse.per_base_sequence_quality()
            elif toolname == "per sequence quality scores":
                analyse.per_sequence_quality_scores()
            elif toolname == "per base sequence content":
                analyse.per_base_sequence_content()
            elif toolname == "per sequence quality scores":
                analyse.per_sequence_quality_scores()
            elif toolname == "per sequence gc content":
                analyse.per_sequence_gc_content()
            elif toolname == "per base n content":
                analyse.per_base_n_content()
            elif toolname == "sequence length distribution":
                analyse.sequence_length_distribution()
            elif toolname == "sequence duplication levels":
                analyse.sequence_duplication_levels()
            elif toolname == "overrepresented sequences":
                analyse.overrepresented_sequences()
            elif toolname == "adapter content":
                analyse.adapter_content()
            elif toolname == "kmer content":
                analyse.kmer_content()
            else:
                print("Tool not found, check if the file name is correct")

            analyse.output_file.close()


if __name__ == "__main__":
    sys.exit()
