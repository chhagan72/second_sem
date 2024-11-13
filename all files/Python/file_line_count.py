def count_lines_and_words(filename):
    line_count = 0
    word_count = 0

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Increment line count
            line_count += 1
            # Split the line into words and count them
            words = line.split()
            word_count += len(words)

    return line_count, word_count

# Enter the filename
filename = input("Enter the filename: ")

# Call the function to count lines and words
lines, words = count_lines_and_words(filename)

print("Number of lines:", lines)
print("Number of words:", words)