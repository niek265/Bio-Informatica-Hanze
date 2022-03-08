def ask():
    text = input("please provide file name here: ")
    file_name = text

    file_object = open(file_name)
    characters = 0

    for line in file_object:
            if line.startswith(">"):
                None
            else:
                line = line.strip()
                characters += len(line)
                print(line)
    print("The total amount of characters is: ",characters)
    file_object.close()
    again()

def again():
    answer = input("would you like to run another file? answer 'yes' or 'no': ")
    if answer == "yes":
        return ask()
    elif answer == "no":
            print("Enjoy the rest of your day")
    else:
        print("Only enter yes or no please")
        return again()

ask()


# snel copy-pasten voor testen
# dna_sequence_cftr.fasta
# rna_sequence_cftr.fasta
# rna_sequence_nba.fasta
# dna_sequence_nba.fasta
