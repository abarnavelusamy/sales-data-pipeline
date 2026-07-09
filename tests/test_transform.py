import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from extract import extract_data
from transform import transform_data


def test_transform():

    customers, products, orders = extract_data()

    df = transform_data(customers, products, orders)

    assert "TotalAmount" in df.columns

    first = df.iloc[0]

    assert first["TotalAmount"] == first["Quantity"] * first["Price"]

    assert first["CustomerName"] == first["CustomerName"].upper()