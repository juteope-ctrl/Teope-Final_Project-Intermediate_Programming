# Teope-Final_Project-Intermediate_Programming
# Project Name: Inventory Management System
This is a Command Line Interface (CLI) application built purely with Python to help manage product inventory. It's designed to be a practical tool for keeping track of products, stock levels, sales, and generating useful reports.

This project allows users to manage products, track stock quantities, search and filter items, generate reports, and automatically save inventory data using CSV file handling.

---

# Features

## Product Management
* See all items currently in inventory.
* Easily add new products with all their details.
* Update information for existing products.
* Remove products that are no longer needed.

## Search & Filter
* Quickly find products using their names.
* View products belonging to specific categories (e.g., Electronics, Furniture).
* Organize product lists by various criteria:

  * Name
  * Price
  * Quantity
  * Inventory value

## Stock Management
* Add more units to existing product stock.
* Decrease stock quantity when a product is sold.
* Manually set the precise stock level for an item.
* Get notifications for products that are running low and need reordering.
## Reports

* A complete list of all products and their details.
* Summarizes stock and value for each product category.
* Identifies the products with the highest total value in stock.
* Provides overall insights and sorting options for reports.

## File Handling
* All changes made to the inventory are automatically saved to a CSV file.
* Inventory data is loaded from the CSV file every time the program starts, so your changes are always there.

---

# Technologies Used
* Python 3.8+
* Object-Oriented Programming (OOP)
* CSV File Handling
* Lists and Dictionaries
* Functions and Modular Programming
* Sorting using `sorted()` and `lambda`

No third-party libraries required.

---

# Project Structure
```
inventory_system/
├── src/
│   ├── main.py            # Main application entry point and menu handler
│   ├── product.py         # Defines the Product class
│   ├── inventory.py       # Manages inventory operations and business logic
│   └── file_handler.py    # Handles all CSV reading and writing operations
│
├── data/
│   └── sample_data.csv    # Sample data file for testing (or actual inventory)
│
├── requirements.txt       # Lists project dependencies (none for this project)
├── .gitignore             # Specifies files/folders to ignore in Git
└── README.md              # This documentation file
```

---

# File Descriptions
| File              | Description                             |
| ----------------- | --------------------------------------- |
| `main.py`         | Main program and menu system            |
| `product.py`      | Contains the `Product` class            |
| `inventory.py`    | Inventory operations and business logic |
| `file_handler.py` | Handles CSV reading and writing         |
| `sample_data.csv` | Stores inventory data                   |

---

# Python Concepts Demonstrated
| Concept            | Usage                        |
| ------------------ | ---------------------------- |
| Classes & Objects  | `Product` class              |
| File Handling      | CSV read/write operations    |
| Functions          | Modular program structure    |
| Lists & Loops      | Inventory processing         |
| Sorting Algorithms | `sorted()` with lambda       |
| Input Validation   | Integer and float validation |
| String Methods     | Searching and filtering      |
| CRUD Operations    | Create, Read, Update, Delete |

---

# Installation & Setup
## Requirements

* Python 3.8 or higher is needed to run this application.

* No external packages are required!

---

## Clone the Repository

```bash
git clone https://github.com/<YourUsername>/inventory_system.git
cd inventory_system
```

---

## Run the Program
```bash
python src/main.py
```

---

# Sample Menu
```
=====================================================
     INVENTORY MANAGEMENT SYSTEM  v1.0
     CLI Application - Python Final Project
=====================================================

Loaded N products from file.

-----------------------------------------------------
MAIN MENU
-----------------------------------------------------
1. View all products
2. Search / Filter products
3. Add a new product
4. Edit a product
5. Delete a product
6. Adjust stock quantity
7. Reports & Summary
0. Exit
-----------------------------------------------------
Enter your choice:
```

---

# Sample Data
The system comes with a sample_data.csv file that contains 20 pre-populated products across various categories. This makes it easy to test out all the features right away!

## Categories Included
| Category    | Example Products             |
| ----------- | ---------------------------- |
| Electronics | Webcam, Monitor, USB-C Hub   |
| Furniture   | Office Chair, Standing Desk  |
| Stationery  | Printer Paper, Pens, Stapler |

---

# Example CSV Format
The sample_data.csv (and any new data saved) follows this structure:

```csv
name,category,quantity,price,supplier,reorder_level
Wireless Keyboard,Electronics,25,1499.99,TechSource,5
Office Chair,Furniture,10,5999.99,FurniCo,2
Printer Paper,Stationery,100,299.50,OfficePlus,20
```

---

# How the System Works
1. When you run main.py, it first loads product data from data/sample_data.csv.
2. It then presents the main menu and waits for your input.
3. Based on your choice, the program calls functions in inventory.py to perform tasks like adding, editing, or viewing products.
4. After any change made to the inventory, file_handler.py automatically writes the updated data back to the CSV file.
5. This cycle continues until you select the "Exit" option.

---

# Learning Objectives
This project demonstrates understanding of:

* Object-Oriented Programming
* File Handling in Python
* Modular Programming
* Data Validation
* Search and Sorting Algorithms
* Command Line Interface Design
* CRUD System Development

---

# Screenshots

## Main Menu

<img width="571" height="482" alt="Screenshot 2026-05-14 030516" src="https://github.com/user-attachments/assets/995eaf1e-f264-4803-bedf-9b4bae568d34" />


## Product List

<img width="596" height="628" alt="Screenshot 2026-05-14 030540" src="https://github.com/user-attachments/assets/1eba60b7-d32d-439a-a8ca-bf6280acbb67" />


## Reports Section

<img width="598" height="670" alt="Screenshot 2026-05-14 030613" src="https://github.com/user-attachments/assets/9b8f7d8c-0df2-44cb-8be2-16eecef84538" />


---

# Video Demonstration
YouTube Demo Link:
https://youtu.be/1KZ9Rqx0GbU?si=hgbpbzvELFrgrPOi


---

# Author
Name: Teope, Juzzua Phillip A.  
1st Year BS Computer Science Student Section 1B
---

# License
This project is for educational purposes only.
