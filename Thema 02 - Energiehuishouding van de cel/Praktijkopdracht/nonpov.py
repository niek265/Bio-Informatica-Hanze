#!/usr/bin/env python3

"""
Voor de functies van main.py die geen povray nodig hebben
"""

__author__ = 'Gijs Bakker, Niek Scholten'


def read_fasta(file_naam):
    """Leest een fasta bestnad in en slaat de nucleotiden op in een string
    Args: file_naam: de naam van de fasta file waar de nucleotiden uit gehaald moeten worden.
    Return: Een string van nucleotiden."""
    file_obj = open(file_naam)
    nucleotiden = ''
    for line in file_obj:
        if line[0] != '>':
            line.strip()
            nucleotiden += line

    file_obj.close()
    return nucleotiden


def triplet_maker(nucleo_string):
    """Haalt uit een string van nucleotiden de tripletten en
    slaat deze strings van tripletten op in een list.
    Args: nucleo_string: een string van nucleotiden
    Return: een list van strings van tripletten."""
    count = 0
    tripletten = []
    triplet = ''
    for nucleotide in nucleo_string:
        if nucleotide != "\n":
            triplet += nucleotide
            count += 1
            if count == 3:
                count = 0
                tripletten.append(triplet)
                triplet = ''

    return tripletten
