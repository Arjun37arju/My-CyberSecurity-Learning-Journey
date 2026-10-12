logs = [
    "Failed login from 192.168.1.10",
    "Successful login from 192.168.1.20",
    "Failed login from 192.168.1.10",
    "ERROR: Database connection failed"
]

failed_logins = []

for log in logs:
    if "Failed login" in log:
        failed_logins.append(log)

print("Failed login attempts:", len(failed_logins))
