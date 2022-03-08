def read():
    global file
    global file_obj
    global uppercase
    file_type = input('Do you want the file to be seperated or uppercased?\nPlease select "S" or "U": ')
    if file_type.upper() == 'U':
        uppercase = True
    elif file_type.upper() == 'S':
        uppercase = False
    else: # Als het antwoord geen U of S is, nog een keer vragen
        read()
    file = input('Please specify the input file & extension: ')

def printer():
    global nucleotides
    global header
    section = ''    
    content = ''
    nucleotides = ''
    file_dict = dict()
    file_obj = open(file)

    for line in file_obj:
        if not line.startswith(' '): 
            line = line.strip()
            # Toevoegen aan de dictionary
            file_dict[section] = content
            X = True
            content = ''
            section = ''
            for char in line:
                if char == ' ': 
                    X = False
                if X == True:   
                    section += char # Schrijven van karakters naar de key
                if X == False:
                    if char != '\t':
                        content += char # Schrijven van karakters naar de value
        # Bij een spatie de zin automatisch toevoegen aan de value
        else:
            line = line.strip()
            content += line
    file_obj.close()

    # Alles uit ORIGIN naar een string schrijven als het niet in het filter voorkomt
    for char in file_dict['ORIGIN']:
        if char not in sequence_filter: 
            nucleotides += char

    # Header aanmaken
    header = (file_dict['VERSION'].strip() + ' ' + file_dict['DEFINITION'].strip())

def writer():
    global file_new_obj
    stop = ""
    start = ""
    subsection = ">"
    sequence_check = False
    dots = False

    file_obj = open(file)

    # Outputbestand aanmaken gebaseerd op de naam van het inputbestand
    file_new = file.split(".")[0] + "_features.txt"
    file_new_obj = open(file_new, "w")
    
    # Header aan het bestand toevoegen
    print(header + "\n", file = file_new_obj)

    
    for line in file_obj:
        if sequence_check == False:
            if line.startswith("FEATURES"):
                sequence_check = True
        else:
            if not line.startswith("ORIGIN"): 
                if line[5] not in sequence_filter: # Het 5e karakter checken in het filter
                    line = line.strip() 
                    for char in line:
                        if char not in sequence_filter: # Toevoegen aan de subsectie als het niet in het filter voorkomt
                            subsection += char
                        elif char in num and not dots: # Startpositie invullen als het een nummer is en als dots False is
                            start += char
                        elif char in num and dots: # Stoppositie invullen als het een nummer is en als dots True is
                            stop += char
                        elif char == ".": # Dots naar True zetten als een punt wordt gevonden
                            dots = True
                elif dots == True:
                    # Als dots True is de lijn bij de subsectie optellen
                    subsection += " " + line.strip()
                    file_new_obj.write(subsection)
                    file_new_obj.write("\n") 
                    if uppercase: # Als er voor uppercase is gekozen, uppercase_write aanroepen
                        uppercase_write(start, stop)
                    else: # Als er voor seperated is gekozen, sperated_write aanroepen
                        separated_write(start, stop)
                    
                    subsection = ">"
                    start = ""
                    stop = ""
                    dots = False
            else: # Bij het tegenkomen van ORIGIN de loop afbreken
                break
    print("Succesfully written to: ", file_new)
    file_new_obj.close()
    file_obj.close()

def separated_write(start, stop):
    count = 0 
    for char in range(int(start)-1, int(stop)):
        # Alle karakters tussen de start- en stoppositie wegschrijven
        file_new_obj.write(nucleotides[char])
        count += 1
        # Na 60 karakters een nieuwe regel beginnen
        if count == 60: 
            file_new_obj.write("\n")
            count = 0
    file_new_obj.write("\n\n") 

def uppercase_write(start, stop):
    count = 0 
    for char in range(0, int(stop)):
        if char >= int(start)-1: # Als het karakter meer is dan start,
            # De karakters binnen start en stop wegschrijven naar de file in hoofdletters
            file_new_obj.write(nucleotides[char].upper())
        else: # Zo niet, alles in kleine letters wegschrijven
            file_new_obj.write(nucleotides[char])
        count += 1 
        if count == 60:
            #  Op een nieuwe regel beginnen als er 60 karakters staan
            file_new_obj.write("\n")
            count = 0
    file_new_obj.write("\n\n")

# Aanmaken van lijsten met vaker gebruikte inhoud
sequence_filter = ["1","2","3","4","5","6","7","8","9","0"," ","\t","\n","/","."]
num = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
spaces = (" ", "\n", "\t", "/")

running = True
while running == True:
    read()
    printer()
    writer()
    
