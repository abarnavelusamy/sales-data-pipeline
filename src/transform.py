from logger import logger


def transform_data(customers, products, orders):

    logger.info("Starting transformation")

    df = orders.merge(customers, on="CustomerID")

    df = df.merge(products, on="ProductID")

    df["TotalAmount"] = df["Quantity"] * df["Price"]

    df["CustomerName"] = df["CustomerName"].str.upper()

    logger.info("Transformation completed")

    return df