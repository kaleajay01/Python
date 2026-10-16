import multiprocessing
import time

def task(name):
    print(f"{name} started")

    time.sleep(5)

    print(f"{name} completed")


if __name__ == "__main__":

    p1 = multiprocessing.Process(
        target=task,
        args=("Process 1",)
    )

    p2 = multiprocessing.Process(
        target=task,
        args=("Process 2",)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed")