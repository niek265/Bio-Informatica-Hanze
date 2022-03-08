def read():    # inlezen van de file
    file = input("Please specify a file to open:\n")
    file_obj = open(file, "r")
    file_out = input("Please specify an output file:\n")
    file_obj_out = open(file_out, "a")
    convert(file_obj, file_obj_out, file_out)
        
def convert(file_obj, file_obj_out, file_out):
    pro_char = "" 
    total_char = ""
    counter = 0
    counter2 = 0
    codons = {"TTT":"F", "TTC":"F",
               "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
               "ATT":"I", "ATC":"I", "ATA":"I",
               "ATG":"M",
               "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
               "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
               "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
               "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
               "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
               "TAT":"Y", "TAC":"Y",
               "TAA":"#", "TAG":"#", "TGA":"#",
               "CAT":"H", "CAC":"H",
               "CAA":"Q", "CAG":"Q",
               "AAT":"N", "AAC":"N",
               "AAA":"K", "AAG":"K",
               "GAT":"D", "GAC":"D",
               "GAA":"E", "GAG":"E",
               "TGT":"C", "TGC":"C",
               "TGG":"W",
               "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
               "AGT":"S", "AGC":"S",
               "AGA":"R", "AGG":"R",
               "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"R"}
    for line in file_obj:
        if line.startswith(">"): # header printen in de file
            line = line.strip()
            print(line, file=file_obj_out)
        else:
            line = line.strip()
            for char in line: # tripletten testen en corresponderende aminozuren naar een string schrijven
                if counter == 3:
                    aminoacid = codons[pro_char]
                    total_char += aminoacid    
                    counter = 0
                    counter2 += 1
                    pro_char = ""
                    if counter2 == 70: # afsnijden bij 70 karakters
                        total_char += "\n"
                        counter2 = 0
                else:
                    pro_char += char
                    pro_char = pro_char.strip()
                    counter += 1
    result(file_obj, file_obj_out, file_out, total_char)

def result(file_obj, file_obj_out, file_out, total_char):
    print(total_char, file=file_obj_out) # schrijven van alle karakters naar de opgegeven file
    print("Saved to file", file_out)
    file_obj.close()
    file_obj_out.close()
    another()

def another():    
    answer = input("Would you to like to convert another file? (yes, no): ")
    answer = answer.lower()
    if  answer == "yes":
        return read()  
    else:
        if answer == "no":
            print("Have a nice day!")
            pass
        else:
            print("Please enter 'yes' or 'no'")
            return another()

print("Converter of fasta files with DNA sequences.\nOutputs the sequence in aminoacid codes.\nStopcodons will be shown as :'#'.")
read()



