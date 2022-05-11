pro_dict = {'CYS': 'C', 'ASP': 'D', 'SER': 'S',
            'GLN': 'Q', 'LYS': 'K', 'ILE': 'I',
            'PRO': 'P', 'THR': 'T', 'PHE': 'F',
            'ASN': 'N', 'GLY': 'G', 'HIS': 'H',
            'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E',
            'TYR': 'Y', 'MET': 'M', 'UNK': '-'}
def read():
    global file, file_obj
    file = input('Please specify the file to open:\n')
    file_obj = open(file)
     
def pro_sequence():
    global protein_letters, proteins
    proteins = ''
    trip_count = 0
    letters = ''
    protein_letters = ''
    for line in file_obj:
        if line.startswith('SEQRES'):
            counter = 0
            for char in line:
                if counter >= 19:
                    proteins += char.strip()
                    counter += 1
                else:
                    counter += 1
    for char in proteins:
        trip_count += 1
        letters += char
        if trip_count == 3:
            protein_letters += pro_dict[letters]
            trip_count = 0
            letters = ''
    file_obj.close()

def helix():
    global helix_sequence
    helix_list = []
    helix_start = 0
    helix_stop = 0
    helix_count = 0
    helix_sequence = ''
    file_obj = open(file)
    for line in file_obj:
        helix_count = 0
        if line.startswith('HELIX'):
            helix_list = line.split()
            helix_start = int(helix_list[5])
            helix_stop = int(helix_list[8])
            for char in protein_letters:
                if helix_count >= helix_start and helix_count <= helix_stop:
                    helix_sequence += char
                helix_count += 1

def sheet():
    global sheet_sequence
    sheet_count = 0
    sheet_sequence = ''
    file_obj = open(file)
    for line in file_obj:
        sheet_count = 0
        if line.startswith('SHEET'):
            letter = False
            sheet_list = []
            sheet_start = ''
            sheet_stop = ''
            sheet_list = line.split()
            for char in sheet_list[6]:
                if char.isalpha():
                    letter = True
                    break
                else:
                    sheet_start += char
                    sheet_stop = sheet_list[9]

            if letter == True:
                for char in sheet_list[5]:
                        if not char.isalpha():
                            sheet_start += char
                for char in sheet_list[7]:
                        if not char.isalpha():
                            sheet_stop += char
                            
            for char in protein_letters:
                if sheet_count >= int(sheet_start) and sheet_count <= int(sheet_stop):
                    sheet_sequence += char
                sheet_count += 1
    file_obj.close()

def printer():
    file_list = file.split('.')
    file_out = file_list[0] + '_HS.fasta'
    file_obj_out = open(file_out, 'w')
    file_obj = open(file)
    for line in file_obj:
        if line.startswith('HEADER'):
            header_list = line.split()
    header_helix = '>' + header_list[5] + ' ' + header_list[1] + ' ' + header_list[2] + ' ' + header_list[3] + ' HELIX'
    header_sheet = '>' + header_list[5] + ' ' + header_list[1] + ' ' + header_list[2] + ' ' + header_list[3] + ' SHEET'

    counter = 0
    helix_print = ''
    for char in helix_sequence:
        if counter == 70:
            counter = 0
            helix_print += "\n"
        else:
            counter += 1
            helix_print += char        

    global sheet_sequence
    counter2 = 0
    sheet_print = ''
    for char in sheet_sequence:
        if counter2 == 70:
            counter2 = 0
            sheet_print += "\n"
        else:
            counter2 += 1
            sheet_print += char

    print(header_helix, file=file_obj_out)
    print(helix_print, '\n', file=file_obj_out)
    print(header_sheet, file=file_obj_out)
    print(sheet_print, '\n', file=file_obj_out)

def graph():
    h = '#'
    total_p = 0
    count_dict = {'C': 0, 'D': 0, 'S': 0,
                  'Q': 0, 'K': 0, 'I': 0,
                  'P': 0, 'T': 0, 'F': 0,
                  'N': 0, 'G': 0, 'H': 0,
                  'L': 0, 'R': 0, 'W': 0,
                  'A': 0, 'V': 0, 'E': 0,
                  'Y': 0, 'M': 0, '-': 0}
    for p in protein_letters:
        total_p += 1
        count_dict[p] += 1
    print('\nGrafiek voor de protein sequence:')
    for key in count_dict.keys():
        pro_p = count_dict[key] / total_p * 100
        print(key, count_dict[key], ' ', h * int(round(pro_p)), (round(pro_p)), "%")

def graph_helix():
    h = '#'
    total_p = 0
    count_dict = {'C': 0, 'D': 0, 'S': 0,
                  'Q': 0, 'K': 0, 'I': 0,
                  'P': 0, 'T': 0, 'F': 0,
                  'N': 0, 'G': 0, 'H': 0,
                  'L': 0, 'R': 0, 'W': 0,
                  'A': 0, 'V': 0, 'E': 0,
                  'Y': 0, 'M': 0, '-': 0}
    for p in helix_sequence:
        total_p += 1
        count_dict[p] += 1
    print('\nGrafiek voor de helix sequence:')
    for key in count_dict.keys():
        pro_p = count_dict[key] / total_p * 100
        print(key, count_dict[key], ' ', h * int(round(pro_p)), (round(pro_p)), "%")

def graph_sheet():
    h = '#'
    total_p = 0
    count_dict = {'C': 0, 'D': 0, 'S': 0,
                  'Q': 0, 'K': 0, 'I': 0,
                  'P': 0, 'T': 0, 'F': 0,
                  'N': 0, 'G': 0, 'H': 0,
                  'L': 0, 'R': 0, 'W': 0,
                  'A': 0, 'V': 0, 'E': 0,
                  'Y': 0, 'M': 0, '-': 0}
    for p in sheet_sequence:
        total_p += 1
        count_dict[p] += 1
    print('\nGrafiek voor de sheet sequence:')
    for key in count_dict.keys():
        pro_p = count_dict[key] / total_p * 100
        print(key, count_dict[key], ' ', h * int(round(pro_p)), (round(pro_p)), "%")

running = True
while running == True:
    read()
    pro_sequence()
    helix()
    sheet()
    printer()
    graph()
    graph_helix()
    graph_sheet()