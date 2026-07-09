# import sys
# import os

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

# from extract import extract_data
# from transform import transform_data
# from validate import validate_data


# def test_validation():

#     customers, products, orders = extract_data()

#     df = transform_data(customers, products, orders)

#     assert validate_data(df) is True

import sys
import os
import pytest

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from extract import extract_data
from transform import transform_data
from validate import (
    validate_source_data,
    validate_transformed_data
)


# ==========================================================
# SUCCESS TEST
# ==========================================================

def test_validation_success():
    """
    Valid source data and transformed data should pass validation.
    """

    customers, products, orders = extract_data()

    validate_source_data(customers, products, orders)

    df = transform_data(customers, products, orders)

    assert validate_transformed_data(df) is True


# ==========================================================
# SOURCE VALIDATION TESTS
# ==========================================================

def test_duplicate_orderid():
    """
    Duplicate OrderID should fail.
    """

    customers, products, orders = extract_data()

    orders.loc[1, "OrderID"] = orders.loc[0, "OrderID"]

    with pytest.raises(Exception, match="Duplicate OrderID found"):
        validate_source_data(customers, products, orders)


def test_null_customerid():
    """
    NULL CustomerID should fail.
    """

    customers, products, orders = extract_data()

    customers.loc[0, "CustomerID"] = None

    with pytest.raises(Exception, match="CustomerID contains NULL values"):
        validate_source_data(customers, products, orders)


def test_null_productid():
    """
    NULL ProductID should fail.
    """

    customers, products, orders = extract_data()

    products.loc[0, "ProductID"] = None

    with pytest.raises(Exception, match="ProductID contains NULL values"):
        validate_source_data(customers, products, orders)


def test_null_orderid():
    """
    NULL OrderID should fail.
    """

    customers, products, orders = extract_data()

    orders.loc[0, "OrderID"] = None

    with pytest.raises(Exception, match="OrderID contains NULL values"):
        validate_source_data(customers, products, orders)


def test_negative_price():
    """
    Negative Price should fail.
    """

    customers, products, orders = extract_data()

    products.loc[0, "Price"] = -100

    with pytest.raises(Exception, match="Price must be greater than zero"):
        validate_source_data(customers, products, orders)


def test_zero_price():
    """
    Zero Price should fail.
    """

    customers, products, orders = extract_data()

    products.loc[0, "Price"] = 0

    with pytest.raises(Exception, match="Price must be greater than zero"):
        validate_source_data(customers, products, orders)


def test_negative_quantity():
    """
    Negative Quantity should fail.
    """

    customers, products, orders = extract_data()

    orders.loc[0, "Quantity"] = -5

    with pytest.raises(Exception, match="Quantity must be greater than zero"):
        validate_source_data(customers, products, orders)


def test_zero_quantity():
    """
    Zero Quantity should fail.
    """

    customers, products, orders = extract_data()

    orders.loc[0, "Quantity"] = 0

    with pytest.raises(Exception, match="Quantity must be greater than zero"):
        validate_source_data(customers, products, orders)


# ==========================================================
# TRANSFORM VALIDATION TESTS
# ==========================================================

def test_invalid_totalamount():
    """
    Invalid TotalAmount should fail.
    """

    customers, products, orders = extract_data()

    validate_source_data(customers, products, orders)

    df = transform_data(customers, products, orders)

    df.loc[0, "TotalAmount"] = -100

    with pytest.raises(Exception, match="Invalid TotalAmount"):
        validate_transformed_data(df)


def test_missing_totalamount_column():
    """
    Missing TotalAmount column should fail.
    """

    customers, products, orders = extract_data()

    validate_source_data(customers, products, orders)

    df = transform_data(customers, products, orders)

    df.drop(columns=["TotalAmount"], inplace=True)

    with pytest.raises(Exception, match="TotalAmount column missing"):
        validate_transformed_data(df)