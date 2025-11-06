# 💻 Python Store Inventory CLI

This is a simple command-line interface (CLI) application for managing a store's product inventory and processing orders. It is built using **Python** and structured around core Object-Oriented Programming (OOP) principles, featuring classes for **Products**, the **Store**, and a dedicated **Menu** system.

-----

## ✨ Features

  * **Product Management:** Define products with a name, price, and quantity.
  * **Stock Tracking:** Get the total quantity of all items currently in stock.
  * **Order Processing:** Calculate the total cost of a customer's shopping list and reduce the stock quantity of purchased items.
  * **Stock Control:** Products are automatically deactivated if their quantity drops to zero or below.
  * **Error Handling:** Custom exceptions are implemented to handle invalid input and insufficient stock.
  * **Menu-Driven Interface:** Easy interaction via a custom, formatted text menu.

-----

## 📂 File Structure

The project is divided into several modules for clear separation of concerns:

| File | Description |
| :--- | :--- |
| **`main.py`** | The **entry point** of the application. It initializes the `Store` with a starting list of `Product` objects, creates the CLI `Menu`, and starts the main interaction loop. |
| **`store.py`** | Defines the **`Store` class** responsible for managing the product inventory (`_stock`), including methods for adding/removing products, listing active products, and processing orders. |
| **`products.py`** | Defines the **`Product` class** and custom exceptions. This class holds product details (name, price, quantity) and methods to manage its status and stock, like `buy()` and `deactivate()`. |
| **`menu.py`** | Contains the **`Menu` class** and the **`MenuObject` dataclass** for creating a reusable, structured, and displayable text menu. |

-----

## ▶️ Getting Started

### Prerequisites

  * Python 3+

### Running the Application

1.  Clone or download the project files.

2.  Navigate to the project directory in your terminal.

3.  Run the main script:

    ```bash
    python main.py
    ```

### Initial Inventory

The store is initialized with the following products:

| Product | Price | Quantity |
| :--- | :--- | :--- |
| **MacBook Air M2** | 1450 | 100 |
| **Bose QuietComfort Earbuds** | 250 | 500 |
| **Google Pixel 7** | 500 | 250 |

-----

## 🚀 How to Use

Upon starting, you will be presented with the main menu:

```
Store Menu
----------
1. List all products in store
2. show total amount in store
3. Make an order
4. Quit
Please choose a number:
```

Enter the corresponding number for the action you want to perform.

### Making an Order (Option 3)

1.  Select **3** from the main menu.
2.  The program will display the current list of available products with their corresponding number.
3.  Enter the **product number** you wish to buy, followed by the **quantity**.
4.  The product and quantity will be added to your shopping list.
5.  To finish the order, enter an **empty input** for either the product number or amount.
6.  The total payment will be displayed, and the stock will be updated.
