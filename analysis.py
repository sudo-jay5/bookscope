import numpy as np
from scipy import stats


def get_prices(books):
    return np.array([book["price"] for book in books])


def get_ratings(books):
    return np.array([book["rating"] for book in books])


def price_summary(books):
    prices = get_prices(books)
    summary = {
        "count": len(prices),
        "mean": float(np.mean(prices)),
        "median": float(np.median(prices)),
        "std": float(np.std(prices)),
        "min": float(np.min(prices)),
        "max": float(np.max(prices)),
    }
    return summary


def average_price_by_rating(books):
    result = {}
    for rating in range(1, 6):
        group = [book["price"] for book in books if book["rating"] == rating]
        if len(group) > 0:
            result[rating] = float(np.mean(group))
    return result


def rating_price_correlation(books):
    ratings = get_ratings(books)
    prices = get_prices(books)
    if len(books) < 3 or np.std(ratings) == 0 or np.std(prices) == 0:
        return None
    r_value, p_value = stats.pearsonr(ratings, prices)
    return float(r_value), float(p_value)


def price_trend_line(books):
    ratings = get_ratings(books)
    prices = get_prices(books)
    if len(books) < 3 or np.std(ratings) == 0:
        return None
    result = stats.linregress(ratings, prices)
    return float(result.slope), float(result.intercept)


def compare_high_and_low_rated(books):
    high = [book["price"] for book in books if book["rating"] >= 4]
    low = [book["price"] for book in books if book["rating"] <= 2]
    if len(high) < 2 or len(low) < 2:
        return None
    t_value, p_value = stats.ttest_ind(high, low, equal_var=False)
    return float(np.mean(high)), float(np.mean(low)), float(t_value), float(p_value)


def best_value_books(books, count=5):
    value_scores = get_ratings(books) / get_prices(books)
    order = np.argsort(value_scores)[::-1]
    best = []
    for index in order[:count]:
        best.append(books[int(index)])
    return best


def rating_then_price(book):
    return (-book["rating"], book["price"])


def books_within_budget(books, budget, count=5):
    affordable = [book for book in books if book["price"] <= budget]
    affordable.sort(key=rating_then_price)
    return affordable[:count]
