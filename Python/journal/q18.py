# 18 Write a Python multithreading program to print the thread name and corresponding process
# for each task (assume that there are four tasks). 
import threading
import os

def task(task_number):
    print(f"Task {task_number} is running in thread: {threading.current_thread().name} (Process ID: {os.getpid()})")

if __name__ == "__main__":
    # Create four threads for four tasks
    threads = []
    for i in range(4):
        thread = threading.Thread(target=task, args=(i+1,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All tasks are completed.")
