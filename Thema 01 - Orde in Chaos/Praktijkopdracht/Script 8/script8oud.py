def read():
    global file_in
    global file_obj_in
    file_in = input("Please enter the input file:\n")
    file_obj_in = open(file_in)    

def opener():
    global sections
    global header
    global nucleotides
    space = ("\n", "\t"," ","/")
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    sections = dict() # het maken van een lege dictionary voor de secties
    cats = ""
    info = ""
    nucleotides = ""
    counter = 0
    for line in file_obj_in:
        if not line.startswith(" "):
            line = line.strip()
            info_stream = True
            sections[cats] = info # het opnemen van de key en value in de dictionary
            cats = ""
            info = ""
            for char in line:
                if char == " ": # spatie detecteren
                    info_stream = False
                if info_stream == True: # het schrijven van de characters naar de keystring
                    cats += char
                if info_stream == False: # het schrijven van de characters naar de valuestring
                    if char != "\t":
                        info += char
        else:
            line = line.strip()
            info += line
 
    header = (">" + sections["VERSION"].strip() + " " + sections["DEFINITION"].strip())
    
    for line in sections["ORIGIN"]: # doorstappen van de dictionary entry "origin"
        line = line.strip()
        for char in line:
            if not char in space and char not in numbers: # spaties, tabs, enters en cijfers eruit halen
               nucleotides += char.upper()
               counter +=1
               if counter == 70: # bij 70 characters verdergaan bij een nieuwe regel
                    nucleotides += "\n"
                    counter = 0
    file_obj_in.close()

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
    file_obj = open(file_in)

    file_new = file_in.split(".")[0] + "_features.fasta"
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
                    subsection = ">"
                    start = ""
                    stop = ""
                    dots = False
            else:
                break
    
    file_new_obj.close()
    file_obj.close()

def another(): # vragen of nog een file geopend moet worden
    global running
    answer = input("Would you to like to run again? (yes, no): ")
    answer = answer.lower()
    if  answer == "yes":
        pass
    else:
        if answer == "no":
            print("Have a nice day!")
            running = False
        else:
            print("Please enter 'yes' or 'no'")
            return another()

running = True
while running == True: # loop om de definities aan te roepen
    read()
    opener()
    writer()
    another()
