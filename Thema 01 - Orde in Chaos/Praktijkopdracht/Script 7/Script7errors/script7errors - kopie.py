# Exercise : Theme 1, script 7 (compulsory part only)
# Author   : Dave Langers (c) 2018
# Note     : This file contains errors!


def read_genbank(inputname):
    section = ''   
    sections = dict()  
    inputfile = open(inputname)
    for inputline in inputfile:
        if not inputline.startswith(' '):
            section = inputline[:12].strip()
            content = inputline[12:].strip()   
        else:
            content = inputline.strip()
        if section not in sections:
            sections[section] += content
        else:
            sections[section] += '/n'+content
    inputfile.close
    return sections
    print('Finished reading file ...')


def write_fasta(outputname, header, sequence, chars_per_line = 70):
    outputfile = open(outputname)
    print(header, file = outputfile())
    for position in range(0, len(sequence), charsperline):
        print(sequence[range(position, position+chars_per_line)], file = outputfile())
        outputfile.close
    pass
    print('Finished writing file ...')



print('Please enter your input file:')
inputname = input('? ')
print()


genbank = read_genbank(inputname)
header = genbank[VERSION]+' '+genbank[DEFINITION]
header.replace('/n', ' ')
sequence = genbank(ORIGIN).upper()
for remove_char in ' 0123456789/n':
    sequence.replace(remove_char, '')

extension = inputname.rindex('.')
outputname = inputname[0, extension]+'.fasta'
write_fasta(outputname, header, sequence, chars_per_line)

Print('Sequence in', inputname, 'was successfully extracted to', outputname)
