# ========================================================================
# CORE UTILITY: AUTOMATED IT DESK SECURITY DATA PIPELINE ENGINE (ETL)
# AUTHOR: SUDHRSHAN G S
# OBJECTIVE: Transform raw text data streams into relational database scripts
# ========================================================================

import datetime

# PHASE 1: RAW INGESTION (Simulating unstructured, raw IT system logs)
RAW_DATA_STREAM = [
    "LOG-ID: 9001 | 2026-09-16 22:15:00 | AUTH_SUCCESS | operator_sudhrshan | IP: 192.168.1.12",
    "LOG-ID: 9002 | 2026-09-16 22:18:22 | DISK_CRITICAL | system_alert       | Space: 98% Full",
    "LOG-ID: 9003 | 2026-09-16 22:20:05 | SECURITY_WARN | malicious_ip       | IP: 185.220.10.4",
    "LOG-ID: 9004 | 2026-09-16 22:25:40 | AUTH_FAILURE  | unknown_user       | IP: 10.0.0.5"
]

def run_data_pipeline(raw_logs):
    """
    EXTRACTS raw text strings, TRANSFORMS attributes by cleaning anomalies,
    and LOADS them by auto-generating production-ready relational SQL insertion scripts.
    """
    print(f"-- INITIATING DATA EXTRACTION & PIPELINE COMPLIANCE AUDIT --")
    print(f"Execution Clock: {datetime.datetime.now()}\n")
    
    generated_sql_statements = []
    
    # PHASE 2: DATA TRANSFORMATION & FILTERING LOGIC
    for raw_entry in raw_logs:
        # Parse data blocks separated by the pipe symbol
        segments = [seg.strip() for seg in raw_entry.split("|")]
        
        # Clean up individual parameter strings
        log_id = segments[0].replace("LOG-ID: ", "")
        timestamp = segments[1]
        event_type = segments[2]
        user_identity = segments[3]
        metric_details = segments[4]
        
        # Determine strict database operational categorization
        if "CRITICAL" in event_type or "WARN" in event_type:
            severity_rank = "HIGH_PRIORITY"
        else:
            severity_rank = "NORMAL_OPERATIONAL"
            
        # PHASE 3: DATA LOADING (Auto-Generating SQL Relational Statements)
        sql_insert = (
            f"INSERT INTO system_security_logs "
            f"(log_ref, timestamp_logged, event_code, initiated_by, details, audit_tier) "
            f"VALUES ({log_id}, '{timestamp}', '{event_type}', '{user_identity}', '{metric_details}', '{severity_rank}');"
        )
        generated_sql_statements.append(sql_insert)

    # Output the production-ready script block
    print("/* ======================================================== */")
    print("/* AUTO-GENERATED SQL INSERTION SCRIPT FROM PYTHON PIPELINE  */")
    print("/* ======================================================== */\n")
    
    for statement in generated_sql_statements:
        print(statement)
        
    print(f"\n[SUCCESS] Successfully parsed and converted {len(raw_logs)} records into structured SQL injections.")

if __name__ == "__main__":
    run_data_pipeline(RAW_DATA_STREAM)
