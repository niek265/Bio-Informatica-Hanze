file_name = "output1.txt"

file_object = open(file_name, "a")
text = input("Please provide a message to save to file: ")
print(text, file=file_object)
print("content saved to file", file_name)
file_object.close()
