from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database

from pydantic import BaseModel

# Blueprint for creating a new book
class BookCreate(BaseModel):
    isbn: str
    title: str
    author: str
    year: int
    publisher: str

app = FastAPI(title="Book Discovery API")

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Discovery API! Go to /docs for the interactive UI."}

# Endpoint to get a list of books
@app.get("/books", response_model=List[dict])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(database.Book).offset(skip).limit(limit).all()
    # Convert SQLAlchemy objects to simple dictionaries
    return [
        {
            "id": b.id,
            "isbn": b.isbn,
            "title": b.title,
            "author": b.author,
            "year": b.year,
            "publisher": b.publisher,
            "average_rating": b.average_rating
        } for b in books
    ]

@app.post("/books", status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Create the database object
    new_book = database.Book(
        isbn=book.isbn,
        title=book.title,
        author=book.author,
        year=book.year,
        publisher=book.publisher,
        average_rating=0.0  # New books start with no rating
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book