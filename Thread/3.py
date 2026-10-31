import threading
import time

def download_file(filename):
    print(f"Downloading {filename}...")
    time.sleep(2)  # Simulating download
    print(f"{filename} downloaded successfully")

# Create threads
t1 = threading.Thread(target=download_file, args=("file1.pdf",))
t2 = threading.Thread(target=download_file, args=("file2.pdf",))
t3 = threading.Thread(target=download_file, args=("file3.pdf",))

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads
t1.join()
t2.join()
t3.join()

print("All files downloaded")