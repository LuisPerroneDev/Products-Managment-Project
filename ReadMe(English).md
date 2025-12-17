### Product Management System in Python

Main project: inventario_db_compro_clever.py

Exercise: gestion_de_productos.py

# Description

This is a simple product management system built in Python that uses an SQLite database to store and manage product information. The system allows the following operations:

Add products: Enter new products with details such as name, description, category, quantity, and price.
List products: Display all registered products in the database.
Update products: Modify the details of an existing product.
Delete products: Remove products by their ID.
Search products: Search for products by name.
Low stock report: Display products whose stock is below a set minimum value.
The system also handles data input errors and validates that values are correct before storing them in the database.

### Requirements

Python 3.x
Libraries:
sqlite3 (To manage the SQLite database)
colorama (To add color and formatting to the text interface)

# You can install colorama using pip:

````bash
pip install colorama || pip3 install colorama

## Database Structure

The database is an SQLite file named database.db and contains a table called products with the following fields:

id: Unique product identifier (primary key, auto-incremented).
name: Product name (unique).
description: Product description.
category: Product category.
quantity: Available stock quantity.
price: Product price.

# The code includes an initial check to ensure the table exists, creating it if necessary.

Features

1. Add Products
   Allows users to enter new products into the database. The system validates that the product name does not already exist.

Process:

Enter the product name.
Enter the product description.
Enter the category.
Enter the stock quantity.
Enter the price. 2. List Products
Displays a complete list of stored products, showing their ID, name, description, category, quantity, and price.

3. Update Products
   Allows updating product details. The user must select the product ID to modify and then can change the fields: name, description, category, quantity, and price.

4. Delete Products
   Allows users to remove a product from the database using its ID.

5. Search Products
   Allows searching for a product by name. If the product exists, its details are displayed. If not found, the system notifies the user.

6. Low Stock Report
   Generates a report of products whose stock is below a minimum value set by the user.

Main Menu
When running the program, an interactive menu is displayed with the following options:

Add new products
View all products
Update products
Delete products
Search products by name
Low stock report
Exit
The system only accepts numbers from 1 to 7 as valid options. If an invalid option is entered, the system will display an error message and request a valid input.

Error Handling
The program is designed to handle common errors, such as:

Invalid data entry: If the user enters a non-numeric value where a number is required (e.g., quantity or price), the system will prompt for a valid input.
Duplicate products: If a user attempts to add a product with a name that already exists, the system will notify the user and request a new name.
Empty fields: The system ensures that description and category fields are not left empty.

## Usage Instructions

Clone or download this project to your local machine.

# Install the necessary dependencies using pip:

```bash
pip or pip3 install colorama

## Run

### Main project — Inventory (SQLite + Colorama)

```bash
python inventario_db_compro_clever.py

Follow the on-screen instructions to perform operations.

Example Output

When running the program, the initial menu may look like this:

---

Welcome to the Product Management Menu - Compro Clever
\---------------------------------------------------/

1.  Add new products
2.  View all products
3.  Update products
4.  Delete products
5.  Search products
6.  Low stock report
7.  Exit
    If you choose to add a new product, you might see something like this:

mathematica
Copy
Edit
Enter the product name: Shirt
Enter the product description: Cotton shirt
Enter the product category: Clothing
Enter the stock quantity: 100
Enter the product price: 25.50
Product 'Shirt' added successfully.

This system provides a simple and efficient way to manage product inventory while ensuring data integrity and usability.
````

# Exercise — Product management menu

python gestion_de_productos.py
