# Given a file called myfile.txt which contains the text: “Python is object oriented programming
# language”. Write a program in Python that transforms the content of the file by writing each word
# in a separate line. 
# Open the input file in read mode
with open("myfile.txt", "r") as file:
    # Read the content of the file
    content = file.read()
    # Split the content into words
    words = content.split()

# Open a new file in write mode
with open("transformed_file.txt", "w") as new_file:
    # Write each word on a separate line
    for word in words:
        new_file.write(word + "\n")

print("Transformation complete. Check transformed_file.txt for the result.")
