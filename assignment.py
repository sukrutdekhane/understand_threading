import threading
import time

counter = [0]

def increment_counter():
    for _ in range(10):
        counter[0] += 1

thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(counter[0])