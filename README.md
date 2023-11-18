# Restaurant Ordering System 🌮

Welcome to BringMeFood, the Restaurant Ordering System project! This command-line application simulates a restaurant ordering system, providing features for customers, items, orders, and operations.

## Table of Contents

- [Classes](#classes)
- [Usage](#usage)
- [Options](#options)
- [Files](#files)
- [Contributing](#contributing)

## Classes

#### Customer
- Represents a customer with basic information.
- Subclasses include BronzeCustomer, SilverCustomer, and GoldCustomer.

#### BronzeCustomer
- Subclass of Customer with specific attributes and methods for bronze customers.

#### SilverCustomer
- Subclass of Customer with specific attributes and methods for silver customers.

#### GoldCustomer
- Subclass of Customer with specific attributes and methods for gold customers.

#### Item
- Represents an item with basic information.
- Subclasses include FoodDish, Drink, and Banquet.

#### FoodDish
- Subclass of Item representing a food dish.

#### Drink
- Subclass of Item representing a drink.

#### Banquet
- Subclass of Item representing a banquet, consisting of food dishes and drinks.

#### Order
- Represents a customer's order with information about the customer, item, and quantity.

#### Records
- Manages lists of customers and items.
- Provides methods to read customer and item information from files.
- Helps find customers and items in the lists.

#### Operations
- Main class that orchestrates the restaurant operations.
- Reads customer and item information from files.
- Provides options for ordering meals, displaying customer and item information, and adjusting rates.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/byte-bistro.git
    cd byte-bistro
    ```

2. **Run the program:**

    ```bash
    python byte_bistro.py
    ```

3. **Follow the on-screen instructions to interact with the system.**

## Options

- **Order a meal (Option 1):** Place a new order by entering customer and item details.
- **Display existing customer information (Option 2):** View information about all existing customers.
- **Display existing item information (Option 3):** View information about all existing items.
- **Order Meals via file (Option 4):** Load orders from a file and place them.
- **Adjust the service fee rate of all bronze customers (Option 5):** Change the service fee rate for bronze customers.
- **Adjust the discount rate of a gold customer (Option 6):** Change the discount rate for a specific gold customer.
- **Display all orders (Option 7):** View information about all placed orders.
- **Exit the program (Option 0):** Terminate the application.

## Files

- `customers.txt`: Contains information about customers, used during initialization.
- `items.txt`: Contains information about items (food dishes, drinks, banquets), used during initialization.
- `order_file.txt`: Sample order file for testing the "Order Meals via file" option.

## Project Structure

```plaintext
.
├── BringMeFood.py
├── customers.txt
├── items.txt
└── orders.txt
```

## Contributing

Contributions are welcome! If you find a bug or have an enhancement idea, please open an issue or submit a pull request.
