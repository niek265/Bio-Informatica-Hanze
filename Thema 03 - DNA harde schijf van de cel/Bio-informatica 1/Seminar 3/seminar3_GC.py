file_name = "input_sequence.txt"
file_obj = open(file_name)

highest_pstring = " "
highest_percentage = 0
print("Opening", file_name)
for line in file_obj:
    line = line.strip()
    G = line.count("G")
    C = line.count("C")
    GC = C + G
    
    GC_percentage = GC / len(line) * 100
   
    if GC_percentage > highest_percentage:
        highest_percentage = GC_percentage
        highest_pstring = line        
    print(line, "The percentage of GC is: ", GC_percentage)

print("The highest percentage of CG is:",highest_percentage,"in string:",highest_pstring)

file_obj.close()
