try:
    # Accepting input from the user
    num = int(input("Enter an integer number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter an integer number.")