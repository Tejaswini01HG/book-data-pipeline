from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from database import BookDatabaseManager


app = FastAPI(
    title="Book Data Pipeline API",
    description="REST API for Book Data",
    version="1.0.0"
)

database = BookDatabaseManager()


class Book(BaseModel):
    title: str
    price: float = Field(gt=0)
    in_stock: bool
    rating: int = Field(ge=1, le=5)


@app.get("/")
def home():
    return {
        "message": "Book Data Pipeline API is running",
        "books_endpoint": "/books",
        "documentation": "/docs"
    }


# GET all books
@app.get("/books")
def get_books():
    return database.get_all_books()


# GET one book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):

    book = database.get_book(book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# CREATE a new book
@app.post("/books", status_code=201)
def create_book(book: Book):

    return database.create_book(
        title=book.title,
        price=book.price,
        in_stock=book.in_stock,
        rating=book.rating
    )


# UPDATE an existing book
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):

    updated_book = database.update_book(
        book_id=book_id,
        title=book.title,
        price=book.price,
        in_stock=book.in_stock,
        rating=book.rating
    )

    if updated_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated_book


# DELETE a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    deleted = database.delete_book(book_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "message": f"Book {book_id} deleted successfully"
    }