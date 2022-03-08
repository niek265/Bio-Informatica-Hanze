def read():
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
    file = input("Please specify a file to open:\n")
    file_obj = open(file, "r")
    file_out = input("Please specify an output file:\n")
    file_obj_out = open(file_out, "a")
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
    print(total_char, file=file_obj_out)
    print("Saved to file", file_out)
    file_obj.close()
    file_obj_out.close()
    
read()

