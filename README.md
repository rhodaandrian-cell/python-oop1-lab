# Bookstore OOP Lab

A Python application that models a bookstore using Object-Oriented Programming (OOP) principles. The system defines two classes — `Book` and `Coffee` — each with attributes, properties, and methods.

---

## Features

- **Book class** — represents a book with a title and page count, with the ability to turn pages
- **Coffee class** — represents a coffee with a size and price, with the ability to add a tip
- **Property validation** — ensures correct data types and values are used
- **Modular structure** — each class lives in its own file inside `lib/`

---

## Project Structure

```
.
├── lib/
│   ├── book.py        # Book class definition
│   └── coffee.py      # Coffee class definition
├── testing/
│   ├── book_test.py   # Tests for the Book class
│   └── coffee_test.py # Tests for the Coffee class
├── run_demo.py        # Demo script to test outputs in terminal
├── Pipfile            # Project dependencies
└── README.md
```

---

## Setup

### Prerequisites

- Python 3.8+
- `pipenv` for virtual environment management

### Installation

```bash
# Clone the repository
git clone <your-fork-url>
cd <repo-folder>

# Install dependencies
pipenv install

# Activate the virtual environment
pipenv shell
```

---

## Usage

### Book

```python
from lib.book import Book

# Create a book
book = Book("The Great Gatsby", 180)
print(book.title)       # => The Great Gatsby
print(book.page_count)  # => 180

# Turn a page
book.turn_page()
# => Flipping the page...wow, you read fast!

# Invalid page_count
book2 = Book("Bad Book", "not a number")
# => page_count must be an integer
```

### Coffee

```python
from lib.coffee import Coffee

# Create a coffee
coffee = Coffee("Medium", 3.50)
print(coffee.size)   # => Medium
print(coffee.price)  # => 3.5

# Add a tip
coffee.tip()
# => This coffee is great, here's a tip!
print(coffee.price)  # => 4.5

# Invalid size
coffee2 = Coffee("Huge", 5.00)
# => size must be Small, Medium, or Large
```

---

## Running Tests

```bash
# Run all tests
pytest -x

# Run only Book tests
pytest -x testing/book_test.py

# Run only Coffee tests
pytest -x testing/coffee_test.py
```

---

## Class Design

### Book

| Component | Details |
|---|---|
| `__init__` | Takes `title` and `page_count` |
| `page_count` property | Must be an integer |
| `turn_page()` | Prints a page-turning message |

### Coffee

| Component | Details |
|---|---|
| `__init__` | Takes `size` and `price` |
| `size` property | Must be `Small`, `Medium`, or `Large` |
| `tip()` | Prints a tip message and increases price by 1 |

---

## Git Workflow

```bash
# Create a feature branch
git checkout -b feature/bookstore-oop

# Stage and commit changes
git add .
git commit -m "Add Book and Coffee classes with properties and methods"

# Push and open a Pull Request
git push origin feature/bookstore-oop

# After PR merge, clean up
git checkout main
git pull origin main
git branch -d feature/bookstore-oop
```