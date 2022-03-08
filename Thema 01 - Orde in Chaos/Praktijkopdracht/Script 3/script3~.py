    output_file_name = input("Please specify an output file: ")
    output_file = open(output_file_name, "a")
    multi_in(output_file, output_file_name)
    all_char = ""
    counter = 0
    ask_i = input("Please specify the file to import: ")
    input_file = open(ask_i)
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
