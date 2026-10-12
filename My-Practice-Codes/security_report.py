total_logs = 100
failed_logins = 12
errors = 5
alerts = 3

report = f"""
========== SECURITY REPORT ==========

Total logs       : {total_logs}
Failed logins    : {failed_logins}
Errors           : {errors}
Security alerts  : {alerts}

======================================
"""

print(report)
