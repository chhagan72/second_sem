{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2776b61c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Assignment 6 :Error and Exception Handling\n",
    "# Name : Rishi Ram\n",
    "# Roll No : 20230201032\n",
    "# Division : SIMMC -A\n",
    "\n",
    "'''\n",
    "1.\tWrite a script for file handling using following function-\n",
    "a.\tcenter()\n",
    "b.\tb.repr()\n",
    "c.\trjust()\n",
    "d.\tljust()\n",
    "e.\tzfill()\n",
    "f.\tformat()\n",
    "g.\tread()\n",
    "h.\topen()\n",
    "i.\ttell()\n",
    "j.\tseek()\n",
    "k.\trename()\n",
    "l.\tremove()\n",
    "m.\tformat()\n",
    "\n",
    "'''\n",
    "# File paths\n",
    "file_path = \"example.txt\"\n",
    "new_file_path = \"new_example.txt\"\n",
    "\n",
    "# a. center()\n",
    "text = \"Hello\"\n",
    "width = 20\n",
    "with open(file_path, 'w') as file:\n",
    "    file.write(text.center(width))\n",
    "\n",
    "# b. repr()\n",
    "obj = [1, 2, 3]\n",
    "with open(file_path, 'a') as file:\n",
    "    file.write(repr(obj))\n",
    "\n",
    "# c. rjust()\n",
    "text = \"World\"\n",
    "width = 10\n",
    "with open(file_path, 'a') as file:\n",
    "    file.write(text.rjust(width))\n",
    "\n",
    "# d. ljust()\n",
    "text = \"Python\"\n",
    "width = 10\n",
    "with open(file_path, 'a') as file:\n",
    "    file.write(text.ljust(width))\n",
    "\n",
    "# e. zfill()\n",
    "num = 42\n",
    "width = 5\n",
    "with open(file_path, 'a') as file:\n",
    "    file.write(str(num).zfill(width))\n",
    "\n",
    "# f. format()\n",
    "text = \"Name: {}\\n\".format(\"John\")\n",
    "with open(file_path, 'a') as file:\n",
    "    file.write(text)\n",
    "\n",
    "# g. read()\n",
    "with open(file_path, 'r') as file:\n",
    "    content = file.read()\n",
    "    print(\"File content:\")\n",
    "    print(content)\n",
    "\n",
    "# h. open() - Not used here, as it's primarily for opening files which is done throughout the script.\n",
    "\n",
    "# i. tell()\n",
    "with open(file_path, 'r') as file:\n",
    "    pos = file.tell()\n",
    "    print(\"Current position:\", pos)\n",
    "\n",
    "# j. seek()\n",
    "with open(file_path, 'r') as file:\n",
    "    file.seek(5)\n",
    "    pos = file.tell()\n",
    "    print(\"Position after seeking:\", pos)\n",
    "\n",
    "# k. rename()\n",
    "import os\n",
    "os.rename(file_path, new_file_path)\n",
    "\n",
    "# l. remove()\n",
    "os.remove(new_file_path)\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "File content:\n",
    "       Hello        [1, 2, 3]     WorldPython    00042Name: John\n",
    "\n",
    "Current position: 0\n",
    "Position after seeking: 5\n",
    "'''\n",
    "'''\n",
    "2.\tCreate a file and copy in another file\n",
    "'''\n",
    "# Source file path (the file you want to copy from)\n",
    "source_file_path = \"source_file.txt\"\n",
    "\n",
    "# Destination file path (the file you want to copy to)\n",
    "destination_file_path = \"destination_file.txt\"\n",
    "\n",
    "# Create the source file and write some content into it\n",
    "with open(source_file_path, 'w') as source_file:\n",
    "    source_file.write(\"This is the content of the source file.\")\n",
    "\n",
    "# Open the source file for reading\n",
    "with open(source_file_path, 'r') as source_file:\n",
    "    # Read the content of the source file\n",
    "    content = source_file.read()\n",
    "\n",
    "    # Open the destination file for writing\n",
    "    with open(destination_file_path, 'w') as destination_file:\n",
    "        # Write the content of the source file into the destination file\n",
    "        destination_file.write(content)\n",
    "\n",
    "print(\"File copied successfully!\")\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "File copied successfully!\n",
    "'''\n",
    "'''\n",
    "3.\tOpen existing file and copy in binary file. Also check file is exist or not.\n",
    "'''\n",
    "import os\n",
    "\n",
    "# Source file path (the existing file you want to copy from)\n",
    "source_file_path = \"existing_file.txt\"\n",
    "\n",
    "# Destination file path (the binary file you want to copy to)\n",
    "binary_file_path = \"binary_copy.bin\"\n",
    "\n",
    "# Check if the source file exists\n",
    "if os.path.exists(source_file_path):\n",
    "    # Open the source file for reading in binary mode\n",
    "    with open(source_file_path, 'rb') as source_file:\n",
    "        # Read the content of the source file\n",
    "        content = source_file.read()\n",
    "\n",
    "        # Open the binary file for writing in binary mode\n",
    "        with open(binary_file_path, 'wb') as binary_file:\n",
    "            # Write the content of the source file into the binary file\n",
    "            binary_file.write(content)\n",
    "\n",
    "    print(\"File copied successfully.\")\n",
    "else:\n",
    "    print(\"Source file does not exist.\")\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "File copied successfully.\n",
    "'''\n",
    "\n",
    "'''\n",
    "4.\tCreate a file. Read the content from file and display on console with result of file – count number vowels, consonants, digit, special character.\n",
    "'''\n",
    "#Function to count the number of vowels, consonants, digits, and special characters\n",
    "def count_characters(text):\n",
    "    vowels = 0\n",
    "    consonants = 0\n",
    "    digits = 0\n",
    "    special_chars = 0\n",
    "\n",
    "    # Define vowels\n",
    "    vowels_list = 'aeiouAEIOU'\n",
    "\n",
    "    for char in text:\n",
    "        if char.isalpha():\n",
    "            if char in vowels_list:\n",
    "                vowels += 1\n",
    "            else:\n",
    "                consonants += 1\n",
    "        elif char.isdigit():\n",
    "            digits += 1\n",
    "        else:\n",
    "            special_chars += 1\n",
    "\n",
    "    return vowels, consonants, digits, special_chars\n",
    "\n",
    "# Create a file and write some content into it\n",
    "file_path = \"sample.txt\"\n",
    "with open(file_path, 'w') as file:\n",
    "    file.write(\"Hello World! 123 $#\")\n",
    "\n",
    "# Read the content of the file\n",
    "with open(file_path, 'r') as file:\n",
    "    content = file.read()\n",
    "    print(\"File Content:\")\n",
    "    print(content)\n",
    "\n",
    "# Count characters in the content\n",
    "vowels, consonants, digits, special_chars = count_characters(content)\n",
    "\n",
    "# Display the results\n",
    "print(\"\\nResults:\")\n",
    "print(\"Number of vowels:\", vowels)\n",
    "print(\"Number of consonants:\", consonants)\n",
    "print(\"Number of digits:\", digits)\n",
    "print(\"Number of special characters:\", special_chars)\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "File Content:\n",
    "Hello World! 123 $#\n",
    "\n",
    "Results:\n",
    "Number of vowels: 3\n",
    "Number of consonants: 7\n",
    "Number of digits: 3\n",
    "Number of special characters: 6\n",
    "'''\n",
    "\n",
    "'''\n",
    "5.\tWrite a program to read file line by line and store in array.\n",
    "'''\n",
    "# File path\n",
    "file_path = \"example.txt\"\n",
    "\n",
    "# List to store lines\n",
    "lines_array = []\n",
    "\n",
    "# Read file line by line and store in array\n",
    "with open(file_path, 'r') as file:\n",
    "    for line in file:\n",
    "        lines_array.append(line.strip())  # Append the line to the array, removing trailing newline characters\n",
    "\n",
    "# Display the lines stored in the array\n",
    "print(\"Lines stored in the array:\")\n",
    "for line in lines_array:\n",
    "    print(line)\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "Lines stored in the array:\n",
    "['Hello','bhai']\n",
    "'''\n",
    "\n",
    "'''\n",
    "6.\tWrite a program to read file line by line and store in variable.\n",
    "'''\n",
    "# File path\n",
    "file_path = \"example.txt\"\n",
    "\n",
    "# Variable to store file content\n",
    "file_content = \"\"\n",
    "\n",
    "# Read file line by line and store in variable\n",
    "with open(file_path, 'r') as file:\n",
    "    for line in file:\n",
    "        file_content += line  # Append the line to the variable\n",
    "\n",
    "# Display the file content stored in the variable\n",
    "print(\"File content stored in the variable:\")\n",
    "print(file_content)\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "File content stored in the variable:\n",
    "THis is my world\n",
    "Where we all humans live here.\n",
    "Ok.\n",
    "'''\n",
    "'''\n",
    "7.\tWrite a script for file handling. Create three file a.txt and b.txt, c.txt. Write a content in file from user. After that copy this content in another file from user taken. Count content - number of line, number of words, number of blank spaces and display result in c.txt.\n",
    "'''\n",
    "# Function to count the number of lines, words, and blank spaces in a text\n",
    "def count_content(text):\n",
    "    num_lines = text.count('\\n') + 1  # Counting the number of lines\n",
    "    words = text.split()  # Splitting the text into words\n",
    "    num_words = len(words)  # Counting the number of words\n",
    "    num_blank_spaces = text.count(' ')  # Counting the number of blank spaces\n",
    "\n",
    "    return num_lines, num_words, num_blank_spaces\n",
    "\n",
    "# Create three files a.txt, b.txt, c.txt\n",
    "files = ['a.txt', 'b.txt', 'c.txt']\n",
    "\n",
    "for filename in files:\n",
    "    with open(filename, 'w') as file:\n",
    "        content = input(f\"Enter content for {filename}: \")\n",
    "        file.write(content)\n",
    "\n",
    "# Copy the content from one file to another\n",
    "source_file = input(\"Enter the source file name: \")\n",
    "destination_file = input(\"Enter the destination file name: \")\n",
    "\n",
    "try:\n",
    "    with open(source_file, 'r') as source:\n",
    "        content = source.read()\n",
    "        with open(destination_file, 'w') as destination:\n",
    "            destination.write(content)\n",
    "    print(\"Content copied successfully.\")\n",
    "except FileNotFoundError:\n",
    "    print(\"One or both of the specified files does not exist.\")\n",
    "\n",
    "# Count the content in the destination file\n",
    "try:\n",
    "    with open(destination_file, 'r') as file:\n",
    "        file_content = file.read()\n",
    "        num_lines, num_words, num_blank_spaces = count_content(file_content)\n",
    "\n",
    "    # Write the result in c.txt\n",
    "    with open('c.txt', 'w') as c_file:\n",
    "        c_file.write(f\"Number of lines: {num_lines}\\n\")\n",
    "        c_file.write(f\"Number of words: {num_words}\\n\")\n",
    "        c_file.write(f\"Number of blank spaces: {num_blank_spaces}\\n\")\n",
    "\n",
    "    print(\"Result written to c.txt.\")\n",
    "except FileNotFoundError:\n",
    "    print(\"Destination file not found.\")\n",
    "\n",
    "#OutPut\n",
    "'''\n",
    "Enter content for a.txt: a\n",
    "Enter content for b.txt: b\n",
    "Enter content for c.txt: c\n",
    "Enter the source file name: write.txt\n",
    "Enter the destination file name: dest.txt\n",
    "Content copied successfully.\n",
    "Result written to c.txt.\n",
    "'''\n",
    "'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8bcc6a5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter content for a.txt: a\n",
      "Enter content for b.txt: b\n",
      "Enter content for c.txt: c\n",
      "Enter the source file name: write.txt\n",
      "Enter the destination file name: dest.txt\n",
      "Content copied successfully.\n",
      "Result written to c.txt.\n"
     ]
    }
   ],
   "source": [
    "# Function to count the number of lines, words, and blank spaces in a text\n",
    "def count_content(text):\n",
    "    num_lines = text.count('\\n') + 1  # Counting the number of lines\n",
    "    words = text.split()  # Splitting the text into words\n",
    "    num_words = len(words)  # Counting the number of words\n",
    "    num_blank_spaces = text.count(' ')  # Counting the number of blank spaces\n",
    "\n",
    "    return num_lines, num_words, num_blank_spaces\n",
    "\n",
    "# Create three files a.txt, b.txt, c.txt\n",
    "files = ['a.txt', 'b.txt', 'c.txt']\n",
    "\n",
    "for filename in files:\n",
    "    with open(filename, 'w') as file:\n",
    "        content = input(f\"Enter content for {filename}: \")\n",
    "        file.write(content)\n",
    "\n",
    "# Copy the content from one file to another\n",
    "source_file = input(\"Enter the source file name: \")\n",
    "destination_file = input(\"Enter the destination file name: \")\n",
    "\n",
    "try:\n",
    "    with open(source_file, 'r') as source:\n",
    "        content = source.read()\n",
    "        with open(destination_file, 'w') as destination:\n",
    "            destination.write(content)\n",
    "    print(\"Content copied successfully.\")\n",
    "except FileNotFoundError:\n",
    "    print(\"One or both of the specified files does not exist.\")\n",
    "\n",
    "# Count the content in the destination file\n",
    "try:\n",
    "    with open(destination_file, 'r') as file:\n",
    "        file_content = file.read()\n",
    "        num_lines, num_words, num_blank_spaces = count_content(file_content)\n",
    "\n",
    "    # Write the result in c.txt\n",
    "    with open('c.txt', 'w') as c_file:\n",
    "        c_file.write(f\"Number of lines: {num_lines}\\n\")\n",
    "        c_file.write(f\"Number of words: {num_words}\\n\")\n",
    "        c_file.write(f\"Number of blank spaces: {num_blank_spaces}\\n\")\n",
    "\n",
    "    print(\"Result written to c.txt.\")\n",
    "except FileNotFoundError:\n",
    "    print(\"Destination file not found.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6b1a54c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File copied successfully!\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "421e2a17",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}