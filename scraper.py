import requests
from bs4 import BeautifulSoup
from database import BookDatabaseManager


URL = "https://books.toscrape.com/"


def convert_rating(rating_word):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    return rating_map.get(rating_word, 0)


def scrape_books():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    # Get only the first 20 books
    book_containers = soup.select("article.product_pod")[:20]

    for book in book_containers:

        # -------------------------
        # Title
        # -------------------------
        title_element = book.select_one("h3 a")
        title = title_element.get("title").strip()

        # -------------------------
        # Price
        # -------------------------
        price_element = book.select_one(".price_color")
        price_text = price_element.get_text(strip=True)

        # Remove pound symbol and possible encoding character
        price_text = (
            price_text
            .replace("£", "")
            .replace("Â", "")
            .strip()
        )

        price = float(price_text)

        # -------------------------
        # In Stock
        # -------------------------
        availability_element = book.select_one(".availability")
        availability = availability_element.get_text(
            " ",
            strip=True
        )

        in_stock = "In stock" in availability

        # -------------------------
        # Rating
        # -------------------------
        rating_element = book.select_one(".star-rating")

        rating_classes = rating_element.get("class", [])

        rating_word = None

        for rating_class in rating_classes:
            if rating_class in [
                "One",
                "Two",
                "Three",
                "Four",
                "Five"
            ]:
                rating_word = rating_class
                break

        rating = convert_rating(rating_word)

        # -------------------------
        # Store book
        # -------------------------
        books.append({
            "title": title,
            "price": price,
            "in_stock": in_stock,
            "rating": rating
        })

    return books


def main():

    print("Scraping first 20 books...")

    books = scrape_books()

    database = BookDatabaseManager()

    # Clear old records before inserting fresh data.
    # This prevents duplicate books if the scraper is run again.
    connection = database.get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books")

    connection.commit()
    connection.close()

    # Insert scraped books into database
    for book in books:

        database.create_book(
            title=book["title"],
            price=book["price"],
            in_stock=book["in_stock"],
            rating=book["rating"]
        )

    print(f"Successfully scraped and stored {len(books)} books.")

    print("\nStored Books:")
    print("-" * 80)

    for book in database.get_all_books():
        print(book)


if __name__ == "__main__":
    main()