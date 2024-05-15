from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    
    author = relationship('Author', back_populates='books')

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

# CRUD operations
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

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_authors(db: Session):
    return db.query(Author).all()

def get_books(db: Session):
    return db.query(Book).all()

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

def main():
    init_db()
    db: Session = SessionLocal()

    # Create authors
    author1 = create_author(db, "Author One")
    author2 = create_author(db, "Author Two")
    
    # Create books
    book1 = create_book(db, "Book One", author1.id)
    book2 = create_book(db, "Book Two", author2.id)

    # Read authors and books
    authors = get_authors(db)
    books = get_books(db)

    print(f"Authors: {authors}")
    print(f"Books: {books}")

    # Update author
    updated_author = update_author(db, author1.id, "Updated Author One")

    # Update book
    updated_book = update_book(db, book1.id, "Updated Book One", author2.id)

    # Delete author and book
    delete_author(db, author2.id)
    delete_book(db, book2.id)

    # Check results after updates and deletions
    authors = get_authors(db)
    books = get_books(db)

    print(f"Authors after updates: {authors}")
    print(f"Books after updates: {books}")

    db.close()

if __name__ == "__main__":
    main()
