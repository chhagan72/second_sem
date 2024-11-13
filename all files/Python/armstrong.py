# Accepting input from the user
num = int(input("Enter a number: "))

# Calculating the number of digits in the number
num_str = str(num)
num_digits = len(num_str)

# Calculating the sum of the nth power of each digit
armstrong_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10

# Checking if the number is an Armstrong number
if num == armstrong_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")