input_string = input("Enter a string:")
num_letters = 0
num_digits = 0
for char in input_string:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1
print("Letters:", num_letters)
print("Digits:", num_digits)
