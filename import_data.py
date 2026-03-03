import pandas as pd
from database import SessionLocal, Book, engine

def import_books():
    print("Reading CSV files...")
    books_df = pd.read_csv('data/books.csv', sep=';', on_bad_lines='skip', low_memory=False, encoding='ISO-8859-1').head(5000)
    ratings_df = pd.read_csv('data/ratings.csv', sep=';', on_bad_lines='skip', low_memory=False, encoding='ISO-8859-1')

    print("Calculating average ratings...")
    explicit_ratings = ratings_df[ratings_df['Book-Rating'] > 0] 

    avg_ratings = explicit_ratings.groupby('ISBN')['Book-Rating'].mean().reset_index()
    
    merged_df = pd.merge(books_df, avg_ratings, on='ISBN', how='left').fillna(0)

    print("Saving to database...")
    db = SessionLocal()
    for _, row in merged_df.iterrows():
        new_book = Book(
            isbn=str(row['ISBN']),
            title=str(row['Book-Title']),
            author=str(row['Book-Author']),
            year=int(row['Year-Of-Publication']),
            publisher=str(row['Publisher']),
            average_rating=float(row['Book-Rating'])
        )
        db.add(new_book)
    
    db.commit()
    db.close()
    print("Import Complete!")

if __name__ == "__main__":
    import_books()