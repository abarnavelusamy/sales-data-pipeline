import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_DIR = os.path.join(BASE_DIR, "data", "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

CUSTOMER_FILE = os.path.join(INPUT_DIR, "customers.csv")
PRODUCT_FILE = os.path.join(INPUT_DIR, "products.csv")
ORDER_FILE = os.path.join(INPUT_DIR, "orders.csv")

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "processed_orders.csv")

LOG_FILE = os.path.join(LOG_DIR, "pipeline.log")