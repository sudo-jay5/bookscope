import os
import scraper
import storage
import analysis
import plots

DATA_FILE = os.path.join("data", "books.csv")


def show_menu():
    print()
    print("===== BookScope: Book Market Analyzer =====")
    print("1. Scrape books from the website")
    print("2. Show price summary")
    print("3. Show statistical report (SciPy)")
    print("4. Show top 5 best value books")
    print("5. Find books within my budget")
    print("6. Show charts (Matplotlib)")
    print("7. Exit")


def has_data(books):
    if len(books) == 0:
        print("No data yet. Choose option 1 first.")
        return False
    return True


def scrape_option():
    answer = input("How many pages to scrape (1 to 50)? ")
    if not answer.isdigit() or int(answer) < 1 or int(answer) > 50:
        print("Please enter a number between 1 and 50.")
        return []
    books = scraper.scrape_books(int(answer))
    if len(books) > 0:
        storage.save_books(books, DATA_FILE)
        print(len(books), "books saved to", DATA_FILE)
    return books


def summary_option(books):
    summary = analysis.price_summary(books)
    print()
    print("Total books :", summary["count"])
    print("Mean price  : {:.2f}".format(summary["mean"]))
    print("Median price: {:.2f}".format(summary["median"]))
    print("Std. dev.   : {:.2f}".format(summary["std"]))
    print("Cheapest    : {:.2f}".format(summary["min"]))
    print("Costliest   : {:.2f}".format(summary["max"]))
    print()
    print("Average price by star rating:")
    averages = analysis.average_price_by_rating(books)
    for rating in averages:
        print(" ", rating, "star : {:.2f}".format(averages[rating]))


def report_option(books):
    print()
    correlation = analysis.rating_price_correlation(books)
    if correlation is None:
        print("Not enough varied data for correlation.")
    else:
        r_value, p_value = correlation
        print("Correlation between rating and price: r = {:.3f}, p = {:.3f}".format(r_value, p_value))
        if p_value < 0.05:
            print("The relationship is statistically significant.")
        else:
            print("No significant relationship between rating and price.")
    line = analysis.price_trend_line(books)
    if line is not None:
        print("Trend line: price = {:.2f} x rating + {:.2f}".format(line[0], line[1]))
    comparison = analysis.compare_high_and_low_rated(books)
    if comparison is None:
        print("Not enough high and low rated books for a t-test.")
    else:
        high_mean, low_mean, t_value, p_value = comparison
        print("Mean price of 4-5 star books: {:.2f}".format(high_mean))
        print("Mean price of 1-2 star books: {:.2f}".format(low_mean))
        print("T-test: t = {:.3f}, p = {:.3f}".format(t_value, p_value))


def best_value_option(books):
    print()
    print("Top 5 best value books (rating per pound):")
    count = 1
    for book in analysis.best_value_books(books, 5):
        print(count, ".", book["title"], "|", book["rating"], "stars |", "{:.2f}".format(book["price"]))
        count = count + 1


def budget_option(books):
    text = input("Enter your budget in GBP: ")
    try:
        budget = float(text)
    except ValueError:
        print("That is not a valid number.")
        return
    results = analysis.books_within_budget(books, budget, 5)
    if len(results) == 0:
        print("No books found within that budget.")
        return
    print()
    print("Top rated books within", budget, "GBP:")
    for book in results:
        print("-", book["title"], "|", book["rating"], "stars |", "{:.2f}".format(book["price"]))


def charts_option(books):
    print("1. Price histogram")
    print("2. Average price by rating")
    print("3. Rating vs price scatter")
    choice = input("Choose a chart: ")
    if choice == "1":
        plots.plot_price_histogram(books)
    elif choice == "2":
        plots.plot_average_price_by_rating(books)
    elif choice == "3":
        plots.plot_rating_vs_price(books)
    else:
        print("Invalid chart choice.")


def main():
    books = storage.load_books(DATA_FILE)
    if len(books) > 0:
        print(len(books), "books loaded from saved file.")
    running = True
    while running:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            new_books = scrape_option()
            if len(new_books) > 0:
                books = new_books
        elif choice == "2" and has_data(books):
            summary_option(books)
        elif choice == "3" and has_data(books):
            report_option(books)
        elif choice == "4" and has_data(books):
            best_value_option(books)
        elif choice == "5" and has_data(books):
            budget_option(books)
        elif choice == "6" and has_data(books):
            charts_option(books)
        elif choice == "7":
            print("Goodbye!")
            running = False
        elif choice not in ["2", "3", "4", "5", "6"]:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
