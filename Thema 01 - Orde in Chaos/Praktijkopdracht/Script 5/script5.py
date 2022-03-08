# file name opgeven
def read(): 
    file_name = input("Please enter the file name:\n")
    return file_name

def counter(file_name):    
    triplets = {"TTT":0, "TTC":0,
               "TTA":0, "TTG":0, "CTT":0, "CTC":0, "CTA":0, "CTG":0,
               "ATT":0, "ATC":0, "ATA":0,
               "ATG":0,
               "GTT":0, "GTC":0, "GTA":0, "GTG":0,
               "TCT":0, "TCC":0, "TCA":0, "TCG":0, "AGT":0, "AGC":0,
               "CCT":0, "CCC":0, "CCA":0, "CCG":0,
               "ACT":0, "ACC":0, "ACA":0, "ACG":0,
               "GCT":0, "GCC":0, "GCA":0, "GCG":0,
               "TAT":0, "TAC":0,
               "TAA":0, "TAG":0, "TGA":0,
               "CAT":0, "CAC":0,
               "CAA":0, "CAG":0,
               "AAT":0, "AAC":0,
               "AAA":0, "AAG":0,
               "GAT":0, "GAC":0,
               "GAA":0, "GAG":0,
               "TGT":0, "TGC":0,
               "TGG":0,
               "CGT":0, "CGC":0, "CGA":0, "CGG":0, "AGA":0, "AGG":0, "GGG":0,
               "GGT":0, "GGC":0, "GGA":0} # dict met de tripletten en hun aantallen
    triplet_counter = 0
    triplet = ""
    for pos in range(3): # 3x uitvoeren voor alle nucleotide combinaties
        start = 0
        file_obj = open(file_name)
        for line in file_obj:
            if line.startswith(">"): # header overslaan
                pass
            else:
                line = line.strip()
                if start == pos:                
                    for char in line:
                        if triplet_counter == 3: # 3 nucleotides uitlezen
                            triplets[triplet] +=1 # de teller van desbetreffende triplet optellen
                            triplet_counter = 0
                            triplet = ""
                        else:
                            triplet_counter += 1
                            triplet += char
                else:
                    start += 1
        file_obj.close()
    print(triplets)

def another():
    global running
    answer = input("Would you to like to convert another file? (yes, no): ")
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
    name = read()
    counter(name)
    another()

    
    
    
