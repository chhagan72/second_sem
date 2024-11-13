'''
What is thread? Write a program that creates two threads. One thread
should print even numbers from 2 to 8 and the other should print odd
numbers from 1 to 7

Ans: 
Thead:
A thread is the smallest unit of execution within a process. Threads enable concurrent execution of tasks within a program. Multiple threads within a process can execute independently, sharing the same memory space and resources, which can lead to more efficient program execution, especially in tasks that involve waiting for I/O or performing parallel computations.
'''
import threading
def print_even():
    for i in range(2,9,2):
        print("Even Thread : ",i)

def print_odd():
    for i in range(1,8,2):
        print("Odd Thread : ",i)

even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

even_thread.start()
even_thread.join()
odd_thread.start()
odd_thread.join()


print("The main thread exiting.")