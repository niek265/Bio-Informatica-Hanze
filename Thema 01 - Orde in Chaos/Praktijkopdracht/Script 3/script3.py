def io(): # vragen of de gebruiker 1 of meerdere files wil openen
    ask = input("Would you like to combine multiple files into 1 file? (yes, no): ")
    ask = ask.lower()
    if ask == "yes":
        multi()
    else:
        if ask == "no":
            single()
        else:
            print("Please enter 'yes' or 'no'")
            return io()

def single():
    all_char = "" # voor het opslaan van alle karakters met witregels
    counter = 0 # voor het plaatsen van een witregel bij elke 50 karakters
    input_file_name = input("Please enter the input file: ")
    input_file = open(input_file_name)
    output_file_name = input("Please enter a name for the output file: ")
    output_file = open(output_file_name, "w")
    for text in input_file:
        if text.startswith(">"):
            print(text, file=output_file)
        else:
            text = text.upper()
            text = text.strip()
            for char in text:                
                if counter == 50:
                    counter = 0
                    all_char += ("\n")
                else:                    
                    char = char.strip()
                    all_char += char
                    counter += 1
    printer(all_char, output_file, input_file, output_file_name)
    output_file.close()

def multi(): # openen van een output file, die tevens gebruikt wordt voor de rest van het programma
    output_file_name = input("Please specify an output file: ")
    output_file = open(output_file_name, "a")
    multi_in(output_file, output_file_name)

def multi_in(output_file, output_file_name):
    all_char = ""
    counter = 0
    ask_i = input("Please specify the file to import: ")
    input_file = open(ask_i)
    for text in input_file:
        if text.startswith(">"):
            print("\n", text, file=output_file)
        else:
            text = text.upper()
            text = text.strip()
            for char in text:                
                if counter == 50:
                    counter = 0
                    all_char += ("\n")
                else:                    
                    char = char.strip()
                    all_char += char
                    counter += 1    
    printer(all_char, output_file, input_file, output_file_name)
    more(output_file, output_file_name)
    
def more(output_file, output_file_name): # vragen of er nog meer bestanden moeten worden toegevoegd
    ask_more = input("Would you like to import another file? (yes, no): ")
    ask_more = ask_more.lower()
    if ask_more == "yes":
        multi_in(output_file, output_file_name)
    else:
        if ask_more == "no":
            print("Goodbye!")
            output_file.close()
            pass
        else:
            print("Please enter 'yes' of 'no'")
            return more(output_file, output_file_name)
            
def printer(all_char, output_file, input_file, output_file_name): # hier wordt telkens de string met karakters heengestuurd, om vervolgens in een bestand geplaatst te worden              
    print(all_char, file=output_file)
    print("Saved to file", output_file_name)
    input_file.close() 

io()
