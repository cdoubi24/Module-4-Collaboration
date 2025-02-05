from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    book_name: str
    author: str
    publisher: str

books_db = []  # In-memory database for storing books

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(i)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
