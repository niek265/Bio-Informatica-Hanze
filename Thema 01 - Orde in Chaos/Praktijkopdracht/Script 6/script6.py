def read():
    global input_list
    global out_file
    input_list = list() # het maken van een lijst voor de input
    print("Please provide the following information in this order;\nFilename Startpoint Stoppingpoint Replacement\nExample: dna.fasta 10 12 ATG\nIf you want to enter a deletion, please enter '-' instead of the replacement")
    answer = input("Enter input:\n")
    input_list = answer.split() # het antwoord splitsen en in de lijst zetten
    out_file = input("Please provide an output file: (leave blank if you want this to automatically generate)")
    if out_file == "" or " ": # als niks wordt ingevuld, automatisch de naam genereren
        output_file_name = (input_list[0].split("."))
        out_file = output_file_name[0] + "_mutated.fasta"
    
def write():
    counter = 0
    done = False
    replace = ""
    all_char = ""
    replacement = input_list[3] # vervangende karakters opslaan
    file_obj = open(input_list[0])
    file_obj_out = open(out_file, "w")
    if replacement == "-": # testen of er een deletie plaats moet vinden
        replacement = ""
    for line in file_obj:
        line = line.strip()
        if line.startswith(">"):
            print(line, "mutated", file=file_obj_out) # printen van de header met mutatie
        else:
            for char in line:
                if counter >= int(input_list[1])-1 and counter <= int(input_list[2])-1: # alles binnen de start en stopwaardes overslaan
                    if done == False:
                        all_char += replacement # opslaan van de vervangende tekens in de uitendelijke string
                        counter += 1
                        done = True
                    elif done == True:
                        counter += 1
                else:
                    all_char += char
                    counter += 1
                
        print(all_char, file=file_obj_out) # printen van de nieuwe sequence naar de file
        all_char = ""
    file_obj.close()
    file_obj_out.close()
    print("Saved to file", out_file)

def another(): # vragen om nog een file te openen
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
while running == True:
    read()
    write()
    another()
