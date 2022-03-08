opened = False
h = "#"
def reader():
        global opened
        if opened is False:
                answer = input("Welcome, would you to like to open a file? (yes, no): ") # openen van de file
        else:
                answer = input("Would you to like to open another file? (yes, no): ")
        answer = answer.lower()
        if  answer == "yes":
                file_name = input("Please provide the file name & extension: ")
                file_object = open(file_name)
                opened = True
                scanner(file_object)
        else:
                if answer == "no":
                        print("Understandable, have a nice day!")
                        pass
                else:
                        print("Please enter 'yes' or 'no'")
                        return reader()

def scanner(file_object):
        nucleotides = {"A":0, "T":0, "G":0, "C":0} # dictionaries
        aminoacids = {"A":0, "R":0, "N":0, "D":0, "C":0, "E":0, "Q":0, "G":0, "H":0, "I":0, "L":0, "K":0, "M":0, "F":0, "P":0, "S":0, "T":0, "W":0, "Y":0, "V":0}
        for line in file_object:
            if not line.startswith(">"):
                    line = line.strip()
                    print(line)
            else:
                    print()
                    print(line)
            if not line.startswith(">"): # voor het overslaan van de header met tellen
                    for n in nucleotides.keys():
                            nucleotides[n] += line.count(n)
                    for a in aminoacids.keys():
                            aminoacids[a] += line.count(a)
        total_n = 0
        for i in ["A", "T", "G", "C"]:
                total_n += nucleotides[i]

        total_a = 0
        for i in ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]:
            total_a += aminoacids[i]
        G = nucleotides["G"] # berekenen van GC en het percentage
        C = nucleotides["C"]
        GC = G+C
        GCP = GC / total_n * 100
        if aminoacids["M"]: # testen of het nucleotiden of aminozuren zijn
            print("The file contains Aminoacids")
            for key in aminoacids.keys():
                amino_p = aminoacids[key] / total_a * 100 #berekenen van de percentages van de aminozuren
                print(key, aminoacids[key], h * int(round(amino_p)), (round(amino_p)), "%")
            print("The total amount of characters is: ", total_a)
        else:
            print("The file contains Nucleotides.")
            for key in nucleotides.keys():
                nucleo_p = nucleotides[key] / total_n * 100
                print(key, nucleotides[key], h * int(round(nucleo_p)), (round(nucleo_p)), "%")
            print("The total amount of characters is: ", total_n)
            print("The percentage of GC in the sequence is: ", round(GCP),"%")
        file_object.close()
        reader()

reader()

