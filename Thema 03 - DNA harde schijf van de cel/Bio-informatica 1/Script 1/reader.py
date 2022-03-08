# hierdoor vraagt hij om de filename, die hij vervolgens opent
text = input("Please provide the file name and extension of file 1 : ")
file_name1 = text

# deze zijn gebruikt voor het snel copy-pasten van de namen van de datasets
# rna_sequence_cftr.fasta
# dna_sequence_cftr.fasta
# dna_sequence_brca1.fasta
# rna_sequence_brca1.fasta

# het definiëren van "character"
character1 = 0

# hier wordt de file geopend
file_object1 = open(file_name1)

# hier wordt de text getest op headers, als die er zijn worden ze niet meegeteld
for line in file_object1:
    if line.startswith(">"):
        None
    else:
        line = line.strip()
        print(line)
        character1 += len(line)
# het laten zien van het aantal karakters
print("The total amount of characters is:", character1)

# sluiten
file_object1.close()

print()

askformore = input("Would you to like to open another file?: ")
answer = askformore
if answer == "Yes":
    text2 = input("Please provide the file name and extension of the file: ")
    file_name2 = text2
    file_object2 = open(file_name2)

    for line in file_object2:
        if line.startswith(">"):
            None
        else:
            line = line.strip()
            print(line)
            character2 += len(line)
# het laten zien van het aantal karakters
    print("The total amount of characters is:", character2)

    file_object2.close()
