from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to books.db
engine = create_engine('sqlite:///books.db')

# Create a metadata object
metadata = MetaData()
metadata.reflect(bind=engine)

# Access the book table
book_table = metadata.tables['book']

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query the database and print titles in alphabetical order
titles = session.query(book_table.c.title).order_by(book_table.c.title).all()

# Print the titles
for title in titles:
    print(title[0])

# Close the session
session.close()
