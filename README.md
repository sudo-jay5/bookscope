# BookScope: Book Market Analyzer

A Python mini project that scrapes book data from [books.toscrape.com](https://books.toscrape.com), saves it to CSV, and analyses it with NumPy and SciPy. Results are shown in the terminal and as Matplotlib charts.

## Features

- Scrape book titles, prices, star ratings and stock status (Requests + BeautifulSoup)
- Price summary: mean, median, standard deviation, min, max
- Average price per star rating
- Statistical report with SciPy: correlation, trend line, t-test
- Top 5 best value books (rating per pound)
- Budget finder: top rated books within your budget
- Charts: price histogram, average price by rating, rating vs price scatter

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Menu and program flow |
| `scraper.py` | Fetches and parses web pages |
| `storage.py` | Saves and loads CSV data |
| `analysis.py` | NumPy and SciPy calculations |
| `plots.py` | Matplotlib charts |
| `requirements.txt` | Required libraries |

## Requirements

- Python 3.8 or newer
- Internet connection (for scraping)

## Installation

Clone the repository:

```
git clone https://github.com/sudo-jay5/bookscope.git
cd bookscope
```

Create and activate a virtual environment, then install the libraries.

**Linux / macOS (bash or zsh):**

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Linux (fish shell):**

```
python3 -m venv venv
source venv/bin/activate.fish
pip install -r requirements.txt
```

**Windows (Command Prompt):**

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

If chart windows do not open on Linux, install Tk (for example `sudo apt install python3-tk` on Debian/Ubuntu or `sudo pacman -S tk` on Arch). Charts are still saved in the `output` folder.

## How to Run

```
python main.py
```

1. Choose option **1** first and enter the number of pages to scrape (1 to 50, about 20 books per page). Use 50 for the full dataset.
2. After that, options 2 to 6 work on the saved data. The data is stored in `data/books.csv`, so you only need to scrape once.
3. Choose option **7** to exit.

## Topics Covered

Python programs and modules, keywords, operators, loops and control constructs, user defined functions, files, modules and packages, SciPy, NumPy, Matplotlib, web scraping, Requests and bs4.

## Team

- Add member names and roll numbers here
