#!/usr/bin/python3

"""
This script identifies the organism
"""

__author__ = 'Carlo van Buiten'


def identify(organism):
    """
    :param organism: User input that designates the type of organism.
    :return: Directory names or, in the event of a mismatching organism code, returns None.
    """
    organisms = {"hs": ["Data/grch38/genome",     # Human
                        "Data/grch38/Homo_sapiens.GRCh38.92.gtf",
                        "Data/grch38/genome.fa"],

                 "mmu": ["Genome/HiSat2/Macaca_mulatta/genome",     # Macaque
                         "Genome/Macaca_mulatta.Mmul_8.0.1.92.gtf",
                         "Macaca_mulatta.Mmul_8.0.1.dna.toplevel.fa"],

                 "mm": ["Genome/HiSat2/Mus_musculus/GRCm38",        # Mouse
                        "Genome/Mus_musculus.GRCm38.92.gtf",
                        "Genome/Mus_musculus.GRCm38.dna_sm.primary_assembly.fa"],

                 "rn": ["Genome/HiSat2/Rattus_norvegicus/Rnor6.0",  # Rat
                        "Genome/Rattus_norvegicus.Rnor_6.0.93.gtf",
                        "Genome/Rattus_norvegicus.Rnor_6.0.dna_sm.toplevel.fa"],

                 "dr": ["Genome/HiSat2/Danio_rerio/GRCz11.93",      # Zebrafish
                        "Genome/Danio_rerio.GRCz11.93.gtf",
                        "Genome/Danio_rerio.GRCz11.93.dna_sm.primary_assembly.fa"]}

    if organism in organisms:
        return organisms[organism]

    print("Please make sure your chosen organism is one of the available types.")
    return None, None, None
