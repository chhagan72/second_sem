# 22 Write a function in python that allows you to count the frequency of repetition of each word
# found in a given file. 
def count_word_frequency(filename):
    word_frequency = {}
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Split the content into words
        words = content.split()
        # Count the frequency of each word
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    return word_frequency

# Test the function with a file named "example.txt"
filename = "myfile.txt"  # Replace "example.txt" with the name of your text file
word_frequency = count_word_frequency(filename)

# Print the frequency of each word
for word, frequency in word_frequency.items():
    print(f"'{word}': {frequency}")
