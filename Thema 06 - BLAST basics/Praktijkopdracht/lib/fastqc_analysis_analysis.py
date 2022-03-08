#!/usr/bin/env python3

"""
Description:
Analysing the fastqc analysis data and giving a biological/technical explanation.
This module makes use of the class in the fastqc_functions.py module. This
module should be located in the same map, it will not work if it's not.

Usage:
Uses a fastqc_data.txt as input. If you want to change this to a desired file
change the argument on line 118 to the path of the desired file.
"""

__author__ = "Eric Hoekstra"
__version__ = "1.0"

from os import path
from zipfile import ZipFile
from sys import exit as sys_exit
from lib.fastqc_function import AnalyseFunctions
from termcolor import colored


class AnalysisFastqcOutput:
    """
    AnalysisFastqc output is a class that parses the fastQC output and returns it.
    It will use a fastQC.txt as input and it will return a dictionary with as key
    the fastQC toolname and as value the data belonging to that tool.
    """
    def __init__(self, fastqc_data_list, output_data):
        """
        init function for the AnalysisFastqcOutput class
        """
        self.fastqc_data_list = fastqc_data_list
        self.output_data = f"{output_data}/fastqc_analysis_output.txt"

    def __str__(self):
        """
        str function for the AnalysisFastqcOutput class
        :return: str representation for the object
        """
        return f"file list:\t{self.fastqc_data_list}"

    def __repr__(self):
        """
        repr function for the AnalysisFastqcOutput class
        :return: str represenentation for the object
        """
        return self.fastqc_data_list

    def run_analysis(self):
        """
        This function multi runs the analysis to make it faster.
        """

        print(colored('Analysing FastQC ouput...', 'blue'))

        failed_tools_dict = {}

        for fastqc_data in self.fastqc_data_list:
            # Unzip the files
            archive = ZipFile(fastqc_data, 'r')
            filename = path.basename(fastqc_data)
            fastqc_data = archive.open(f'{path.splitext(filename)[0]}/fastqc_data.txt')
            # Create data dict for analysis
            data_dict = get_data(fastqc_data)

            failed_tools_dict = analyse(data_dict, filename, failed_tools_dict)

        # calling the analyse functions
        call_analyse_functions(failed_tools_dict, self.output_data, self.fastqc_data_list)


def get_data(fastqc_data):
    """
    This function will parse the fastqc_data.txt, it will put the results
    in a dictionary. The key will be the fastQC toolname and the value
    will be the data belonging to this tool.
    :return: dictionary like described above
    """

    # Defining variables
    data_list = []
    data_dict = {}
    toolname = ''

    for line in fastqc_data:
        line = line.decode()
        # Define boolean to decide which lines to parse
        add_line = True
        end_line = line.split("\t")[-1]
        # If the line starts with >>END module the module is over
        if line.startswith(">>END_MODULE\n"):
            # If the toolname is not yet in the dict it will be added
            if toolname not in data_dict:
                data_dict[toolname] = data_list

            # The data list will be emptied to make it possible for new data to be added
            data_list = []
        # If the line starts with >> and does not end with "pass" it will be added
        elif line.startswith(">>") and end_line != "pass\n":
            # Defining toolname
            toolname = line.split(">>")[1]
        # Makes sure no data is added when the data gave a pass
        elif end_line == "pass\n" and line.startswith(">>"):
            data_list = []
        # Adds data to the data_list
        elif add_line:
            data_list.append(line)

    return data_dict


def analyse(data_dict, filename, failed_tools_dict):
    """
    Function to create a dictionary with toolnames and the samples that failed those tools
    :return: failed_tools_dict: All the tools that gave warning with the samples that failed with
                                this tool.
    """

    for key in data_dict:
        # Set status
        toolname = key.split("\t")[0].lower()
        # If the toolname is empty it should not continu
        if toolname:
            # Create key for dictionary with certain file
            if toolname not in failed_tools_dict:
                failed_tools_dict[toolname] = [filename]
            else:
                failed_tools_dict[toolname].append(filename)

    return failed_tools_dict


def call_analyse_functions(tool_dict, output_file, input_files):
    """
    Function to call the functions that analyse each tool.
    :param tool_dict: Dictionary with the failed tools and their filenames
    :param output_file: Output file name
    :param input_files: Input files their names
    """

    input_files = ",\n".join(input_files)
    print(f"Creating fastqc analysis output file: {colored(output_file, 'green')} for "
          f"{colored(input_files, 'green')}")

    for i in tool_dict:
        # If the tool is in the dictionary and its not empty then continu
        if i in tool_dict and tool_dict[i]:
            analysis = AnalyseFunctions(tool_dict[i], output_file, tool_dict)
            toolname = i
            # Call the correct function corresponding to the tool
            if toolname == "per base sequence quality":
                analysis.per_base_sequence_quality()
            elif toolname == "per sequence quality scores":
                analysis.per_sequence_quality_scores()
            elif toolname == "per base sequence content":
                analysis.per_base_sequence_content()
            elif toolname == "per sequence quality scores":
                analysis.per_sequence_quality_scores()
            elif toolname == "per sequence gc content":
                analysis.per_sequence_gc_content()
            elif toolname == "per base n content":
                analysis.per_base_n_content()
            elif toolname == "sequence length distribution":
                analysis.sequence_length_distribution()
            elif toolname == "sequence duplication levels":
                analysis.sequence_duplication_levels()
            elif toolname == "overrepresented sequences":
                analysis.overrepresented_sequences()
            elif toolname == "adapter content":
                analysis.adapter_content()
            elif toolname == "kmer content":
                analysis.kmer_content()
            else:
                print("Tool not found, check if the file name is correct")

            analysis.output_file.close()


if __name__ == "__main__":
    sys_exit()
