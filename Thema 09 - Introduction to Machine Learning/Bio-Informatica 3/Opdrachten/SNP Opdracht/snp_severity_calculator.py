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
        self.data = np.empty(0)  # Temporary empty array
        self.matrix = bl.BLOSUM(matrix, 0)  # Initialize a scoring matrix

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
        count = -1  # Initialize at -1, so it won't interfere in else
        data = []  # Initialize empty list
        with open(filename, encoding="UTF-8") as open_file:
            for line in open_file:
                if line.startswith(">"):  # If the line is a header, add it to element 1
                    data.append([line.strip()])
                    count += 1
                else:  # If it is not a header, add it to the rest of the elements
                    for char in line.strip():
                        data[count].append(char)

        self.data = np.array(data)  # Convert list to an array

    def calculate_score(self, protein_colnum: int, new_protein: str = ""):
        """
        Calculates the severity score of a mutation at a given position in the sequence.
        param protein_colnum = Column number of the protein position to score.
        """

        protein_col = self.data.transpose()[protein_colnum:][0]  # Flip the array for looping

        if f"{new_protein.upper()}*" in self.matrix.keys():
            # Calculate maximum and minimum score for determining grades
            max_score = max(self.matrix.values()) * len(protein_col) + 1
            min_score = min(self.matrix.values()) * len(protein_col) + 1

            # Calculate the total score possible and create a division number
            max_points_factor = (abs(max_score) + abs(min_score)) / 10
            score = abs(min_score)  # Set the base score to the "zero" point of the scale

            for i in protein_col:
                if i == "-":  # If it is a gap, use the gap symbol from the matrix
                    score += self.matrix[f"*{new_protein}"]
                # Add the number from the matrix to the score
                score += self.matrix[f"{i}{new_protein}"]

            # Divide the score by the factor based on the maximum possible score
            score /= max_points_factor
            # Return the score and the column for output
            return 10-score, protein_col

        elif new_protein == "":
            # Calculate maximum and minimum score for determining grades
            max_score = max(self.matrix.values()) * (len(protein_col) * len(protein_col))
            min_score = min(self.matrix.values()) * (len(protein_col) * len(protein_col))

            # Calculate the total score possible and create a division number
            max_points_factor = (abs(max_score) + abs(min_score)) / 10
            score = abs(min_score)  # Set the base score to the "zero" point of the scale

            for i in protein_col:  # Loop 1
                for j in protein_col:  # Loop 2, so each element is compared to one another
                    if i == "-":  # If it is a gap, use the gap symbol from the matrix
                        score += self.matrix[f"*{j}"]
                    if j == "-":
                        score += self.matrix[f"{i}*"]
                    # Add the number from the matrix to the score
                    score += self.matrix[f"{i}{j}"]

            # Divide the score by the factor based on the maximum possible score
            score /= max_points_factor

            # Return the score and the column for output
            return score, protein_col
        else:
            raise SyntaxError("Input is not correct, please check '--help' for info")

    def calculate_all_scores(self):
        """
        Calculates all severity scores for each position in the multiple sequence alignment.
        """
        scores = ["Importance scores"]  # Initialize the list with first element
        for item in range(len(self.data.transpose()[1:])):
            # Calculate and append scores to list
            scores.append(self.calculate_score(item+1)[0])

        self.data = np.vstack([self.data, scores])  # Stack the new list underneath the data array
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
    args = parser.parse_args()  # Parse arguments from commandline
    check = SeverityCheckSNP(args.matrix)  # Initialize object with possible matrix
    check.load_file(args.file)  # Load given file into the object
    if args.all:  # If "--all" is picked, calculate all scores
        print(check.calculate_all_scores())
        store = input(f"Would you like to print these {len(check.data)}"
                      f" lines to a csv file? (yes or no): ")
        if store in ["yes", "y"]:
            file_to_store = input("Please enter a file path to output to: ")
            # Convert the file to csv data and save it to given path
            pd.DataFrame(check.data).to_csv(file_to_store)
        else:
            # Exit program if "no" is picked
            sys.exit(0)
    elif args.p is None:
        raise SyntaxError("No position specified, please use '-p' or '--all'")
    else:
        answer = check.calculate_score(args.p)
        #  Print severity score in an orderly fashion
        print(f"The severity score for a mutation in protein "
              f"at position {args.p} is {answer[0]} out of 10.\n"
              f"The scored proteins are: {answer[1]} ('-' means a gap).")
        new_char = input("Please select a protein to compare to this set: (type anything else to exit)\n")
        while f"{new_char.upper()}*" in check.matrix.keys():
            new_answer = check.calculate_score(args.p, new_char)
            print(f"The severity score for a mutation to protein {new_char.upper()} "
                  f"at position {args.p} is {new_answer[0]} out of 10.\n"
                  f"The scored proteins are: {new_answer[1]} ('-' means a gap).")
            new_char = input("Please select a protein to compare to this set: (type anything else to exit)\n")
        sys.exit(0)
