import threading

# Function to print even numbers
def print_even():
    for i in range(2, 9, 2):
        print("Even Thread:", i)

# Function to print odd numbers
def print_odd():
    for i in range(1, 8, 2):
        print("Odd Thread:", i)

# Creating threads
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

# Starting threads
even_thread.start()
odd_thread.start()

# Waiting for threads to finish
even_thread.join()
odd_thread.join()

print("Both threads have finished execution.")