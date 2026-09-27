import threading
import time
def download_policy():
    print("Downloading policy...")
    time.sleep(5)
    print("Policy downloaded")
def send_email():
    print("Sending email...")
    time.sleep(12)
    print("Email sent")
t1 = threading.Thread(target=download_policy)
t2 = threading.Thread(target=send_email)
t1.start()
t2.start()

# waiting for all thread to complete
t1.join()
t2.join()
print("All tasks completed")