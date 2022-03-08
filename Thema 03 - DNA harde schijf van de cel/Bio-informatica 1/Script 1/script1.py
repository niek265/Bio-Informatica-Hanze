def function():
    text = input("Please provide the name and extension of the file: ")
    character = 0

    file_object = open(text)
    for line in file_object:
        if line.startswith(">"):
            None
        else:
            line = line.strip()
            print(line)
            character += len(line)
    print("The total amount of characters is:", character)
        
    answer = input("Would you to like to open another file? (yes, no): ")
    if  answer == "Yes" or answer == "yes":
        return function()  
    else:
        if answer == "No" or answer == "no":
            print("Understandable, have a nice day!")
        else:
            print("Please enter 'yes' or 'no'")
        

function()
        



    
       
