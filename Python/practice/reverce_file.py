# ex = "ex.txt"

# # def r_word(r):
# #     return r[::-1]
# try:
#     with open(ex,"r") as read_data:
#         content=read_data.read()
# except FileNotFoundError as f:
#     print("File not found.........")
# words=content.split()
# r_words = [ex for ex in words]
# r_content=" ".join(r_words)


# with open("r_file.txt","w") as o_file:
#     o_file.write(r_content)


def reverse_word(word):
    """
    Function to reverse a word.
    """
    return word[::-1]

def main():
    # Open the input file for reading
    try:
        with open("data.txt", "r") as input_file:
            # Read the contents of the file
            content = input_file.read()
    except FileNotFoundError:
        print("Error: File 'data.txt' not found")
        return

    # Split the content into words
    words = content.split()

    # Reverse each word
    reversed_words = [reverse_word(word) for word in words]

    # Join the reversed words into a string
    reversed_content = " ".join(reversed_words)

    # Write the reversed content to a new file
    with open("reversed_data.txt", "w") as output_file:
        output_file.write(reversed_content)

    print("Words reversed and saved to 'reversed_data.txt'")

if __name__ == "__main__":
    main()
