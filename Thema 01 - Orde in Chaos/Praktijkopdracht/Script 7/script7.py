def read():
    global file_in
    global file_obj_in
    global file_out
    file_in = input("Please enter the input file:\n")
    file_obj_in = open(file_in)
    file_out = file_in.split(".")
    file_out = file_out[0]+".fasta" # het automatisch aanmaken van de output file name
    

def opener():
    global sections
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
    file_obj_out = open(file_out, "w") # openen van de output file
 
    header = (">" + sections["VERSION"].strip() + " " + sections["DEFINITION"].strip())
    print(header, file=file_obj_out) # het maken en schrijven van de header
    
    for line in sections["ORIGIN"]: # doorstappen van de dictionary entry "origin"
        line = line.strip()
        for char in line:
            if not char in space and char not in numbers: # spaties, tabs, enters en cijfers eruit halen
               nucleotides += char.upper()
               counter +=1
               if counter == 70: # bij 70 characters verdergaan bij een nieuwe regel
                    nucleotides += "\n"
                    counter = 0
    print(nucleotides, file=file_obj_out) # schrijven van de sequence naar de output file
    print("Converted",file_in,"to",file_out)
    file_obj_in.close()
    file_obj_out.close()

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
    another()
