"""
inventory.py

This module contains all the functions for managing the inventory.
Each function takes the products list and performs one operation:
searching, adding, editing, deleting, sorting, or getting reports.
"""

from product import Product
from file_handler import save_products, today


# ── Search functions ─────────────────────────────────────────────────

def find_by_id(products, product_id):
    for p in products:
        if p.product_id.upper() == product_id.upper():
            return p
    return None


def search_by_name(products, keyword):
    results = []
    for p in products:
        if keyword.lower() in p.name.lower():
            results.append(p)
    return results


def filter_by_category(products, category):
    results = []
    for p in products:
        if p.category.lower() == category.lower():
            results.append(p)
    return results


def get_low_stock(products):
    low = []
    for p in products:
        if p.is_low_stock():
            low.append(p)
    # Sort by quantity ascending (lowest stock first)
    low.sort(key=lambda p: p.quantity)
    return low


# ── Sort functions ───────────────────────────────────────────────────

def sort_products(products, key):
    if key == "name":
        return sorted(products, key=lambda p: p.name.lower())
    elif key == "quantity":
        return sorted(products, key=lambda p: p.quantity)
    elif key == "price":
        return sorted(products, key=lambda p: p.unit_price)
    elif key == "category":
        return sorted(products, key=lambda p: p.category.lower())
    else:
        return products


# ── CRUD functions ───────────────────────────────────────────────────

def add_product(products, product_id, name, category, quantity, unit_price, supplier, reorder_level):
    if find_by_id(products, product_id) is not None:
        return False  # ID already taken

    new_product = Product(
        product_id    = product_id.upper(),
        name          = name,
        category      = category,
        quantity      = quantity,
        unit_price    = unit_price,
        supplier      = supplier,
        reorder_level = reorder_level,
        last_updated  = today()
    )
    products.append(new_product)
    save_products(products)
    return True


def delete_product(products, product_id):
    product = find_by_id(products, product_id)
    if product is None:
        return False

    products.remove(product)
    save_products(products)
    return True


def update_quantity(products, product_id, new_quantity):
    product = find_by_id(products, product_id)
    if product is None:
        return False

    product.quantity = new_quantity
    product.last_updated = today()
    save_products(products)
    return True


def update_price(products, product_id, new_price):
    product = find_by_id(products, product_id)
    if product is None:
        return False

    product.unit_price = new_price
    product.last_updated = today()
    save_products(products)
    return True


# ── Report / summary functions ───────────────────────────────────────

def total_inventory_value(products):
    total = 0
    for p in products:
        total += p.total_value()
    return total


def get_next_id(products):
    if not products:
        return "P001"

    # Get all numeric parts of existing IDs
    numbers = []
    for p in products:
        try:
            numbers.append(int(p.product_id[1:]))  # strip the 'P' prefix
        except ValueError:
            pass

    next_number = max(numbers) + 1
    return f"P{next_number:03d}"
