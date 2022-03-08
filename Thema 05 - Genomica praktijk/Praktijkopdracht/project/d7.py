#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for getting gene names from input data.

Usage: 'd7.py'
"""

import sys
import re

__author__ = 'Niek Scholten, Rienk Heins'
__version__ = '1.0.0'
__email__ = 'n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl'
__status__ = 'Finished'


def get_gene_name(gene_name):
    """
    Searches for gene names.
    :param gene_name: Dictionary containing the gene info.
    :return: Gene name.
    """
    gene = []
    pattern = re.compile(r'[A-Z0-9,]{3,}')
    genes = gene_name.split(',')
    for gen in genes:
        matches = pattern.findall(gen)
        for match in matches:
            if match.startswith(("NONE", "LOC", "LIN")) or re.match(r'\d', match):
                pass
            else:
                gene.append(match)
    if gene == []:
        gene = "-"
    else:
        gene = "/".join(gene)
    return gene

def main():
    """ Main function """

    # Input
    refseq_genes = [
        'TNNI3(NM_000363:exon5:c.371+2T>A)',
        'TSHZ3(dist=65732),THEG5(dist=173173)',
        'ACTR3BP2(dist=138949),NONE(dist=NONE)',
        'BIN1(dist=32600),CYP27C1(dist=43909)',
        'LOC101927282(dist=1978702),LOC101927305(dist=14658)',
        'NBPF10,NBPF20',
        'ERBB4',
        'LOC100507291',
        'NONE'
    ]

    # Output
    genes = [
        'TNNI3',
        'TSHZ3/THEG5',
        'ACTR3BP2',
        'BIN1/CYP27C1',
        '-',
        'NBPF10/NBPF20',
        'ERBB4',
        '-',
        '-'
    ]
    # Process the ANNOVAR-file
    fail = 0
    for i, refseq_gene in enumerate(refseq_genes):
        filtered_gene = get_gene_name(refseq_gene)
        print("Input RefSeq_Gene: '", refseq_gene, "', Filtered gene name: '",
              filtered_gene, "'", sep='')
        if filtered_gene != genes[i]:
            print("\tUnfortunately, '", filtered_gene,
                  "' (your output) is different from the expected output ('",
                  genes[i], "').\n", sep='')
            fail = 1
        else:
            print('\tWell done! The gene name is correct.')

    if fail == 1:
        print('\nNot all genes are filtered correctly, please review',
              'the list above and try again.')
    return 0


if __name__ == "__main__":
    sys.exit(main())
