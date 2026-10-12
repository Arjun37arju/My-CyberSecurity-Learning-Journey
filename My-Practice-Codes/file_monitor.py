
import os
import time

file = "data.csv"

old_time = os.path.getmtime(file)

while True:
    new_time = os.path.getmtime(file)

    if new_time != old_time:
        print("ALERT: File has been modified!")
        old_time = new_time
    else:
        print("eveything oky")

    time.sleep(2)
