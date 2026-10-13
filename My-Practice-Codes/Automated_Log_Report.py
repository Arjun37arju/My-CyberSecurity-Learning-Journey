def generate_report(logs):
    total_logs = len(logs)
    failed_logins = [line for line in logs if "Failed password" in line]
    errors = [line for line in logs if "ERROR" in line]

    report = f"""
    === Automated Log Report ===
    Total log entries: {total_logs}
    Failed login attempts: {len(failed_logins)}
    Error events: {len(errors)}
    """
    return report


# Example usage
logs = [
    "Sep 16 10:20:31 server1 sshd[1234]: Failed password for root from 192.168.1.10",
    "Sep 16 10:21:02 server1 app[5678]: ERROR: Database connection failed",
    "Sep 16 10:22:15 server1 sshd[1234]: Failed password for admin from 192.168.1.30"
]

print(generate_report(logs))
