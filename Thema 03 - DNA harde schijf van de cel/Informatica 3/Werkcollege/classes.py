import sys


class AminoAcid:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return 'Amino Acid [{} weight={}]'.format(self.name, self.weight)


aa1 = AminoAcid('Adenine', 123.45)
aa2 = AminoAcid('Glycine', 75.0)
print(aa1)
print(aa2)


class Nucleotide:
    valid_nucleotides = {'A', 'C', 'G', 'T'}

    def __init__(self, letter):
        if letter not in Nucleotide.valid_nucleotides:
            print('Error: illegal nucleotide!')
            sys.exit(0)
        else:
            self.letter = letter

    def __str__(self):
        return 'Nucleotide['+self.letter+']'


n = Nucleotide('A')
print(n)
n = Nucleotide('G')
print(n)


class Frequency:
    nucleotide_frequencies = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    def __init__(self, letter):
        Frequency.nucleotide_frequencies[letter] += 1


for nucleotide in 'AGAACTGACCCCGGGCA':
    n = Frequency(nucleotide)

for nucleotide in 'ATAGTCTGCATCTACA':
    o = Frequency(nucleotide)

print(Frequency.nucleotide_frequencies)
