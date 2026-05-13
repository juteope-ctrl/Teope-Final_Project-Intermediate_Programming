"""
main.py

Entry point for the Inventory Management System.
Run this file to start the program:

    python src/main.py

This file contains the menu system and user input handling.
It connects the user interface to the inventory functions.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from file_handler import load_products
from inventory import (
    find_by_id, search_by_name, filter_by_category,
    get_low_stock, sort_products,
    add_product, delete_product, update_quantity, update_price,
    total_inventory_value, get_next_id
)


def get_int(prompt, min_val=0):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"  Please enter a number {min_val} or higher.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 29.99).")


def get_category():
    categories = ["Electronics", "Stationery", "Furniture"]
    print("  Categories:")
    for i, cat in enumerate(categories, start=1):
        print(f"    {i}. {cat}")
    while True:
        choice = input("  Choose a number (1-3): ").strip()
        if choice == "1":
            return "Electronics"
        elif choice == "2":
            return "Stationery"
        elif choice == "3":
            return "Furniture"
        else:
            print("  Please enter 1, 2, or 3.")


def print_line():
    print("  " + "-" * 55)


def print_product_table(products):
    if not products:
        print("  No products found.")
        return

    print()
    print(f"  {'ID':<7} {'Name':<30} {'Qty':>5} {'Price':>8} {'Status'}")
    print_line()
    for p in products:
        status = "LOW!" if p.is_low_stock() else "OK"
        print(f"  {p.product_id:<7} {p.name:<30} {p.quantity:>5} ${p.unit_price:>7.2f} {status}")
    print_line()
    print(f"  Total: {len(products)} product(s)")
    print()


# Menu screens

def show_banner():
    print()
    print("  =====================================================")
    print("       INVENTORY MANAGEMENT SYSTEM  v1.0")
    print("       CLI Application - Python Final Project")
    print("  =====================================================")
    print()


def show_main_menu():
    print()
    print_line()
    print("  MAIN MENU")
    print_line()
    print("  1. View all products")
    print("  2. Search / Filter products")
    print("  3. Add a new product")
    print("  4. Edit a product")
    print("  5. Delete a product")
    print("  6. Adjust stock quantity")
    print("  7. Reports & Summary")
    print("  0. Exit")
    print_line()


# Feature handlers

def view_all_products(products):
    print("\n  ALL PRODUCTS")
    sorted_list = sort_products(products, "name")
    print_product_table(sorted_list)


def handle_search(products):
    print()
    print_line()
    print("  SEARCH & FILTER")
    print_line()
    print("  1. Search by name")
    print("  2. Filter by category")
    print("  3. Show low-stock items only")
    print("  0. Back")
    print_line()

    choice = input("  Choose: ").strip()

    if choice == "1":
        keyword = input("  Enter keyword: ").strip()
        if not keyword:
            print("  Please enter a keyword.")
            return
        results = search_by_name(products, keyword)
        print(f"\n  Search results for '{keyword}':")
        print_product_table(results)

    elif choice == "2":
        category = get_category()
        results = filter_by_category(products, category)
        print(f"\n  Products in '{category}':")
        print_product_table(results)

    elif choice == "3":
        results = get_low_stock(products)
        print("\n  LOW STOCK ITEMS:")
        print_product_table(results)
        if not results:
            print("  All products are sufficiently stocked!")

    elif choice == "0":
        return
    else:
        print("  Invalid choice.")


def handle_add_product(products):
    print()
    print_line()
    print("  ADD NEW PRODUCT")
    print_line()

    suggested_id = get_next_id(products)
    print(f"  Suggested ID: {suggested_id}")

    product_id = input("  Product ID (e.g. P021): ").strip().upper()
    if not product_id:
        print("  Product ID cannot be empty.")
        return

    if find_by_id(products, product_id) is not None:
        print(f"  Error: Product ID '{product_id}' already exists.")
        return

    name          = input("  Product Name: ").strip()
    if not name:
        print("  Name cannot be empty.")
        return

    category      = get_category()
    quantity      = get_int("  Quantity: ", min_val=0)
    unit_price    = get_float("  Unit Price ($): ")
    supplier      = input("  Supplier Name: ").strip()
    reorder_level = get_int("  Reorder Level: ", min_val=0)

    confirm = input(f"\n  Add '{name}' to inventory? (y/n): ").strip().lower()
    if confirm != "y":
        print("  Cancelled.")
        return

    success = add_product(products, product_id, name, category,
                          quantity, unit_price, supplier, reorder_level)
    if success:
        print(f"\n  Product '{name}' added successfully!")
    else:
        print("  Failed to add product. ID may already exist.")


def handle_edit_product(products):
    print()
    print_line()
    print("  EDIT PRODUCT")
    print_line()

    product_id = input("  Enter Product ID to edit: ").strip().upper()
    product = find_by_id(products, product_id)

    if product is None:
        print(f"  Product '{product_id}' not found.")
        return

    product.display()

    print("  What would you like to edit?")
    print("  1. Product Name")
    print("  2. Category")
    print("  3. Unit Price")
    print("  4. Supplier")
    print("  5. Reorder Level")
    print("  0. Back")

    choice = input("  Choose: ").strip()

    if choice == "1":
        new_name = input("  New Name: ").strip()
        if new_name:
            product.name = new_name
            from file_handler import save_products, today
            product.last_updated = today()
            save_products(products)
            print(f"  Name updated to '{new_name}'.")
        else:
            print("  Name cannot be empty.")

    elif choice == "2":
        product.category = get_category()
        from file_handler import save_products, today
        product.last_updated = today()
        save_products(products)
        print(f"  Category updated to '{product.category}'.")

    elif choice == "3":
        new_price = get_float("  New Unit Price ($): ")
        success = update_price(products, product_id, new_price)
        if success:
            print(f"  Price updated to ${new_price:.2f}.")

    elif choice == "4":
        new_supplier = input("  New Supplier: ").strip()
        if new_supplier:
            product.supplier = new_supplier
            from file_handler import save_products, today
            product.last_updated = today()
            save_products(products)
            print(f"  Supplier updated to '{new_supplier}'.")
        else:
            print("  Supplier name cannot be empty.")

    elif choice == "5":
        new_level = get_int("  New Reorder Level: ", min_val=0)
        product.reorder_level = new_level
        from file_handler import save_products, today
        product.last_updated = today()
        save_products(products)
        print(f"  Reorder level updated to {new_level}.")

    elif choice == "0":
        return
    else:
        print("  Invalid choice.")


def handle_delete_product(products):
    print()
    print_line()
    print("  DELETE PRODUCT")
    print_line()

    product_id = input("  Enter Product ID to delete: ").strip().upper()
    product = find_by_id(products, product_id)

    if product is None:
        print(f"  Product '{product_id}' not found.")
        return

    product.display()
    confirm = input(f"  Are you sure you want to delete '{product.name}'? (y/n): ").strip().lower()

    if confirm == "y":
        success = delete_product(products, product_id)
        if success:
            print(f"  Product '{product_id}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


def handle_adjust_quantity(products):
    print()
    print_line()
    print("  ADJUST STOCK QUANTITY")
    print_line()

    product_id = input("  Enter Product ID: ").strip().upper()
    product = find_by_id(products, product_id)

    if product is None:
        print(f"  Product '{product_id}' not found.")
        return

    print(f"  Product: {product.name}")
    print(f"  Current Quantity: {product.quantity}")
    print()
    print("  1. Add stock (restock)")
    print("  2. Remove stock (sold/used)")
    print("  3. Set exact quantity")
    print("  0. Back")

    choice = input("  Choose: ").strip()

    if choice == "1":
        amount = get_int("  How many to add: ", min_val=1)
        new_qty = product.quantity + amount
        update_quantity(products, product_id, new_qty)
        print(f"  Quantity updated: {product.quantity - amount} + {amount} = {new_qty}")

    elif choice == "2":
        amount = get_int("  How many to remove: ", min_val=1)
        if amount > product.quantity:
            print(f"  Error: Cannot remove {amount} — only {product.quantity} in stock.")
            return
        new_qty = product.quantity - amount
        update_quantity(products, product_id, new_qty)
        print(f"  Quantity updated: {product.quantity + amount} - {amount} = {new_qty}")

    elif choice == "3":
        new_qty = get_int("  Set quantity to: ", min_val=0)
        update_quantity(products, product_id, new_qty)
        print(f"  Quantity set to {new_qty}.")

    elif choice == "0":
        return
    else:
        print("  Invalid choice.")

    # Warn if now low on stock
    updated_product = find_by_id(products, product_id)
    if updated_product and updated_product.is_low_stock():
        print(f"  WARNING: '{updated_product.name}' is now at or below reorder level!")


def handle_reports(products):
    print()
    print_line()
    print("  REPORTS & SUMMARY")
    print_line()
    print("  1. Full inventory report")
    print("  2. Category summary")
    print("  3. Top 5 most valuable products")
    print("  4. Low stock report")
    print("  5. Sort products")
    print("  0. Back")
    print_line()

    choice = input("  Choose: ").strip()

    if choice == "1":
        # Full report
        total = total_inventory_value(products)
        print("\n  FULL INVENTORY REPORT")
        print_product_table(sort_products(products, "name"))
        print(f"  Total Inventory Value: ${total:,.2f}")

    elif choice == "2":
        # Category summary
        categories = ["Electronics", "Stationery", "Furniture"]
        print("\n  CATEGORY SUMMARY")
        print_line()
        for cat in categories:
            items = filter_by_category(products, cat)
            cat_value = sum(p.total_value() for p in items)
            cat_qty = sum(p.quantity for p in items)
            print(f"  {cat}:")
            print(f"    Products  : {len(items)}")
            print(f"    Total Qty : {cat_qty}")
            print(f"    Total Val : ${cat_value:,.2f}")
            print()

    elif choice == "3":
        # Top 5 by value
        sorted_by_value = sorted(products, key=lambda p: p.total_value(), reverse=True)
        top5 = sorted_by_value[:5]
        print("\n  TOP 5 PRODUCTS BY STOCK VALUE")
        print_line()
        for i, p in enumerate(top5, start=1):
            print(f"  #{i}  [{p.product_id}] {p.name}")
            print(f"       Value: ${p.total_value():,.2f}  (Qty: {p.quantity} x ${p.unit_price:.2f})")
        print()

    elif choice == "4":
        # Low stock
        low = get_low_stock(products)
        print("\n  LOW STOCK REPORT")
        print_line()
        if not low:
            print("  All products are sufficiently stocked.")
        else:
            for p in low:
                print(f"  [{p.product_id}] {p.name}")
                print(f"       Stock: {p.quantity} | Reorder Level: {p.reorder_level}")
            print()
            print(f"  {len(low)} product(s) need restocking.")
        print()

    elif choice == "5":
        # Sorting
        print("\n  Sort by:")
        print("  1. Name")
        print("  2. Quantity")
        print("  3. Price")
        print("  4. Category")
        sort_choice = input("  Choose: ").strip()
        sort_keys = {"1": "name", "2": "quantity", "3": "price", "4": "category"}
        if sort_choice in sort_keys:
            sorted_list = sort_products(products, sort_keys[sort_choice])
            print_product_table(sorted_list)
        else:
            print("  Invalid choice.")

    elif choice == "0":
        return
    else:
        print("  Invalid choice.")


# Main program loop

def main():
    show_banner()

    # Load products from CSV file
    products = load_products()
    print(f"  Loaded {len(products)} products from file.")

    # Warn if any products are low on stock
    low = get_low_stock(products)
    if low:
        print(f"  WARNING: {len(low)} product(s) are low on stock!")

    # Main loop - keep showing menu until user picks 0
    while True:
        show_main_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            view_all_products(products)

        elif choice == "2":
            handle_search(products)

        elif choice == "3":
            handle_add_product(products)

        elif choice == "4":
            handle_edit_product(products)

        elif choice == "5":
            handle_delete_product(products)

        elif choice == "6":
            handle_adjust_quantity(products)

        elif choice == "7":
            handle_reports(products)

        elif choice == "0":
            print("\n  Thank you for using the Inventory Management System!")
            print("  Goodbye!\n")
            break

        else:
            print("  Invalid choice. Please enter a number from the menu.")


# Run the program
if __name__ == "__main__":
    main()
