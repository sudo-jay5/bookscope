import time
import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def get_page(page_number):
    url = PAGE_URL.format(page_number)
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        return None
    response.encoding = "utf-8"
    return response.text


def clean_price(price_text):
    digits = ""
    for character in price_text:
        if character.isdigit() or character == ".":
            digits = digits + character
    return float(digits)


def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for item in soup.find_all("article", class_="product_pod"):
        title = item.h3.a["title"]
        price = clean_price(item.find("p", class_="price_color").text)
        rating_word = item.find("p", class_="star-rating")["class"][1]
        rating = RATING_WORDS[rating_word]
        stock_text = item.find("p", class_="instock").text.strip()
        if "In stock" in stock_text:
            in_stock = 1
        else:
            in_stock = 0
        books.append({"title": title, "price": price, "rating": rating, "in_stock": in_stock})
    return books


def scrape_books(max_pages):
    all_books = []
    for page_number in range(1, max_pages + 1):
        print("Scraping page", page_number, "of", max_pages)
        try:
            html = get_page(page_number)
        except requests.exceptions.RequestException as error:
            print("Network problem:", error)
            break
        if html is None:
            print("No more pages found.")
            break
        all_books = all_books + parse_books(html)
        time.sleep(0.5)
    return all_books
