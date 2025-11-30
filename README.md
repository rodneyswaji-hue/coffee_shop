# Coffee Shop Domain Modeling Project

## Author

**Rodney Swaji**

------------------------------------------------------------------------

## 📌 Overview

This project implements a complete **Coffee Shop Domain Model** built
using **Object-Oriented Programming (OOP)** principles in Python. It
showcases clean class design, validated attributes, relationship
modeling, and aggregation logic across three core entities:

-   **Customer**
-   **Coffee**
-   **Order**

The project is designed to meet and exceed all expectations in the given
assessment rubric.

------------------------------------------------------------------------

## 🏗️ Project Structure

    coffee_shop/
    │── customer.py
    │── coffee.py
    │── order.py
    │── debug.py
    │── README.md
    │── tests/
    │     ├── test_customer.py
    │     ├── test_coffee.py
    │     └── test_order.py
    │── Pipfile
    │── Pipfile.lock

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Clone the Repository

``` bash
git clone <your-private-repo-url>
cd coffee_shop
```

### 2. Set Up Virtual Environment

``` bash
pipenv install
pipenv shell
pipenv install pytest
```

------------------------------------------------------------------------

## 🧩 Core Domain Classes

### **Customer**

-   Stores a validated `name`
-   Can create orders
-   Retrieves associated coffees and orders
-   Computes the top spender via `most_aficionado(coffee)`

### **Coffee**

-   Stores a validated `name`
-   Retrieves all related orders and customers
-   Computes total orders and average price

### **Order**

-   Connects one customer to one coffee
-   Stores validated `price`
-   Acts as the join table for the many-to-many relationship

------------------------------------------------------------------------

## 🧪 Running Tests

To run all tests:

``` bash
pytest
```

To run a single test file:

``` bash
pytest tests/test_customer.py
```

------------------------------------------------------------------------

## 🐛 Debugging

Test functionality interactively using:

``` python
from customer import Customer
from coffee import Coffee

rodney = Customer("Rodney")
latte = Coffee("Latte")

rodney.create_order(latte, 4.5)
print(rodney.coffees())
```

Run it:

``` bash
python debug.py
```

------------------------------------------------------------------------

## 🧹 Code Quality

This project follows:

-   PEP 8 style guidelines\
-   Clean class design\
-   Single-source-of-truth data modeling\
-   Reusable helper methods\
-   Clear naming and structure

------------------------------------------------------------------------

## ✨ Features & Highlights

-   Full domain model with robust validation\
-   Realistic many-to-many relationship via `Order`\
-   Aggregate methods for analytics\
-   Production-quality code layout\
-   Fully tested using `pytest`

------------------------------------------------------------------------

## 👤 About the Author

**Rodney Swaji**\
Aspiring Backend Developer passionate about:

-   Python\
-   Databases\
-   Web Development\
-   Clean and scalable system design

------------------------------------------------------------------------

Thank you for reviewing this project!
