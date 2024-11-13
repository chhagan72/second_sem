# 21] Write a Python program that displays the longest word found in a text file
def longest_word(filename):
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Split the content into words
        words = content.split()
        # Find the longest word
        longest = max(words, key=len)
    return longest

# Test the function with a file named "example.txt"
filename = "myfile.txt"  # Replace "example.txt" with the name of your text file
longest = longest_word(filename)
print("Longest word in the file:", longest)
