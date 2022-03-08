def read():    
    aminoacids = {"M":0}
    file = input("Please specify a file to open:\n")
    file_obj = open(file)
    for line in file_obj:
        if line.startswith(">"):
            pass
        else:
            for a in line:
                aminoacids["M"] += line.count("M")
            if aminoacids["M"]:
                print("This file alread contains an aminoacid sequence, please open a nucleotide sequence.")
                file_obj.close()
                #return read()
                read()
            else:
                file_out = input("Please specify an output file:\n")
                file_obj_out = open(file_out, "a")
                file_obj.close()
                convert(file_obj_out, file_out, file)
        
def convert(file_obj_out, file_out, file):
    pro_char = ""
    total_char = ""
    counter = 0
    counter2 = 0
    codons = {"TTT":"F", "TTC":"F",
               "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
               "ATT":"I", "ATC":"I", "ATA":"I",
               "ATG":"M",
               "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
               "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
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
               "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", "GGG":"R",
               "GGT":"G", "GGC":"G", "GGA":"G"}
    file_obj = open(file)
    for line in file_obj:
        if line.startswith(">"):
            line = line.strip()
            print(line, file=file_obj_out)
        else:
                line = line.strip()
                for char in line:
                    if counter == 3:
                        aminoacid = codons[pro_char]
                        total_char += aminoacid    
                        counter = 0
                        counter2 += 1
                        pro_char = ""
                        if counter2 == 70:
                            total_char += "\n"
                            counter2 = 0
                    else:
                        pro_char += char
                        pro_char = pro_char.strip()
                        counter += 1
    result(file_obj, file_obj_out, file_out, total_char)

def result(file_obj, file_obj_out, file_out, total_char):
    print(total_char, file=file_obj_out)
    print("Saved to file", file_out)
    another(file_obj, file_obj_out)

def another(file_obj, file_obj_out):    
    answer = input("Would you to like to convert another file? (yes, no): ")
    answer = answer.lower()
    if  answer == "yes":
        read()  
    else:
        if answer == "no":
            close(file_obj, file_obj_out)            
        else:
            print("Please enter 'yes' or 'no'")
            return another()

def close(file_obj, file_obj_out):
    print("Have a nice day!")
    file_obj.close()
    file_obj_out.close()
    pass
    

print("Converter of fasta files with DNA sequences.\nOutputs the sequence in aminoacid codes.\nStopcodons will be shown as :'#'.")
read()



