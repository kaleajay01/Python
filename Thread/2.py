import threading
import time

# 1. Function executed by each thread
def task(name):
    print(f"{name} started")
    time.sleep(5)
    print(f"{name} finished")


# 2. Create threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))


# 3. Start threads
t1.start()
t2.start()


# 4. Wait for both threads to finish
t1.join()
t2.join()


# 5. Continue main program
print("All tasks completed")