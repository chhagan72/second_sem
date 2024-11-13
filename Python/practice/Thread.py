import threading
import time

def a(name,delay):
    print(f" {name} started")
    time.sleep(delay)
    print(f" {name} finished")

thread1 = threading.Thread(target=a, args=("A", 2))
thread2 = threading.Thread(target=a, args=("B", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All Threading Task are complated")

