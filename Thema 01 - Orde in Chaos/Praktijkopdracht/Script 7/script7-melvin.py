file_name = input("Put your filename here: ")
file_object = open(file_name)
sectie = ''
inhoud = ''
my_dict = dict()


for line in file_object:
    if not line.startswith(" "):
        line = line.strip()
        y = True
        my_dict[sectie] = inhoud
        sectie = ''
        inhoud = ''
        for character in line:
            if character == " ":
                y = False
            if y == True:
                sectie += character
            if y == False:
                if character != "\t":
                    inhoud += character
    else:
        line = line.strip()
        inhoud += line

print(my_dict)


version = my_dict.get('VERSION').strip()
definition = my_dict.get('DEFINITION').strip()
header = (">" + version + " " + definition)
print(header)



    

             
