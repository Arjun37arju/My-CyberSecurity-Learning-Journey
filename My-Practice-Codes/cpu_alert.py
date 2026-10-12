import psutil

cpu = psutil.cpu_percent(interval=1)

print("CPU Usage:", cpu, "%")

if cpu > 80:
    print("ALERT: High CPU usage!")
