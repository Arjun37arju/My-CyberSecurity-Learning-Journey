def categorize_event(event):
    if "Failed login" in event or "Successful login" in event:
        return "Authentication"

    elif "port scan" in event or "connection" in event:
        return "Network"

    elif "ERROR" in event or "crash" in event:
        return "System"

    elif "malware" in event or "virus" in event:
        return "Threat"

    else:
        return "Other"


def generate_alert(event, category):
    if "Failed login" in event:
        return "ALERT: Failed login detected"

    if category == "Threat":
        return "ALERT: Possible security threat detected"

    if category == "System":
        return "ALERT: System error detected"

    return "No alert"


logs = [
    "Failed login from 192.168.1.10",
    "Firewall detected port scan from 192.168.1.20",
    "ERROR: Database connection failed",
    "Antivirus detected malware in file.exe",
    "User arjun logged in successfully"
]


for log in logs:
    category = categorize_event(log)
    alert = generate_alert(log, category)

    print(f"Event    : {log}")
    print(f"Category : {category}")
    print(f"Alert    : {alert}")
    print("-----------------------------")
