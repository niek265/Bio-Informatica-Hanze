# Aanmaken functie voor het verschil maken in uppercased en lowercased
def separated_write(start,stop,nucleotides):
    count = 0 # Aanmaken counter
    for char in range(int(start)-1, int(stop)): # voor karakter in de range van aangegeven begin tot eind optellen en de nucleotide naar het bestand schrijven bij de bijbehorende subsectie
        file_new_obj.write(nucleotides[char])
        count += 1
        if count == 60: # Wanneer de counter 60 is een regel overslaan en de count naar 0 zetten
            file_new_obj.write("\n")
            count = 0
        file_new_obj.write("\n\n") # witregels toevoegen voor volgende subsectie

# Aanmaken functie voor hoofdletters
def uppercase_write(start,stop,nucleotides):
    count = 0 # Aanmaken counter
    for char in range(0, int(stop)): # per karakters bijlangs gaan vanaf het begin van de aangegeven start en stop plekken van de nucleotides 
        if char >= int(start)-1: # Wanneer het karakter meer is dan de startplek de nucleotides in hoofdletters wegschrijven
            file_new_obj.write(nucleotides[char].upper())
        else: # Anders de nucleotides in lowercase schrijven
            file_new_obj.write(nucleotides[char])
        count += 1 # Count met 1 ophogen
        if count == 60: # Wanneer de counter 60 is een regel overslaan en de count naar 0 zetten
            file_new_obj.write("\n")
            count = 0
    file_new_obj.write("\n\n") # witregels toevoegen voor volgende subsectie

# Aanmaken van fucntie read() om het bestand in te lezen
def read():
    # Globaal maken van de verscheidene inputs
    global file
    global file_obj
    global uppercase
    # Inlezen bestand
    file = input("please enter your input file here: ")
    file_type = input("Please specify wether you want uppercased or seperated: ")
    if file_type.upper() == "U":
        uppercase = True
    else:
        uppercase = False
    
def printer():
    global nucleotides
    global header
    # Maken header en printen
    sectie = ""
    my_dict = dict()
    info = ""
    nucleotides = ""
    # Dictionaries voor bij de nucleotide sequentie
    cijfer = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    spatie = (" ", "\n", "\t", "/")
    sequence_filter = ["1","2","3","4","5","6","7","8","9","0"," ","\t","\n","/","."]
    file_obj = open(file)

    for line in file_obj:
        if not line.startswith(" "): # Wanneer lijn niet strat met een spatie de lijn bij langs gaan
            line = line.strip() # Lijn netjes maken
            # Dictionary aanmaken
            my_dict[sectie] = info

            # Aanmaken variabelen
            X = True
            info = ""
            sectie = ""
            for char in line:
                if char == " ": # Als het karakter een spatie is X naar False zetten
                    X = False
                if X == True:   # Wanneer X True is het karakter toevoegen aan de key (sectie}
                    sectie += char
                if X == False:  # Wanneer X False is het karakter toevoegen aan de value van de desbetreffende key 
                    if char != "\t":
                        info += char
        # Wanneer er een spatie is aan het begin van de zin, de zin toevoegen aan de value van de key waar de zin als laatst is geweest 
        else:
            line = line.strip()
            info += line

    # header maken printen
    header = (my_dict["VERSION"].strip() + " " + my_dict["DEFINITION"].strip())
    
    for char in my_dict["ORIGIN"]:
        if char not in sequence_filter: 
            nucleotides += char
    # sluiten van de file
    file_obj.close()

# Aanmaken functie writer om alles weg te schrijven naar een zelf gemaakt bestand
def writer():
    global file_new_obj
    # Aanmaken variabelen
    cijfer = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    spatie = (" ", "\n", "\t", "/")
    stop = ""
    start = ""
    subsection = ">"
    sequence_filter = ["1","2","3","4","5","6","7","8","9","0"," ","\t","\n","/","."]

    # Twee booleans aanmaken voor de volgende for loop
    sequence_check = False
    dots = False

    file_obj = open(file)

    # Nieuwe file aanmaken om naar te writen
    file_new = file.split(".")[0] + "_features.txt"
    file_new_obj = open(file_new, "w")

    # Printen van de header
    print(header + "\n", file = file_new_obj)

    
    for line in file_obj:
        if sequence_check == False:
            if line.startswith("FEATURES"): # Checken of de lijn met FEATURES begint
                sequence_check = True # Check naar True zetten
        else:
            if not line.startswith("ORIGIN"): # Wanneer de lijn niet start met ORIGIN defor loop bij langs gaan
                if line[5] not in sequence_filter:  # Als de vijfde letter niet in het filter zit de lijn bijlangsgaan
                    line = line.strip() # lijn schoonmaken
                    for char in line:
                        if char not in sequence_filter: # Wanneer het karakter niet in het filter zit deze bij de subsectie opschrijven
                            subsection += char
                        elif char in cijfer and not dots: # Als het karakter in cijfers zit en dots niet waar is deze bij deze als start plek optellen
                            start += char
                        elif char in cijfer and dots: # Als het karakter in cijfers zit en dots waar is deze bij het eindgetal optelt
                            stop += char
                        elif char == ".": # Wanneer er een "." word tegengekomen dots naar True zetten
                            dots = True
                elif dots == True: # Wanneer dots True is de volgende lijn bij subsection optellen
                    subsection += " " + line.strip()
                    file_new_obj.write(subsection)# De subsectie naar het bestand toeschrijven
                    file_new_obj.write("\n") # Een witregel toevoegen aan het bestand
                    if uppercase: # Wanneer er uppercase is ingevuld de functie uppercase gebruiken
                        uppercase_write(start, stop, nucleotides)
                    else: # Als er iets anders is ingevuld dan uppercase de seperated functie gebruiken
                        separated_write(start, stop, nucleotides)
                    # Variabelen terugzetten naar de originele inhoud
                    subsection = ">"
                    start = ""
                    stop = ""
                    dots = False
            else: # Wanneer de lijn wel met irigin start de loop afsluiten
                break
    print("Your file has been written to file: ", file_new)
    # Sluiten van alle files
    file_new_obj.close()
    file_obj.close()


def again():
    global running
    
    # Vragen of er nog een bestand moet worden ingelezen
    answer = input("Would you like to add another file? answer 'yes' or 'no': ")
    # Wanneer antwoord "ja" is nogmaals While loop uitvoeren
    if answer.lower() == "yes":
        running = True
    # Wanneer antwoord "no" is het programma afsluiten
    elif answer.lower() == "no":
        running = False
        print("Enjoy the rest of your day.")
    # Aangeven dat alleen ja of nee kan worden ingevuld en terugkeren naar begin van de functie
    else:
        print("I would prefer if you only used yes or no.")
        return again()


# While loop om alles af te spelen
running = True
while running == True:
    read()
    printer()
    writer()
    again()
