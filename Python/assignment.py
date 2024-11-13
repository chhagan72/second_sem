# # s = ("chhagan")
# # count = 0
# # # print(len(s))

# # for i in range(len(s)):
# #     # count += i
# #     for s in range():
# #         count +=1
# # print(i)

# def count_characters(input_string):
#     # Create an empty list to store character counts
#     char_counts = [0] * 128  # Assuming ASCII characters, you may adjust this for Unicode

#     # Iterate through each character in the input string
#     for char in input_string:
#         # Increment the count for the current character
#         char_counts[ord(char)] += 1

#     # Display the counts
#     for i in range(128):
#         if char_counts[i] > 0:
#             print(f"Character '{chr(i)}' appears {char_counts[i]} times.")

# # Example usage
# input_string = "chhagan"
# count_characters(input_string)


def count_Char(s):
    count = 0
    for char in s:
        for i in char:
            if i != char:
                count +=1
        print(f"Character '{char}' appears {count} times.")
s = str(input("Enter your string "))

count_Char(s)

# import random as rr
# a = []
# for i in range(5):
#     b = rr.randint(1,500)
#     a.append(b)
# print(a)

