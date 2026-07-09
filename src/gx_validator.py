# import great_expectations as gx
# from logger import logger


# def validate_customers(df):
#     """
#     Validate Customers DataFrame using Great Expectations
#     """

#     logger.info("Starting Great Expectations validation for Customers")

#     # Convert Pandas DataFrame into a GX DataFrame
#     gx_df = gx.from_pandas(df)

#     validation_results = []

#     validation_results.append(
#         gx_df.expect_column_values_to_not_be_null("CustomerID")
#     )

#     validation_results.append(
#         gx_df.expect_column_values_to_be_unique("CustomerID")
#     )

#     validation_results.append(
#         gx_df.expect_column_values_to_not_be_null("CustomerName")
#     )

#     validation_results.append(
#         gx_df.expect_column_values_to_not_be_null("Email")
#     )

#     validation_results.append(
#         gx_df.expect_column_values_to_match_regex(
#             "Email",
#             r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
#         )
#     )

#     validation_results.append(
#         gx_df.expect_column_values_to_not_be_null("JoinDate")
#     )

#     # Check whether every expectation passed
#     all_passed = all(result.success for result in validation_results)

#     if all_passed:
#         logger.info("Customer validation PASSED")
#     else:
#         logger.error("Customer validation FAILED")

#     return all_passed



import yaml
import great_expectations as gx

from logger import logger


# --------------------------------------------------------
# Load validation rules from YAML
# --------------------------------------------------------

with open("config/validation_rules.yml", "r") as file:
    VALIDATION_RULES = yaml.safe_load(file)


# --------------------------------------------------------
# Generic Validator
# --------------------------------------------------------

def validate_dataframe(df, table_name):

    logger.info(f"Starting Great Expectations validation for [{table_name}]")

    gx_df = gx.from_pandas(df)

    rules = VALIDATION_RULES.get(table_name)

    if rules is None:
        raise Exception(f"No validation rules found for '{table_name}'")

    validation_results = []

    for rule in rules:

        expectation = rule["expectation"]

        column = rule["column"]

        # --------------------------
        # NOT NULL
        # --------------------------

        if expectation == "not_null":

            result = gx_df.expect_column_values_to_not_be_null(column)

        # --------------------------
        # UNIQUE
        # --------------------------

        elif expectation == "unique":

            result = gx_df.expect_column_values_to_be_unique(column)

        # --------------------------
        # REGEX
        # --------------------------

        elif expectation == "regex":

            result = gx_df.expect_column_values_to_match_regex(
                column,
                rule["pattern"]
            )

        # --------------------------
        # GREATER THAN
        # --------------------------

        elif expectation == "greater_than":

            result = gx_df.expect_column_values_to_be_between(
                column,
                min_value=rule["value"],
                strict_min=True
            )

        else:

            raise Exception(
                f"Unsupported expectation : {expectation}"
            )

        validation_results.append(result)

    passed = sum(result.success for result in validation_results)

    failed = len(validation_results) - passed

    logger.info(
        f"{table_name} : {passed} Passed | {failed} Failed"
    )

    success = failed == 0

    if success:
        logger.info(f"{table_name} validation PASSED")
    else:
        logger.error(f"{table_name} validation FAILED")

    return {
        "success": success,
        "table": table_name,
        "total_rules": len(validation_results),
        "passed": passed,
        "failed": failed,
        "results": validation_results
    }