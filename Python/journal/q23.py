# 23 Write a Python program which allows you to extract the content of a file from the 3rd line to
# the 7th line and save it in another file called extract_content.txt.
def extract_content(input_file, output_file):
    with open(input_file, 'r') as file:
        # Read all lines from the input file
        lines = file.readlines()

    # Extract lines from 3rd to 7th
    extracted_lines = lines[2:7]

    # Write extracted lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(extracted_lines)

# Test the function with a file named "input_file.txt"
input_file = "myfile.txt"  # Replace "input_file.txt" with the name of your input file
output_file = "transformed_file.txt"
extract_content(input_file, output_file)

print(f"Content from {input_file} extracted and saved in {output_file}.")

