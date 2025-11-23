# Supermarket-Bill-Generation
Supermarket Billing System (Python)
A simple command-line supermarket billing system built in Python that lets a user select items, specify quantities, and automatically generates a formatted bill with GST and a final amount.

Overview

This project simulates a small supermarket checkout.
The program displays a predefined list of products with prices, lets the customer pick what to buy and quantity for each item, calculates the total and 5% GST, and prints a neat text invoice including date, customer name, line items, and final bill amount.

Features

Displays a fixed catalog of supermarket items (e.g., rice, sugar, oil, onions, etc.) with prices.

Allows the user to repeatedly select items and enter quantities using keyboard input.

Validates item names against the catalog and shows a message if an item is not available.
Calculates line-item prices, subtotal, 5% GST, and final payable amount.

Generates an itemized bill with serial number, item name, quantity, and price.

Prints customer name and the current date on the bill using the datetime module.

Shows a thank-you message at the end of billing.

Technologies / Tools Used

Programming language: Python 3

Standard library:

datetime (for printing the current date on the bill)

Environment: Any Python 3 interpreter (IDLE, VS Code, PyCharm, or terminal)

Steps to Install & Run

Ensure Python 3 is installed on your system.

Download or copy the Project.py file into a folder on your computer.

Open a terminal or command prompt in that folder.

Run the script with:
When prompted:

Enter your name.

Press 1 to display the list of available items.

For each loop:

Press 1 to buy an item or 2 to exit item selection.

If you choose 1, type the item name exactly as shown in the list.

Enter the quantity as an integer.

After adding items, respond Yes when asked can i bill the items Yes or No: to generate and view the bill in the console.

Instructions for Testing

Basic flow test

Run the script, enter a valid name, press 1 to see the list, buy 2–3 different valid items with small quantities, then enter Yes to bill and verify the totals and GST output.

Invalid item test

When asked for an item, type a name not in the list (e.g., Apple) and confirm that the program prints the “item is not available” message.

Exit during selection test

After viewing the list, in the loop choose 2 (exist) to stop adding items and then
attempt billing.

GST and total check

Manually compute:

Sum of each quantity * price to confirm the subtotal.

Check GST is 5% of subtotal.

Confirm final amount equals subtotal plus GST.

Format check

Confirm that the printed bill shows:

Supermarket name and location header.

Customer name and current date.

Table-like rows for each item with serial number, quantity, and price.

Total amount, GST amount, and final amount, followed by a thank-you line.
