#!/usr/bin/python3

"""
Calculates severity scores for SNPs at a given position in a multi fasta protein alignment file.
"""

# Imports
import sys
import argparse
import numpy as np
import blosum as bl
import pandas as pd

__author__ = "Niek Scholten"


class SeverityCheckSNP:
    """
    Stores the data of a multiple sequence alignment multi fasta file.
    """
    def __init__(self, matrix=62):
        """
        Initializes the class variables.
        param matrix = Number of the BLOSUM matrix to use.
        """
        self.data = np.empty(0)
        self.matrix = bl.BLOSUM(matrix, 0)

    def __str__(self):
        """
        Returns the data if print() is called.
        """
        return self.data

    def load_file(self, filename: str):
        """
        Loads the file into a numpy array.
        param filename = Name of the file to load.
        """
        count = -1
        data = []
        with open(filename, encoding="UTF-8") as open_file:
            for line in open_file:
                if line.startswith(">"):
                    data.append([line.strip()])
                    count += 1
                else:
                    for char in line.strip():
                        data[count].append(char)

        self.data = np.array(data)

    def calculate_score(self, protein_colnum: int):
        """
        Calculates the severity score of a mutation at a given position in the sequence.
        param protein_colnum = Column number of the protein position to score.
        """
        protein_col = self.data.transpose()[protein_colnum:][0]
        max_score = max(self.matrix.values()) * (len(protein_col) * len(protein_col))
        min_score = min(self.matrix.values()) * (len(protein_col) * len(protein_col))
        max_points_factor = (abs(max_score) + abs(min_score)) / 10
        score = abs(min_score)

        for i in protein_col:
            for j in protein_col:
                if i == "-":
                    score += self.matrix[f"*{j}"]
                if j == "-":
                    score += self.matrix[f"{i}*"]
                score += self.matrix[f"{i}{j}"]

        score = score / max_points_factor

        return score, protein_col

    def calculate_all_scores(self):
        """
        Calculates all severity scores for each position in the multiple sequence alignment.
        """
        scores = ["Importance scores"]
        for item in range(len(self.data.transpose()[1:])):
            scores.append(self.calculate_score(item+1)[0])

        self.data = np.vstack([self.data, scores])
        return self.data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates severity scores for SNPs "
                                                 "at given positions of a "
                                                 "multiple sequence alignment.")
    parser.add_argument("file",
                        metavar="F",
                        type=str,
                        help="Path to the multiple sequence "
                             "alignment file to be loaded (MultiFasta only).")
    parser.add_argument("-p",
                        type=int,
                        metavar="Position",
                        help="Position for the SNP to trigger a mutation.")
    parser.add_argument("-matrix",
                        type=int,
                        default=62,
                        choices=[45, 50, 62, 80, 90],
                        help="BLOSUM matrix to use when calculating scores. "
                             "Options: 45,50,62,80 and 90."
                             "(Default: 62)")
    parser.add_argument("--all",
                        action='store_true',
                        help="Generates the scores for all positions "
                             "and prints them to the console with the data."
                             "(Default: False)")
    args = parser.parse_args()
    check = SeverityCheckSNP(args.matrix)
    check.load_file(args.file)
    if args.all:
        print(check.calculate_all_scores())
        store = input(f"Would you like to print these {len(check.data)}"
                      f" lines to a csv file? (yes or no): ")
        if store in ["yes", "y"]:
            file_to_store = input("Please enter a file path to output to: ")
            pd.DataFrame(check.data).to_csv(file_to_store)
        else:
            sys.exit(0)
    else:
        answer = check.calculate_score(args.p)
        print(f"The severity score for a mutation in protein "
              f"at position {args.p} is {answer[0]} out of 10.\n"
              f"The scored proteins are: {answer[1]} ('-' means a gap).")
