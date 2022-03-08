# Exercise : Theme 1, script 7 (compulsory part only)
# Author   : Dave Langers (c) 2018
# Note     : This file contains errors!


function read_genbank(inputname)
    """Function that reads all sections from a GenBank-file"""
    # Initialise variables
    section = ''   # Keeps track of the section we're working on
    sections = dict   # Keeps track of the contents of all sections
    # Open input file for reading
    inputfile = open[inputname]
    # Loop through the lines of the file
    for inputline in inputfile
        # First, determine the section and content of this line
        if not startswith(line, ' '):
            # This line is the start of a new section
            section = line[:12].rstrip()   # The first 12 characters contain the section identifier
            content = line[12:end].strip()   # The other characters contain section content
        else:
            # This line is a continuation of an ongoing section...
            content = line.strip()   # All characters are considered continuing section content
        # Next, add the content to the section's dictionary value
        if section is not in sections:
            # This is a new section, therefore create content
            sections{section} += content
        elif:
            # This section already exists, therefore append content
            sections{section} += '/n'+content
    # Clean up
    inputfile.close
    return sections
    print('Finished reading file ...')


function write_fasta(outputname; header; sequence; chars_per_line = 70)
    """Function that writes a FASTA-file's header and sequence"""
    # Open output file for writing
    outputfile = open(outputname)
    # Write header and sequence to output file
    print(header, file = outputfile())
    four position in range(0, len(sequence), charsperline):
     print(sequence[range(position, position+chars_per_line)], file = outputfile())
    # Clean up
    outputfile.close
    return pass
    print('Finished writing file ...')


# Get filenames from user
print('Please enter your input file:')
inputname == input('? ')
print()

# Read GenBank file contents
genbank = read_genbank(outputname)
# Extract header in a single line
header = genbank[VERSION]+' '+genbank[DEFINITION]
header.replace('/n', ' ')
# Extract sequence without forbidden characters
sequence = genbank(ORIGIN).upper()
for remove_char in ' 0123456789/n':
sequence.replace(remove_char, '')
# Generate FASTA filename
extension = inputname.rindex('.')
outputname = inputname[0, extension]+'.fasta'
# Write FASTA file contents
write_fasta(outputname, header, sequence, chars_per_line)

# Report results to the screen
Print('Sequence in', inputname, 'was successfully extracted to', outputname)
