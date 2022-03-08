def io():
    all_char = ""
    counter = 0
    input_file_name = input("Please enter the input file: ")
    input_file = open(input_file_name)
    output_file_name = input("Please enter a name for the output file: ")
    output_file = open(output_file_name, "w")
    for text in input_file:
        if text.startswith(">"):
            print(text, file=output_file)
        else:
            text = text.upper()
            text = text.strip()
            for char in text:                
                if counter == 50:
                    counter = 0
                    all_char += ("\n")
                else:                    
                    char = char.strip()
                    all_char += char
                    counter += 1
                
    print(all_char, file=output_file)
    print("Saved to file", output_file_name)
    input_file.close()
    output_file.close()

io()
