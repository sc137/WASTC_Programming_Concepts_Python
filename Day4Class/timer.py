import time

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print("{:02}".format(hour), end=":")
            print("{:02}".format(minute), end=":")
            print("{:02}".format(second), end="\r")
            time.sleep(1) #sleep for one second