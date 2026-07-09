# from logger import logger


# def validate_data(df):

#     logger.info("Starting validation")

#     if df["CustomerID"].isnull().any():
#         raise Exception("CustomerID contains NULL values")

#     if df["OrderID"].duplicated().any():
#         raise Exception("Duplicate OrderID found")

#     if (df["Price"] <= 0).any():
#         raise Exception("Price must be greater than zero")

#     if (df["Quantity"] <= 0).any():
#         raise Exception("Quantity must be greater than zero")

#     logger.info("Validation passed")

#     return True

from logger import logger


def validate_source_data(customers, products, orders):
    """
    Validate source CSV files before transformation.
    """

    logger.info("Starting source validation")

    # ----------------------------
    # Customers
    # ----------------------------

    if customers["CustomerID"].isnull().any():
        raise Exception("CustomerID contains NULL values")

    if customers["CustomerID"].duplicated().any():
        raise Exception("Duplicate CustomerID found")

    # ----------------------------
    # Products
    # ----------------------------

    if products["ProductID"].isnull().any():
        raise Exception("ProductID contains NULL values")

    if products["ProductID"].duplicated().any():
        raise Exception("Duplicate ProductID found")

    if (products["Price"] <= 0).any():
        raise Exception("Price must be greater than zero")

    # ----------------------------
    # Orders
    # ----------------------------

    if orders["OrderID"].isnull().any():
        raise Exception("OrderID contains NULL values")

    if orders["OrderID"].duplicated().any():
        raise Exception("Duplicate OrderID found")

    if orders["CustomerID"].isnull().any():
        raise Exception("Orders contain NULL CustomerID")

    if orders["ProductID"].isnull().any():
        raise Exception("Orders contain NULL ProductID")

    if (orders["Quantity"] <= 0).any():
        raise Exception("Quantity must be greater than zero")

    logger.info("Source validation completed")


def validate_transformed_data(df):
    """
    Validate transformed dataframe.
    """

    logger.info("Starting transformed data validation")

    if df.empty:
        raise Exception("Transformed dataframe is empty")

    if "TotalAmount" not in df.columns:
        raise Exception("TotalAmount column missing")

    if (df["TotalAmount"] <= 0).any():
        raise Exception("Invalid TotalAmount")

    logger.info("Transformation validation completed")

    return True