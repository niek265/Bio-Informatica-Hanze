#!/usr/bin/env python3

"""
This script contains a class with functions within it to analyse fastQC output with.
This standalone script can only be used in combination with the fastqc_analysis_analysis.py

For more information about how to use this script check the description of the other script.
"""

__author__ = "Eric Hoekstra"
__version__ = "1.0"

from termcolor import colored


class AnalyseFunctions:
    """
    Class containing all the functions to analyse every FastQC tool
    and give biological/technical feedback on it.
    """
    def __init__(self, files, output_file, tool_dict):
        """
        init function for AnalyseFunctions class
        :param files: files in the right format
        :param output_file: Output file name
        :param tool_dict: Dictionary with tools and as value the files that failed these tools
        """

        self.output_file = open(output_file, 'a+')
        self.files = files
        self.tool_dict = tool_dict

    def __str__(self):
        """
        str function for the AnalyseFunctions class
        """
        return "files: {}".format(self.files)

    def per_base_sequence_quality(self):
        """
        Analysing the per base sequence quality tool and giving feedback on that.
        """

        if self.tool_dict['per base sequence quality']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['per base sequence quality']),
                  file=self.output_file)

        # Printing function name
        print("\nPer_base sequence quality\n", file=self.output_file)

        # Giving exact feedback on why what error was given

        print("The lower quartile for any base is less than 10, or the median\n"
              "the median for any base is less than 25.", file=self.output_file)

        print("The lower quartile for any base is less than 5, or the median\n"
              "for any base is less than 20.", file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("\nBiological/technical reason:\n"
              "- A general degradation of quality over the duration of long runs\n"
              "- Loss of quality early on in reads, which then proceeds to produce\n"
              "  good quality reads later on. This can happen because of a momentary\n"
              "  problem such as a bubble passing through a flowcell", file=self.output_file)

    def per_base_sequence_content(self):
        """
        Analysing the per base sequence content tool and giving feedback on that.
        """

        if self.tool_dict['per base sequence content']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['per base sequence content']),
                  file=self.output_file)

        # Printing function name
        print("\nPer_base sequence content:\n", file=self.output_file)

        # Giving exact feedback on why what error was given

        print("The difference between A and T, or G and C is greater than 20% in any position.",
              file=self.output_file)

        print("The difference between A and T, or G and C is greater than 10% in any position",
              file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("\nBiological/technical reason:"
              "\n - Overrepresented sequences"
              "\n - Biased fragmentation"
              "\n - Biased composition libraries"
              "\n - Aggressive trimming", file=self.output_file)

    def sequence_length_distribution(self):
        """
        Analysing the sequence length distribution function in fastqc by calculating the average
        read length and giving feedback on that.
        """

        if self.tool_dict['sequence length distribution']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['sequence length distribution']),
                  file=self.output_file)

        print("\nSequence length distribution: \n", file=self.output_file)

        print("All sequences are not the same length", file=self.output_file)

        print("One of the sequences has length 0", file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn

        print("\nAverage read length is low! "
              "\nBiological/technical reason:\n"
              "- The data was probably scanned and skimmed to remove adapter regions, "
              "which means you have short inserts.\n"
              "- Different read lengths may be completely normal", file=self.output_file)

    def overrepresented_sequences(self):
        """
        Analysing the overrepresented sequences tool and giving feedback on that.
        """

        if self.tool_dict['overrepresented sequences']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['overrepresented sequences']),
                  file=self.output_file)

        # Printing function name
        print("\nOverrepresented sequences:\n", file=self.output_file)

        # Giving exact feedback on why what error was given

        print("Sequence is present in more than 0.1% of the reads",
              file=self.output_file)

        print("Sequence is present in more than 1% of the reads",
              file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("Biological/technical reason:\n\n"
              "- Small RNA libraries where sequences are not subjected to random fragmentation, "
              "and the same sequence may naturally be more present", file=self.output_file)

    def per_sequence_quality_scores(self):
        """
        Analysing the per sequence quality scores tool and giving feedback on that.
        """

        if self.tool_dict['per sequence quality scores']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['per sequence quality scores']),
                  file=self.output_file)

        print("The mean quality is below 27, this means that there's a 0.2% error rate!",
              file=self.output_file)

        print("The mean quality is below 20, this means that there's an 1% error rate!",
              file=self.output_file)

        # Printing function name and giving feedback on the biological/technical reason for
        # the fail/warn
        print("\nPer sequence quality scores:\n"
              "Biological/technical reason:"
              "\n- Stain on microarray"
              "\n- Shorter inserts than expected"
              "\n- Low diversity sequences can lead to mistakes made by software",
              file=self.output_file)

    def per_sequence_gc_content(self):
        """
        Analysing the per sequence gc content tool and giving feedback on that.
        """

        if self.tool_dict['per sequence gc content']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['per sequence gc content']),
                  file=self.output_file)

        # Printing function name
        print("\nPer sequence GC content:\n", file=self.output_file)

        # Giving exact feedback on why what error was given

        print("Sum of the deviations from the normal distribution represents more "
              "than 15% of the reads", file=self.output_file)

        print("Sum of the deviations from the normal distribution represents more "
              "than 30% of the reads", file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("\nBiological/technical reason:\n"
              "- Overrepresented sequences\n"
              "- Overrepresented sequences may originate from the ribosomal RNA/DNA",
              file=self.output_file)

    def per_base_n_content(self):
        """
        Analysing the per base n content tool and giving feedback on that.
        """

        if self.tool_dict['per base n content']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['per base n content']),
                  file=self.output_file)

        # Printing function name
        print("\nPer base N content:\n")

        # Giving exact feedback on why what error was given

        print("N content higher than 5%", file=self.output_file)

        print("N content higher than 20%", file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("\nBiological/technical reason:\n"
              "- Big proportions of Ns is a general reason for lost of quality\n"
              "- It's possible that the last bin in this analysis could contain"
              " very few sequences"
              "", file=self.output_file)

    def sequence_duplication_levels(self):
        """
        Analysing the sequence duplication levels tool and giving feedback on that.
        """

        if self.tool_dict['sequence duplication levels']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['sequence duplication levels']),
                  file=self.output_file)

        # Printing function name
        print("\nSequence duplication levels:\n", file=self.output_file)

        # Giving exact feedback on why what error was given

        print("Non-unique sequences make up more than 20% of the total sequences.",
              file=self.output_file)

        print("Non-unique sequences make up more than 50% of the total sequences.",
              file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("\nBiological/technical reason:\n"
              "- A bad enriched library, this will generate duplicates\n"
              "- Duplicates may originate from PCR artefacts or biological duplicates\n "
              "which are natural collisions where different copies of exactly the same\n "
              "sequence are randomly selected.", file=self.output_file)

    def adapter_content(self):
        """
        Analysing the adapter content tool and giving feedback on that.
        """

        if self.tool_dict['adapter content']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['adapter content']),
                  file=self.output_file)

        # Giving exact feedback on why what error was given

        print("A sequence is present in more than 5% of all reads.",
              file=self.output_file)

        print("A sequence is present in more than 10% of all reads.",
              file=self.output_file)

        # Giving feedback on the biological/technical reason for the fail/warn
        print("\nBiological/technical reason:\n"
              "- A library where a reasonable proportion of the insert sizes are shorter\n"
              "than the read length", file=self.output_file)

    def kmer_content(self):
        """
        Analysing the kmer_content tool and giving feedback on that.
        """

        if self.tool_dict['kmer content']:
            print("\nFiles that failed or gave a warning: "
                  "", ", ".join(self.tool_dict['kmer content']),
                  file=self.output_file)

        print("\nKmer content:\n", file=self.output_file)

        print("A Kmer is imbalanced with a binomial p-value < 0.01",
              file=self.output_file)

        print("A Kmer is imbalanced with a binomial p-value < 10^-5",
              file=self.output_file)

        print("\nBiological/technical reason:\n"
              "Any individually overrepresented sequences, even if not present at a high\n "
              "enough threshold to trigger the overrepresented sequences module will cause\n "
              "the Kmers from those sequences to be highly enriched in "
              "this module", file=self.output_file)
