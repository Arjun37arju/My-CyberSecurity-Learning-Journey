
import psutil

print("======SYSTEM MONITORING=====")
print("cpu:", psutil.cpu_percent(),"%")
print("memory: ", psutil.virtual_memory().percent, "%")
print("disk:", psutil.disk_usage("/").percent,"%")


print("\n========== MONITORING COMPLETED ==========")
