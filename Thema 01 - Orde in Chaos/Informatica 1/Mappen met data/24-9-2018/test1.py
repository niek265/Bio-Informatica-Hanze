file_name = "input1.txt"

file_object = open(file_name)

for line in file_object:
    line = line.strip()
    print(line)

file_object.close
