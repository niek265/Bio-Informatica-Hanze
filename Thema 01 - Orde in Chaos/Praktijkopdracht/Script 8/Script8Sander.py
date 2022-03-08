# 
def separated_write(start,stop,nucleotides):
    count = 0
    for char in range(int(start)-1, int(stop)):
        file_new_obj.write(nucleotides[char])
        count += 1
        if count == 60:
            file_new_obj.write("\n")
            count = 0
        file_new_obj.write("\n\n")

def uppercase_write(start,stop,nucleotides):
    count = 0
    for char in range(0, int(stop)):
        if char >= int(start)-1:
            file_new_obj.write(nucleotides[char].upper())
        else:
            file_new_obj.write(nucleotides[char])
        count += 1
        if count == 60:
            file_new_obj.write("\n")
            count = 0
    file_new_obj.write("\n\n")


def read():
    global file
    global file_obj
    global uppercase
    # Inlezen bestand
    file = input("please enter your input file here: ")
    file_type = input("Please specify wether you want uppercased or seperated: ")
    if file_type == "u":
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

    file_obj.close()
    
    
def writer():
    global file_new_obj
    
    cijfer = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    spatie = (" ", "\n", "\t", "/")
    stop = ""
    start = ""
    subsection = ">"
    sequence_filter = ["1","2","3","4","5","6","7","8","9","0"," ","\t","\n","/","."]
    X = False
    dots = False
    file_obj = open(file)

    file_new = file.split(".")[0] + "_features.fasta"
    file_new_obj = open(file_new, "w")
    print(header + "\n", file = file_new_obj)

    for line in file_obj:
        if X == False:
            if line.startswith("FEATURES"):
                X = True
        else:
            if not line.startswith("ORIGIN"):
                if line[5] not in sequence_filter:
                    line = line.strip()
                    for char in line:
                        if char not in sequence_filter:
                            subsection += char
                        elif char in cijfer and not dots:
                            start += char
                        elif char in cijfer and dots:
                            stop += char
                        elif char == ".":
                            dots = True
                elif dots == True:
                    subsection += " " + line.strip()
                    file_new_obj.write(subsection)
                    file_new_obj.write("\n")
                    if uppercase:
                        uppercase_write(start, stop, nucleotides)
                    else:
                        separated_write(start, stop, nucleotides)
                    subsection = ">"
                    start = ""
                    stop = ""
                    dots = False
            else:
                break
    
    file_new_obj.close()
    file_obj.close()


running = True
while running == True:
    read()
    printer()
    writer()
