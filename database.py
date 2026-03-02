from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database file location
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create the connection engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True) # Auto-incrementing ID
    isbn = Column(String, unique=True, index=True)     # From 'ISBN'
    title = Column(String)                             # From 'Book-Title'
    author = Column(String)                            # From 'Book-Author'
    year = Column(Integer)                             # From 'Year-Of-Publication'
    publisher = Column(String)                         # From 'Publisher'
    average_rating = Column(Float, default=0.0)        # Calculated from ratings.csv

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database and 'books' table created successfully!")