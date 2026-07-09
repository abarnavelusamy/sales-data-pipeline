import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from extract import extract_data


def test_extract_data():

    customers, products, orders = extract_data()

    assert customers.empty is False
    assert products.empty is False
    assert orders.empty is False

    assert "CustomerID" in customers.columns
    assert "ProductID" in products.columns
    assert "OrderID" in orders.columns