# het definiëren van ask
# de functie vraagt eerst om een filename, die vervolgens geopend wordt
# hij test of er een header is, zo ja dan telt hij deze niet mee in het totaal aantal tekens

def ask():
    text = input("Please provide the file name and extension: ")
    character = 0
    print("Opening ",text)
    file_object = open(text)
    for line in file_object:
        if line.startswith(">"):
            None
        else:
            line = line.strip()
            print(line)
            character += len(line)
    print("The total amount of characters is:", character)
    another()

# onderstaande functie wordt gebruikt om te vragen of de gebruiker nog een bestand wil openen
# answer wordt automatisch in lowercase gezet, zodat hoofdletters niet uitmaken in het antwoord
# zo ja, dan roept hij opnieuw de ask() functie aan
# zo nee, dan sluit hij af met een berichtje
# als iets anders dan 'ja' of 'nee' wordt ingevuld dan geeft hij dat weer en wordt opnieuw another() aangeroepen

def another():    
    answer = input("Would you to like to open another file? (yes, no): ")
    answer = answer.lower()
    if  answer == "yes":
        return ask()  
    else:
        if answer == "no":
            print("Understandable, have a nice day!")
        else:
            print("Please enter 'yes' or 'no'")
            return another()

ask()

# deze zijn gebruikt voor het snel copy-pasten van de namen van de datasets
# rna_sequence_cftr.fasta
# dna_sequence_cftr.fasta
# dna_sequence_brca1.fasta
# rna_sequence_brca1.fasta
