"""
file_handler.py

This module handles reading and writing inventory data to a CSV file.
It loads products from the file at startup and saves them whenever
something changes.
"""

import csv
import os
from datetime import date
from product import Product


DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "sample_data.csv")

FIELDNAMES = ["product_id", "name", "category", "quantity",
              "unit_price", "supplier", "reorder_level", "last_updated"]


def load_products():
    products = []

    if not os.path.exists(DATA_FILE):
        print("ERROR: Data file not found:", DATA_FILE)
        return products

    with open(DATA_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = Product(
                product_id   = row["product_id"],
                name         = row["name"],
                category     = row["category"],
                quantity     = row["quantity"],
                unit_price   = row["unit_price"],
                supplier     = row["supplier"],
                reorder_level= row["reorder_level"],
                last_updated = row["last_updated"]
            )
            products.append(p)

    return products


def save_products(products):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for p in products:
            writer.writerow({
                "product_id"   : p.product_id,
                "name"         : p.name,
                "category"     : p.category,
                "quantity"     : p.quantity,
                "unit_price"   : p.unit_price,
                "supplier"     : p.supplier,
                "reorder_level": p.reorder_level,
                "last_updated" : p.last_updated
            })


def today():
    return str(date.today())
