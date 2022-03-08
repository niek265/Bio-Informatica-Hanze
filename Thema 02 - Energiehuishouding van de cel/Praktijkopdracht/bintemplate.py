#!/usr/bin/env python3

"""
File met dictionaries
"""

__author__ = "Gijs Bakker, Niek Scholten"

AMINOTOTRIPLET = {"A": "GCC", "R": "AGA", "N": "AAT", "D": "GAT", "C": "TGC",
                  "Q": "CAG", "E": "GAA", "G": "GGA", "H": "CAC", "I": "ATT",
                  "M": "ATG", "L": "CTG", "K": "AAA", "F": "TTT", "P": "CCA",
                  "S": "TCT", "T": "ACA", "W": "TGG", "Y": "TAT", "V": "GTG",
                  "STOP": "TGA", "\n": ""}


TRIPLETTOAMINO = {"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                  "UGU": "C", "UGC": "C",
                  "GAU": "D", "GAC": "D",
                  "GAA": "E", "GAG": "E",
                  "UUU": "F", "UUC": "F",
                  "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "R",
                  "CAU": "H", "CAC": "H",
                  "AUU": "I", "AUC": "I", "AUA": "I",
                  "AAA": "K", "AAG": "K",
                  "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                  "AUG": "M",
                  "AAU": "N", "AAC": "N",
                  "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                  "CAA": "Q", "CAG": "Q",
                  "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
                  "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
                  "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                  "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                  "UAU": "Y", "UAC": "Y",
                  "UAA": "#", "UAG": "#", "UGA": "#",
                  "UGG": "W"}
