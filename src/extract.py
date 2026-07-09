import pandas as pd

from config import (
    CUSTOMER_FILE,
    PRODUCT_FILE,
    ORDER_FILE
)

from logger import logger


def extract_data():
    logger.info("Reading input files")

    customers = pd.read_csv(CUSTOMER_FILE)
    products = pd.read_csv(PRODUCT_FILE)
    orders = pd.read_csv(ORDER_FILE)

    logger.info(f"Customers : {len(customers)}")
    logger.info(f"Products  : {len(products)}")
    logger.info(f"Orders    : {len(orders)}")

    return customers, products, orders