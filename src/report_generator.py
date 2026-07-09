import os
import pandas as pd
from datetime import datetime


REPORT_FILE = "reports/validation_history.csv"


def save_validation_history(run_id, validation_results):

    rows = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for result in validation_results:

        rows.append({
            "Run_ID": run_id,
            "Timestamp": timestamp,
            "Table": result["table"],
            "Total_Rules": result["total_rules"],
            "Passed": result["passed"],
            "Failed": result["failed"],
            "Status": "PASS" if result["success"] else "FAIL"
        })

    new_df = pd.DataFrame(rows)

    # First run (or empty file)
    if (
        not os.path.exists(REPORT_FILE)
        or os.path.getsize(REPORT_FILE) == 0
    ):
        new_df.to_csv(REPORT_FILE, index=False)
        return

    old_df = pd.read_csv(REPORT_FILE)

    final_df = pd.concat([old_df, new_df], ignore_index=True)

    final_df.to_csv(REPORT_FILE, index=False)