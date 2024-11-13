num = int(input("Enter a number: "))
binary_number = bin(num)[2:]
octal_number = oct(num)[2:]
hexadecimal_number = hex(num)[2:]
if num % 2 == 0:
    classification = "even"
else:
    classification = "odd"
print(f"Decimal: {num}")
print(f"Binary: {binary_number}")
print(f"Octal: {octal_number}")
print(f"Hexadecimal: {hexadecimal_number}")
print(f"The number is {classification}.")