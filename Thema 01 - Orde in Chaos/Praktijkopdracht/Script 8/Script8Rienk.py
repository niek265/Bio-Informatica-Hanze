file_name = input("Voer GENBANK bestand in \n")
file_object = open(file_name)

#hier wordt een check gemaakt voor het programma of de output file uppercased of seperated moet zijn
HL_check = False
HL_input = input("uppercased of seperated \n")
if HL_input == "uppercased":
    HL_check = True

#lijsten om de lines te checken op getallen en witregels
getallen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
wit_regels = [" ", "\n", "\t"]

sectie = ""
inhoud = ""
nucleotiden = ""
my_dict = {}

#eerst wordt er een dictionary aangemaakt om alle informatie op te slaan onder de juiste sectie
for line in file_object:
    if line[0] not in wit_regels:
        sectie_check = True
        my_dict[sectie] = inhoud
        sectie = ""
        inhoud = ""
        for character in line:
            if character in wit_regels:
                sectie_check = False
            if sectie_check == True:
                sectie += character
            if sectie_check == False:
                inhoud += character
    else:
        if sectie == "DEFINITION":
            line = line.strip()
        inhoud += line

#alle nucleotiden worden in 1 string gezet zodat later met de range de benodigde delen naar het bestand kunnen worden overgezet
origin = my_dict.get("ORIGIN")
for lines in origin:
    for char in lines:
        if char not in getallen and char not in wit_regels:
            nucleotiden += char
            
file_object.close()

#de naam van de nieuwe file wordt gemaakt uit de naam van het gebruikte bestand
def_header = ""
split_name = file_name.split(".")
output_name = split_name[0] + "_features.txt"
output_object = open(output_name, "a")
output_object.write("GenBank Feature Extractor results \n \n")
definition = my_dict.get("DEFINITION").strip()
#de definition regel wordt gestript om alle witregels weg te halen en om een definition die op meerdere regels staat 1 regel te maken
for line in definition:
    for char in line:
        if char != "\n":
            def_header += char
output_object.write(def_header + "\n \n")
nbr = ""
naam = ""
text = ""
next_line = False
features_check = False
line_check = False
file_object = open(file_name)
#eerst wordt er met de features_check gekeken of het bestand bij features is, waar het de informatie weg moet halen
for line in file_object:
    if line[0] not in wit_regels:
        if line.startswith("FEATURES"):
            features_check = True
        if not line.startswith("FEATURES"):
            features_check = False
#wanneer deze check true is wordt er gekeken of er op het 6e character een spatie is, zo nee, dan is het een nieuwe header voor een nucleotide code
    elif features_check == True:
        if line[5] != " ":
            nbr = line[21:-1]
            naam = line[5:-1]
            naam = naam.split(" ")[0]
            next_line = True
            line_check = True
#als next_line true is dan neemt het programma de volgende regel ook mee, omdat hier informatie in staat die nodig is voor de header, wanneer deze regel compleet is wordt de check weer false zodat de volgende line wordt overgeslagen tot er weer een nieuwe header moet komen
        elif next_line == True:
            text = ""
            line = line.strip()
            text = line
            next_line = False
#als line_check true is dan wordt de header gemaakt en wordt de postitie voor het te gebruiken deel van de nucleotiden bepaald uit de inforamtie uit features
        elif line_check == True:
            header = ">" + naam + " " + text + "\n"
            position = nbr.split("..")
            start = int(position[0]) - 1
            output_object.write(header)
#als HL_check true is dan worden alle nucleotiden tot de start ook in de nieuwe file gezet in kleine letters en het deel waar het bij die header om gaat komt er in hoofdletters achter
#de stop positie wordt pas bepaald als het duidelijk is of het om meer dan 1 nucleotide gaat, dit wordt gedaan door te checken of er een . in de positie staat want .. geeft aan dat er een start en een stop positie is
            if "." not in nbr:
                if HL_check == True:
                    output_object.write(nucleotiden[0:start + 1])
                    nucleotiden = nucleotiden.upper()
                output_object.write(nucleotiden[start])
                nucleotiden = nucleotiden.lower()
            else:
                stop = int(position[1])
                if HL_check == True:
                    output_object.write(nucleotiden[0:start + 1])
                    nucleotiden = nucleotiden.upper()
                output_object.write(nucleotiden[start:stop])
                nucleotiden = nucleotiden.lower()
                output_object.write("\n" + "\n")
            line_check = False

output_object.close()
file_object.close()
