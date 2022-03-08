def ask():
    text = input("Please provide the file name and extension (or type 'cancel' to abort): ")
    if text == "cancel" or text == "Cancel":
        None
    else:
        character = 0
        print("Opening ",text)
        file_object = open(text)
        for line in file_object:
            if line.startswith(">NG"):
                print("This file contains a DNA sequence.")
                ifline()
            elif line.startswith(">NM"):
                print("This file contins a RNA sequence.")
                ifline()
            elif line.startswith(">NP"):
                print("This file contains an aminoacid sequence.")
                ifline()
            else:
                ifline()

def ifline():
    if line.startswith(">"):
        pass
    else:
        line = line.strip()
        print(line)
        character += len(line)
        print("The total amount of characters is:", character)
        file_object.close()
        another()

#def ifline_p():

def another():    
    answer = input("Would you to like to open another file? (yes, no): ")
    answer = answer.lower()
    if  answer == "yes":
        return ask()  
    else:
        if answer == "no":
            print("Understandable, have a nice day!")
        else:
            print("Please enter 'yes' or 'no'")
            return another()

ask()
# pro_sequence_cftr.fasta
