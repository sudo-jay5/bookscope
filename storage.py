import csv
import os

FIELDS = ["title", "price", "rating", "in_stock"]


def save_books(books, filename):
    folder = os.path.dirname(filename)
    if folder != "":
        os.makedirs(folder, exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for book in books:
            writer.writerow(book)


def load_books(filename):
    books = []
    if not os.path.exists(filename):
        return books
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = {
                "title": row["title"],
                "price": float(row["price"]),
                "rating": int(row["rating"]),
                "in_stock": int(row["in_stock"]),
            }
            books.append(book)
    return books
