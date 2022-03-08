file_name = input("Please enter file name: ")
file_object = open(file_name)
lines = file_object.readlines()

# Lijst met namen van Features
feature_names = []
# Lijst met indexen van Features in de sequence lijst
feature_index = []
# Type van de feature (op de volgende line)
feature_type = []

is_sequence = False
sequence = ""
definition = ""

answer = input("Sequence feature should be: seperated/uppercased ")


index = 0
while index < len(lines):  # wanneer index kleiner is dan het aantal lines
    line = lines[index]

    # Als de lijn start met "definition" opslaan voor de eerste line van het nieuwe txt document
    if line.startswith("DEFINITION"):
        definition = line.replace("DEFINITION", "").replace("  ", "")

    # Alle witregels uit de lijn verwijderen
    line = line.replace(" ", "")

    # Als er een lijn wordt gevonden met ".."
    if line.find("..") != -1:  # De functie find geeft -1 terug als het NIET is gevonden
        name = ""
        indexes = ""
        for char in line:  # Voor elk character in de lijn
            if not char.isdigit() and char != ".":  # De naam in deze lijn heeft geen cijfers en leestekens.
                name += char
            else:
                indexes += char  # De index bestaat alleen uit cijfers en leestekens

        # De gevonden naam en indexen worden toegevoegd aan de lijst
        feature_names.append(name.replace("\n", ""))
        feature_index.append(indexes)

        # Het type wordt gevonden op de volgende line. Daarom gebruiken we een while loop met een index
        type = lines[index + 1].strip()

        feature_type.append(type)

    # Checkt of de lines met de sequentie zijn begonnen.
    if is_sequence:
        if not line.startswith("//"):  # Als niet de laatste lijn van de sequentie is bereikt "//"
            line_without_digits = ""

            # Dit haalt alle cijfers uit de lijn
            for char in line:
                if not char.isdigit():
                    line_without_digits += char
                    if answer == "uppercased":
                        line_without_digits = line_without_digits.upper()

            # Haal alle enters uit de lijn
            sequence += line_without_digits.replace("\n", "")

    if line.startswith("ORIGIN"):
        is_sequence = True

    # index wordt opgeteld voor de volgende line
    index = index + 1


result = ""
result += definition
result += "\n"

i = 0
# Voor elke feature in de feature lijst
# Er word weer een index gebruikt omdat we de andere lijsten ook willen gebruiken.
while i < len(feature_names):
    # De eerste regel bestaat uit de naam en type van de feature plus een enter.
    result += feature_names[i] + "  " + feature_type[i] + "\n"

    # De index van de eerste punt word gestuurd.
    dot_index = feature_index[i].find(".")

    # de eerste index (getal voor de "..")
    # het laatste index (getal na de "..")
    first_index = feature_index[i][0:dot_index]
    last_index = feature_index[i][dot_index + 2:len(feature_index[i])]

    # Nu word het deel uit de volledige sequentie gehaald die bij de feature naam en type hoord.
    part = sequence[int(first_index) - 1: int(last_index)]

    # Het volgende zorgt er voor dat de maximaal lijnen 60 tekens lang worden. Er word dus een enter na 60 tekens toegevoegd.
    count = 0
    for char in part:
        count += 1
        result += char

        if count == 60:
            result += "\n"
            count = 0

    # Er worden twee enters toegevoegd na elke feature
    result += "\n\n"
    i += 1

# Maak een nieuwe file_name (veranderd .gb naar .txt
new_file_name = (file_name.replace(".gb", "") + ".txt")
new_file = open(new_file_name, "w")

new_file.write(result)
new_file.close()



