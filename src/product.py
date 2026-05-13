"""
product.py

This module defines the Product class.
A Product represents one item stored in the inventory.
"""


class Product:
    def __init__(self, product_id, name, category, quantity, unit_price, supplier, reorder_level, last_updated):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = int(quantity)
        self.unit_price = float(unit_price)
        self.supplier = supplier
        self.reorder_level = int(reorder_level)
        self.last_updated = last_updated

    def total_value(self):
        return self.quantity * self.unit_price

    def is_low_stock(self):
        return self.quantity <= self.reorder_level

    def display(self):
        status = "LOW STOCK!" if self.is_low_stock() else "OK"
        print(f"""
  +-------------------------------------------------+
  | ID       : {self.product_id}
  | Name     : {self.name}
  | Category : {self.category}
  | Quantity : {self.quantity}  [{status}]
  | Price    : ${self.unit_price:.2f}
  | Value    : ${self.total_value():.2f}
  | Supplier : {self.supplier}
  | Reorder  : {self.reorder_level} units
  | Updated  : {self.last_updated}
  +-------------------------------------------------+""")

    def __str__(self):
        return f"[{self.product_id}] {self.name} | Qty: {self.quantity} | ${self.unit_price:.2f}"
