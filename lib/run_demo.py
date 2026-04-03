# run_demo.py
# Run this to test everything works before pushing to GitHub:
#   python run_demo.py

from lib.book import Book
from lib.coffee import Coffee

# ─────────────────────────────────────────────
print("=" * 50)
print("1. BOOK OBJECT")
print("=" * 50)
book = Book("The Great Gatsby", 180)
print(f"Title: {book.title}")
print(f"Page Count: {book.page_count}")
book.turn_page()

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("2. BOOK - invalid page_count")
print("=" * 50)
book2 = Book("Bad Book", "not a number")

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("3. COFFEE OBJECT")
print("=" * 50)
coffee = Coffee("Medium", 3.50)
print(f"Size: {coffee.size}")
print(f"Price before tip: ${coffee.price}")
coffee.tip()
print(f"Price after tip: ${coffee.price}")

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("4. COFFEE - invalid size")
print("=" * 50)
coffee2 = Coffee("Huge", 5.00)

print("\n✅ All done!")