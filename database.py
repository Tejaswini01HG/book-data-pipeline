import sqlite3


class BookDatabaseManager:
    def __init__(self, db_name="books.db"):
        self.db_name = db_name
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                in_stock BOOLEAN NOT NULL,
                rating INTEGER NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    # CREATE
    def create_book(self, title, price, in_stock, rating):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO books (title, price, in_stock, rating)
            VALUES (?, ?, ?, ?)
        """, (title, price, in_stock, rating))

        connection.commit()
        book_id = cursor.lastrowid
        connection.close()

        return self.get_book(book_id)

    # READ - all books
    def get_all_books(self):
        connection = self.get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        books = [dict(row) for row in cursor.fetchall()]

        connection.close()

        return books

    # READ - single book
    def get_book(self, book_id):
        connection = self.get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )

        book = cursor.fetchone()

        connection.close()

        if book:
            return dict(book)

        return None

    # UPDATE
    def update_book(self, book_id, title, price, in_stock, rating):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE books
            SET title = ?, price = ?, in_stock = ?, rating = ?
            WHERE id = ?
        """, (title, price, in_stock, rating, book_id))

        connection.commit()

        updated = cursor.rowcount > 0

        connection.close()

        if updated:
            return self.get_book(book_id)

        return None

    # DELETE
    def delete_book(self, book_id):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )

        connection.commit()

        deleted = cursor.rowcount > 0

        connection.close()

        return deleted