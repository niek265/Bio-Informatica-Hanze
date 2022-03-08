def file_in():
    line_char = ""
    counter = 0
    counter2 = 0
    """
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
    """

    file = input("Please specify a file to open: ")
    file_obj = open(file, "r")
    for line in file_obj:
        if line.startswith(">"):
            line = line.strip()
            print(line)
        else:
            line = line.strip()
            for char in line:
                if counter == 3:
                    counter = 0
                    line_char += (" ")
                    counter2 += 1
                    if counter2 == 17:
                        line_char += "\n"
                        counter2 = 0
                else:
                    line_char += char
                    line_char = line_char.strip()
                    counter += 1
    print(line_char)
    file_obj.close()

file_in()

