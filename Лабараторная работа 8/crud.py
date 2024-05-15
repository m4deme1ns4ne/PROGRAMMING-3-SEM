from sqlalchemy.orm import Session
from models import Author, Book

# Create
def create_author(db: Session, name: str):
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def create_book(db: Session, title: str, author_id: int):
    book = Book(title=title, author_id=author_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

# Read
def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_authors(db: Session):
    return db.query(Author).all()

def get_books(db: Session):
    return db.query(Book).all()

# Update
def update_author(db: Session, author_id: int, name: str):
    author = get_author(db, author_id)
    if author:
        author.name = name
        db.commit()
        db.refresh(author)
    return author

def update_book(db: Session, book_id: int, title: str, author_id: int):
    book = get_book(db, book_id)
    if book:
        book.title = title
        book.author_id = author_id
        db.commit()
        db.refresh(book)
    return book

# Delete
def delete_author(db: Session, author_id: int):
    author = get_author(db, author_id)
    if author:
        db.delete(author)
        db.commit()
    return author

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book
