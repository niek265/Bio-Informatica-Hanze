#!/usr/bin/env python3

"""
This module can be used to extract information from FASTQ files
and create a visual representation of the information contained within the file.
"""

from io import BytesIO
import base64
import matplotlib.pyplot as plt

__author__ = 'Niek Scholten'


class FQProcessor:
    """
    Used to create a collection of information from the input file
    """
    def __init__(self, file):

        self.all_lines = []
        self.quality_lines = []
        self.values = []
        self.file_enc = file.read()
        self.file = self.file_enc.decode('UTF-8')  # Decodes the given file
        self.table = {'!': 0, '"': 1, '#': 2, '$': 3, '%': 4,
                      '&': 5, "'": 6, '(': 7, ')': 8, '*': 9,
                      '+': 10, ',': 11, '-': 12, '.': 13, '/': 14,
                      '0': 15, '1': 16, '2': 17, '3': 18, '4': 19,
                      '5': 20, '6': 21, '7': 22, '8': 23, '9': 24,
                      ':': 25, ';': 26, '<': 27, '=': 28, '>': 29,
                      '?': 30, '@': 31, 'A': 32, 'B': 33, 'C': 34,
                      'D': 35, 'E': 36, 'F': 37, 'G': 38, 'H': 39,
                      'I': 40}  # Contains the translations of the q-scores

    def read_file(self):
        """
        Sorts all lines and extracts the lines that can be used
        """
        line = ''
        counter = 0
        for char in self.file:  # Splits the characters on line breaks
            if not char == '\n':
                line += char
            else:
                self.all_lines.append(line)
                line = ''
        for line in self.all_lines:  # Sorts the usable lines
            if counter == 3:
                self.quality_lines.append(line)
                counter = 0
            else:
                counter += 1

    def get_quality(self):
        """
        Converts the given values to the correct q-scores
        and creates the correct format for the graph
        """
        values = [[self.table[char] for char in line] for line in self.quality_lines]
        value_sequence = [[] for n in range(len(values[0]))]

        for i in range(len(values)):  # Sorts the values in the right order
            for j in range(len(values[i])):
                value_sequence[j].append(values[i][j])

        self.values = value_sequence
        return self.values

    def create_graph(self):
        """
        Creates the figure and the boxplots within.
        """
        plt.figure(figsize=(len(self.values)/4, 5), dpi=150)  # Creates a figure

        boxplot = plt.boxplot(self.values, showfliers=False, widths=0.6, patch_artist=True)

        plt.xlabel('Position')
        plt.ylabel('Q-Score')
        plt.title('Quality scores per base')

        fill_color = [0, 0.90, 0.46]  # Colors the boxes

        plt.setp(boxplot['medians'], color=[0.988, 0.945, 0.890])

        for box in boxplot['boxes']:
            box.set(facecolor=fill_color, linewidth=2)

        figfile = BytesIO()
        plt.savefig(figfile, format='svg')  # Exports the figure to a temporary file
        figfile.seek(0)
        website_png = base64.b64encode(figfile.getvalue()).decode('ascii')

        return website_png
