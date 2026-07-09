# import time

# from logger import logger

# from extract import extract_data
# from transform import transform_data
# from validate import (
#     validate_source_data,
#     validate_transformed_data
# )
# from load import load_data
# from gx_validator import validate_customers


# def main():

#     start = time.time()

#     logger.info("Pipeline Started")

#     try:

#         customers, products, orders = extract_data()
 
#         if not validate_customers(customers):
#             raise Exception("Customer validation failed")
# # Validate source files
#         validate_source_data(customers, products, orders)

# # Transform data
#         df = transform_data(customers, products, orders)

# # Validate transformed data
#         validate_transformed_data(df)

# # Load output
#         load_data(df)

#         logger.info("Pipeline Completed Successfully")

#     except Exception as e:

#         logger.error(str(e))

#         print(e)

#     finally:

#         end = time.time()

#         logger.info(f"Execution Time : {round(end-start,2)} seconds")


# if __name__ == "__main__":
#     main()

import time

from logger import logger

from extract import extract_data
from transform import transform_data
from validate import (
    validate_source_data,
    validate_transformed_data
)
from load import load_data

from checkpoint import (
    run_source_checkpoint,
    run_processed_checkpoint
)


def main():

    start = time.time()

    logger.info("Pipeline Started")

    try:

        # -------------------------------------------------
        # Extract
        # -------------------------------------------------

        customers, products, orders = extract_data()

        # -------------------------------------------------
        # Great Expectations - Source Checkpoint
        # -------------------------------------------------

        source_checkpoint = run_source_checkpoint(
            customers,
            products,
            orders
        )

        if not source_checkpoint["success"]:
            raise Exception("Source Validation Checkpoint Failed")

        # -------------------------------------------------
        # Manual Source Validation
        # -------------------------------------------------

        validate_source_data(
            customers,
            products,
            orders
        )

        # -------------------------------------------------
        # Transform
        # -------------------------------------------------

        df = transform_data(
            customers,
            products,
            orders
        )

        # -------------------------------------------------
        # Great Expectations - Processed Checkpoint
        # -------------------------------------------------

        processed_checkpoint = run_processed_checkpoint(df)

        if not processed_checkpoint["success"]:
            raise Exception("Processed Validation Checkpoint Failed")

        # -------------------------------------------------
        # Manual Business Validation
        # -------------------------------------------------

        validate_transformed_data(df)

        # -------------------------------------------------
        # Load
        # -------------------------------------------------

        load_data(df)

        logger.info("Pipeline Completed Successfully")

    except Exception as e:

        logger.error(str(e))
        print(e)

    finally:

        end = time.time()

        logger.info(
            f"Execution Time : {round(end-start,2)} seconds"
        )


if __name__ == "__main__":
    main()