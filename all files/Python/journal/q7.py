# Write a Python program to generate a random alphabetical character, alphabetical string
# and alphabetical string of a fixed length. Use random.choice()


import random
import string

rndchoice = random.choice(string.ascii_letters)
print("Random alphabetical character:", rndchoice)

random_length = random.randint(5, 15)  
random_string = ''  
for _ in range(random_length):
    random_string += random.choice(string.ascii_letters)
print("Random alphabetical string:", random_string)

fixed_length = 10
fixed_length_string = ''  
for _ in range(fixed_length):
    fixed_length_string += random.choice(string.ascii_letters)
print("Random alphabetical string of fixed length:", fixed_length_string)

