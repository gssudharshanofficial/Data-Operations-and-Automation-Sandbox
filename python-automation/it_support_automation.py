# ========================================================================
# CORE SYSTEM PROJECT: AUTOMATED IT NETWORK & ACCESS LOG SECURITY AUDITOR
# AUTHOR: SUDHRSHAN G S
# TARGET USE CASE: System Support Operations, Error Auditing, Data Extraction
# ========================================================================

import datetime

# 1. High-Volume Raw System Log Dataset (Simulating a real live server output stream)
raw_server_logs = [
    "2026-09-16 08:12:04 | INFO     | USER_LOGIN_SUCCESS | User: gssudharshan | Source: 192.168.1.50",
    "2026-09-16 08:15:22 | WARNING  | DISK_SPACE_LOW     | Partition: /var/log | Capacity: 92%",
    "2026-09-16 09:00:10 | CRITICAL | DATABASE_CONN_FAIL | Target: SQL_PROD_DB | Error: Timeout",
    "2026-09-16 09:45:55 | ERROR    | UNAUTHORIZED_ACCESS| User: unknown_admin| Source: 10.0.0.12",
    "2026-09-16 10:30:11 | INFO     | LOGOUT_CLEAN       | User: gssudharshan | Session: 45mins",
    "2026-09-16 11:14:02 | CRITICAL | FIREWALL_BREACH_ATT| Action: Blocked    | IP: 185.220.101.4"
]

def execute_security_audit(log_stream):
    """
    Parses complex raw server strings, filters entries by operational severity,
    and automatically outputs critical actions for IT Support teams.
    """
    print(f"============================================================")
    print(f" RUNNING AUTOMATED LOG AUDIT REPORT | TIMESTAMP: {datetime.datetime.now()}")
    print(f"============================================================\n")
    
    critical_alerts_found = 0
    warning_alerts_found = 0
    
    # 2. String parsing automation logic
    for entry in log_stream:
        # Split the text entry by the pipe character to isolate log attributes
        parts = [p.strip() for p in entry.split("|")]
        
        timestamp = parts[0]
        severity = parts[1]
        event_type = parts[2]
        details = parts[3]
        
        # 3. Categorization & routing mechanism based on data values
        if severity == "CRITICAL":
            critical_alerts_found += 1
            print(f"🚨 [CRITICAL ALARM] Generated at {timestamp}")
            print(f"   Event   : {event_type}")
            print(f"   Detail  : {details}")
            print(f"   Action  : Paging On-Call Network Admin immediately.\n")
            
        elif severity == "ERROR" or severity == "WARNING":
            warning_alerts_found += 1
            print(f"⚠️ [SYSTEM WARNING] Isolated at {timestamp}")
            print(f"   Event   : {event_type}")
            print(f"   Detail  : {details}")
            print(f"   Action  : Logged to local data desk for weekly maintenance review.\n")

    # 4. Final summary diagnostics calculation
    print(f"============================================================")
    print(f" AUDIT METRICS REPORT:")
    print(f" Total Log Records Scanned: {len(log_stream)}")
    print(f" Critical Threats Defused : {critical_alerts_found}")
    print(f" Active Warnings Flagged  : {warning_alerts_found}")
    print(f"============================================================")

# Execute the primary script routine
if __name__ == "__main__":
    execute_security_audit(raw_server_logs)
