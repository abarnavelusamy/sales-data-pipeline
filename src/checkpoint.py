import time

from gx_validator import validate_dataframe
from report_generator import save_validation_history
from html_report import generate_html_report


# ==========================================================
# Source Validation Checkpoint
# ==========================================================

def run_source_checkpoint(customers, products, orders):
    """
    Runs validation on all source tables.
    """

    run_id = f"RUN_{int(time.time())}"

    validation_results = []

    # Customers
    validation_results.append(
        validate_dataframe(customers, "customers")
    )

    # Products
    validation_results.append(
        validate_dataframe(products, "products")
    )

    # Orders
    validation_results.append(
        validate_dataframe(orders, "orders")
    )

    # Save Validation History
    save_validation_history(
        run_id,
        validation_results
    )

    # Summary
    total_tables = len(validation_results)

    passed_tables = sum(
        result["success"]
        for result in validation_results
    )

    failed_tables = total_tables - passed_tables

    checkpoint_result = {

        "success": failed_tables == 0,

        "run_id": run_id,

        "total_tables": total_tables,

        "passed_tables": passed_tables,

        "failed_tables": failed_tables,

        "results": validation_results
    }

    # Generate HTML Report
    generate_html_report(
        checkpoint_result,
        "reports/source_validation_report.html"
    )

    return checkpoint_result


# ==========================================================
# Processed Data Validation Checkpoint
# ==========================================================

def run_processed_checkpoint(processed_orders):
    """
    Runs validation on transformed data.
    """

    run_id = f"RUN_{int(time.time())}"

    validation_results = []

    validation_results.append(
        validate_dataframe(
            processed_orders,
            "processed_orders"
        )
    )

    # Save Validation History
    save_validation_history(
        run_id,
        validation_results
    )

    # Summary
    total_tables = len(validation_results)

    passed_tables = sum(
        result["success"]
        for result in validation_results
    )

    failed_tables = total_tables - passed_tables

    checkpoint_result = {

        "success": failed_tables == 0,

        "run_id": run_id,

        "total_tables": total_tables,

        "passed_tables": passed_tables,

        "failed_tables": failed_tables,

        "results": validation_results
    }

    # Generate HTML Report
    generate_html_report(
        checkpoint_result,
        "reports/processed_validation_report.html"
    )

    return checkpoint_result