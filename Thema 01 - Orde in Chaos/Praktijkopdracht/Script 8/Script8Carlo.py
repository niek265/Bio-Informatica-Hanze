#Als de gebruiker voor het separated formaat kiest, schrijft deze functie de nucleotiden per subsection naar het bestand
def separated_write(start,stop,nucleotides):
    count = 0
    for character in range(int(start)-1, int(stop)):
        new_file.write(nucleotides[character])
        count += 1
        if count == 60:
            new_file.write("\n")
            count = 0
    new_file.write("\n\n")

#Als de gebruiker voor het uppercase formaat kiest, schrijft deze functie de nucleotiden per subsection naar het bestand
def uppercase_write(start,stop,nucleotides):
    count = 0
    for character in range(0, int(stop)):
        if character >= int(start)-1:
            new_file.write(nucleotides[character].upper())
        else:
            new_file.write(nucleotides[character])
        count += 1
        if count == 60:
            new_file.write("\n")
            count = 0
    new_file.write("\n\n")
    

sequence_filter = ["1","2","3","4","5","6","7","8","9","0"," ","\t","\n","/","."]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

file_name = input("Enter a GENBANK file: ")
global file_object
file_object = open(file_name)

file_format = input("Would you like the separated or uppercased format? ")
if file_format[0].upper() == "U": #Elk antwoord dat begint met een U leidt tot het kiezen van het uppercase formaat
    uppercase = True
else:
    uppercase = False
    
section = "" #Secties in het GENBANK bestand
content = "" #Alles wat na een section komt in het GENBANK bestand
start = ""
stop = ""
dictionary = {}

#Zet alles uit de GENBANK file in een dictionary, sections zijn de keys, content is de value
for line in file_object:
    if line[0] not in [" ","\t","\n","/"]:  #Als dit waar is, zit je op een regel die begint met een sectionnaam
        sectioncheck = True
        #Als je hier aan het begin van een nieuwe section staat, maak hij een dictionary entry van de vorige section
        if len(section) != 0:
            dictionary[section] = content
            section = ""
            content = ""
        for character in line:
            #Deze if/else maakt onderscheid tussen een sectionnaam en content dat op dezelfde regel staat
            if character not in [" ","\t","\n","/"] and sectioncheck:   
                section += character
            else:
                content += character
                sectioncheck = False
    else:
        content += line  #Voegt content toe dat niet op dezelfde regel als de sectionnaam zit

#Maakt de laatste dictionary entry
if len(section) != 0:
    dictionary[section] = content
file_object.close()

new_file_name = file_name.split(".")[0] + "_features.txt" #Maakt de naam voor de txt versie van het ingevoerde GENBANK bestand
global new_file
new_file = open(new_file_name, "w")

#Schrijft de definition naar het txt bestand
definition = dictionary["DEFINITION"].split()
for item in definition:
    if item != "":
        new_file.write(item)
        new_file.write(" ")
new_file.write("\n\n")


#Schrijft alle nucleotiden naar een string
nucleotides = ""
for character in dictionary["ORIGIN"]:
    if character not in sequence_filter:  #Filtert getallen, spaties, tabs, enters en / eruit
        nucleotides += character

file_object = open(file_name) #Het GENBANK bestand wordt hier opnieuw geopend om zo line voor line doort FEATURES heen te kunnen lopen
sectioncheck = False #Sectioncheck checkt nu of je al in de FEATURES section zit
subsection = ">"
dots = False #Geeft aan of je voorbij de puntjes bent die tussen het start en het stopgetal zitten

#Schrijft alles (op de definition na) naar het nieuwe .txt bestand
for line in file_object:
    if sectioncheck == False:
        if line.startswith("FEATURES"):
            sectioncheck = True
    else:
        if not line.startswith("ORIGIN"):
            if line[5] not in sequence_filter: #Als er op line[5] een letter staat betekent dat dat er een subsection is
                for character in line:
                    if character not in sequence_filter: #Maakt een string van de naam van de subsection
                        subsection += character
                    elif character in numbers and not dots: #Definieert het startgetal
                        start += character
                    elif character in numbers and dots: #Definieert het stopgetal
                        stop += character
                    elif character == ".":
                        dots = True
            elif dots == True: #De eerstvolgende line na de line met de het start en het stopgetal hoort ook nog bij de header van een subsection
                subsection += " " + line.strip()
                new_file.write(subsection)
                new_file.write("\n")
                #Schrijft alle nucleotiden per subsection
                if uppercase:
                    uppercase_write(start, stop, nucleotides)
                else:
                    separated_write(start, stop, nucleotides)
                subsection = ">"
                start = ""
                stop = ""
                dots = False #Aangezien we nu op zoek zijn naar een nieuwe subsection zijn we nog niet voorbij de puntjes/dots geweest
        else:
            break
               
file_object.close()
new_file.close()
