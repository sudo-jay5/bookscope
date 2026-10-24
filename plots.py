import os
import numpy as np
import matplotlib.pyplot as plt
import analysis

OUTPUT_FOLDER = "output"


def save_and_show(figure_name):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    path = os.path.join(OUTPUT_FOLDER, figure_name)
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    print("Chart saved to", path)
    plt.show()
    plt.close()


def plot_price_histogram(books):
    prices = analysis.get_prices(books)
    plt.figure(figsize=(8, 5))
    plt.hist(prices, bins=15, color="steelblue", edgecolor="black")
    plt.axvline(np.mean(prices), color="red", linestyle="--", label="Mean")
    plt.axvline(np.median(prices), color="green", linestyle="--", label="Median")
    plt.title("Distribution of Book Prices")
    plt.xlabel("Price (GBP)")
    plt.ylabel("Number of books")
    plt.legend()
    save_and_show("price_histogram.png")


def plot_average_price_by_rating(books):
    averages = analysis.average_price_by_rating(books)
    ratings = list(averages.keys())
    values = list(averages.values())
    plt.figure(figsize=(8, 5))
    plt.bar(ratings, values, color="orange", edgecolor="black")
    plt.title("Average Price for Each Star Rating")
    plt.xlabel("Star rating")
    plt.ylabel("Average price (GBP)")
    save_and_show("average_price_by_rating.png")


def plot_rating_vs_price(books):
    ratings = analysis.get_ratings(books)
    prices = analysis.get_prices(books)
    plt.figure(figsize=(8, 5))
    plt.scatter(ratings, prices, alpha=0.4, color="purple")
    line = analysis.price_trend_line(books)
    if line is not None:
        slope, intercept = line
        x_values = np.array([1, 5])
        y_values = slope * x_values + intercept
        plt.plot(x_values, y_values, color="red", label="Trend line")
        plt.legend()
    plt.title("Star Rating vs Price")
    plt.xlabel("Star rating")
    plt.ylabel("Price (GBP)")
    save_and_show("rating_vs_price.png")
