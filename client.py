import requests
import pandas as pd
import matplotlib.pyplot as plt


API_URL = "http://127.0.0.1:8000/books"


def main():

    # Fetch data from FastAPI
    print("Fetching book data from FastAPI...")

    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    books = response.json()

    # Convert API response to Pandas DataFrame
    df = pd.DataFrame(books)

    # Print DataFrame
    print("\nBook DataFrame:")
    print("=" * 100)
    print(df.to_string(index=False))
    print("=" * 100)

    # Export DataFrame to CSV
    df.to_csv(
        "exported_books.csv",
        index=False
    )

    print("\nCSV file created successfully:")
    print("exported_books.csv")

    # Create scatter plot
    plt.figure(figsize=(8, 6))

    plt.scatter(
        df["price"],
        df["rating"]
    )

    plt.title("Price vs Rating")
    plt.xlabel("Price")
    plt.ylabel("Rating (1-5)")

    plt.grid(True)

    # Save the chart
    plt.savefig(
        "price_vs_rating.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("\nScatter plot created successfully:")
    print("price_vs_rating.png")

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()