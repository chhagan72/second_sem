# Write a Python multithreading program which creates two threads, one for calculating the
# square of a given number and other for calculating the cube of a given number. 
import threading

def calculate_square(number):
    print(f"Square of {number}: {number ** 2}")

def calculate_cube(number):
    print(f"Cube of {number}: {number ** 3}")

if __name__ == "__main__":
    number = 5
    
    # Create two threads, one for square and one for cube
    square_thread = threading.Thread(target=calculate_square, args=(number,))
    cube_thread = threading.Thread(target=calculate_cube, args=(number,))

    # Start both threads
    square_thread.start()
    cube_thread.start()

    # Wait for both threads to finish
    square_thread.join()
    cube_thread.join()

    print("Main thread finished.")
